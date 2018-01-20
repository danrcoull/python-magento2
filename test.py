import sys
from magento2dev import magento2

import logging

_logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', level=logging.DEBUG)

# ---------- CONFIG ----------------------------------------------------------------------------------------------------

url = 'http://bewusst.mageshops.com/'
apiuser = 'odoo'
apipass = 'odoo90odoo'

# ---------- CONNECT ---------------------------------------------------------------------------------------------------

# Create an instance of API
client = magento2.API(url, apiuser, apipass, protocol='rest')
client.connect()

# ========================= COUNTRIES ==================================================================================

# Get a list of countries
with magento2.Country(url, apiuser, apipass, protocol='rest') as country_api:
    countries = country_api.list()
    assert countries is not None
    _logger.info("Fetched countries")

# ========================= CATEGORIES =================================================================================

# Get a list of categories
categories = client.category.list()
assert categories is not None
_logger.info("Fetched categories")

# ========================= PRODUCTS ===================================================================================

# Get a list of products
product = client.product.list()
assert product is not None
_logger.info("Fetched products")



