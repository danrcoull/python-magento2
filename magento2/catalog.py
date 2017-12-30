# -*- coding: UTF-8 -*-
'''
    magento.catalog

    Product Catalog API for magento see: https://devdocs.magento.com/guides/v2.1/rest/list.html#catalog

    :license: BSD, see LICENSE for more details
'''

import warnings

from .api import API


class Category(API):
    """
    Product Category API
    """
    __slots__ = ()

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        args = [store_view] if store_view else []
        return int(self.call('catalog_category.currentStore', args))

    def tree(self, parent_id=None, store_view=None):
        """
        Retrieve hierarchical tree of categories.

        :param parent_id: Integer ID of parent category (optional)
        :param store_view: Store View (optional)
        :return: dictionary of values
        """
        return self.call('catalog_category.tree', [parent_id, store_view])

    def level(self, website=None, store_view=None, parent_category=None):
        """
        Retrieve one level of categories by website/store view/parent category

        :param website: Website code or ID
        :param store_view: storeview code or ID
        :param parent_category: Parent Category ID
        :return: Dictionary
        """
        return self.call(
            'catalog_category.level', [website, store_view, parent_category]
        )

    def info(self, category_id, store_view=None, attributes=None):
        """
        Retrieve Category details

        :param category_id: ID of category to retrieve
        :param store_view: Store view ID or code
        :param attributes: Return the fields specified
        :return: Dictionary of data
        """
        return self.get(
            'categories/%s' % (category_id,),
            {
                'storeId': store_view
            }
        )

    def create(self, parent_id, data, store_view=None):
        """
        Create new category and return its ID

        :param parent_id: ID of parent
        :param data: Data for category
        :param store_view: Store view ID or Code
        :return: Integer ID
        """
        return int(self.post(
            'categories',
            {
                'parent_id': parent_id,
                'data': data,
                'storeId': store_view
            }
        ))

    def update(self, category_id, data, store_view=None):
        """
        Update Category

        :param category_id: ID of category
        :param data: Category Data
        :param store_view: Store view ID or code
        :return: Boolean
        """
        return bool(self.put(
            'categories/%s' % (category_id,),
            {
                'data': data,
                'storeId': store_view
            }
        ))

    def move(self, category_id, parent_id, after_id=None):
        """
        Move category in tree

        :param category_id: ID of category to move
        :param parent_id: New parent of the category
        :param after_id: Category ID after what position it will be moved
        :return: Boolean
        """
        return bool(self.call(
            'catalog_category.move', [category_id, parent_id, after_id])
        )

    def delete(self, category_id):
        """
        Delete category

        :param category_id: ID of category
        :return: Boolean
        """
        return bool(self.delete('categories/%s' % (category_id,)))

    def assignedproducts(self, category_id, store):
        """
        Retrieve list of assigned products

        :param category_id: Category ID
        :param store: Store ID or Code

        :return: Dictionary
        """
        return self.call(
            'catalog_category.assignedProducts', [category_id, store]
        )

    #: A proxy for :meth:`assignedproducts`
    assigned_products = assignedproducts

    def assignproduct(self, category_id, product, position=None):
        """
        Assign product to a category

        :param category_id: ID of a category
        :param product: ID or Code of the product
        :param position: Position of product in category

        :return: boolean
        """
        return bool(self.call(
            'catalog_category.assignProduct', [category_id, product, position])
        )

    #: A proxy for :meth:`assignproduct`
    assign_product = assignproduct

    def updateproduct(self, category_id, product, position=None):
        """
        Update assigned product

        :param category_id: ID of a category
        :param product: ID or Code of the product
        :param position: Position of product in category

        :return: boolean
        """
        return bool(self.call(
            'catalog_category.updateProduct', [category_id, product, position])
        )

    #: A proxy for :meth:`updateproduct`
    update_product = updateproduct

    def removeproduct(self, category_id, product):
        """
        Remove product from category

        :param category_id: ID of a category
        :param product: ID or Code of the product

        :return: boolean
        """
        return bool(self.call(
            'catalog_category.removeProduct', [category_id, product])
        )

    #: A proxy for :meth:`removeproduct`
    remove_product = removeproduct


class CategoryAttribute(API):
    """
    Product Category Attribute API to connect to magento
    Allows to get attributes and options for category.
    """
    __slots__ = ()

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        args = [store_view] if store_view else []
        return int(self.call('catalog_category_attribute.currentStore', args))

    def list(self):
        """
        Retrieve Category attrbutes
        """
        return self.get('categories/attributes', [])

    def options(self, attribute_id, store_view=None):
        """
        Retrieve attribute options

        :param attribute_id: ID of the attribute whose options are reqd
        :param store_view: ID or Code of the store view

        :return: list of dictionary
        """
        return self.get('categories/attributes/%s' % (attribute_id,))


class Product(API):
    """
    Product API for magento
    """
    __slots__ = ()


    def list(self, filters=None, store_view=None):
        """
        Retrieve product list by filters

        :param filters: Dictionary of filters.

               Format :
                   `{<attribute>:{<operator>:<value>}}`
               Example :
                   `{'firstname':{'ilike':'sharoon'}}`

        :param store_view: Code or ID of store view
        :return: `list` of `dict`
        """
        return self.get(
            'products',
            {
                'filters': filters,
                'storeId': store_view
            }
        )

    def info(self, product, store_view=None):
        """
        Retrieve product data

        :param product: ID or SKU of product
        :param store_view: ID or Code of store view
        :param attributes: List of fields required
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: `dict` of values
        """
        return self.get(
            'products/%s' % (product,),
            {
                'storeId': store_view
            }
        )

    def create(self, type_id, attribute_set_id, sku, data):
        """
        Create Product and return ID

        :param product_type: String type of product
        :param attribute_set_id: ID of attribute set
        :param sku: SKU of the product
        :param data: Dictionary of data
        :return: INT id of product created
        """
        return self.post(
            'products',
            {
                'product': {
                    'type_id': type_id,
                    'attribute_set_id': attribute_set_id,
                    'sku': sku,
                }.update(data)
            }
        )

    def update(self, sku, data):
        """
        Update product Information

        :param product: ID or SKU of product
        :param data: Dictionary of attributes to update
        :param store_view: ID or Code of store view
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: Boolean
        """
        return self.put(
            'products/%s' % sku,
            {
                'product': {
                }.update(data)
            }
        )

    def remove(self, sku):
        """
        Delete a product

        :param product: ID or SKU of product
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: Boolean
        """
        return self.delete(
            'products/%s' % sku, {}
        )
class ProductAttribute(API):
    """
    Product Attribute API
    """
    __slots__ = ()

    def list(self, attribute_set_id):
        """
        Retrieve product attribute list

        :param attribute_set_id: ID of attribute set
        :return: `list` of `dict`
        """
        return self.get('products/attribute-sets/%s/attributes' % attribute_set_id, {})

    def info(self, attributeCode):
        """
        Retrieve product attribute info

        :param attribute: ID or Code of the attribute
        :return: `list` of `dict`
        """
        return self.get('products/attributes/%s' % attributeCode)

    def options(self, attribute):
        """
        Retrieve product attribute options

        :param attribute: Code of the attribute
        :return: `list` of `dict`
        """
        return self.get('products/attributes/%s/options' % attribute)

    def addOption(self, attribute, label,value, data):
        """
        Create new options to attribute (Magento > 1.7.0)

        :param attribute: Code of the attribute.
        :param data: Dictionary of Data.
        :return: True if created.
        """
        return self.post('products/attributes/%s/options' % attribute, {
            'option': {
                'label': label,
                'value': value,
            }.update(data)
        })


    def removeOption(self, attributeCode, optionId):
        """
        Remove option to attribute (Magento > 1.7.0)

        :param attributeCode: Code of the attribute.
        :param optionId: Option ID.
        :return: True if the option is removed.
        """
        return self.delete('products/attributes/%s/options/%s' % (attributeCode, optionId))

    def create(self, attribute_code, label, frontendinput,  data):
        """
        Create attribute entity.

        :param data: Dictionary of entity data to create attribute with.
        :param attribute_code: Code for new attribute.
        :param label: Label for new attribute.
        :param frontendinput: Frontend Input type for new attribute use getTypes for a list of available.

        :return: Integer ID of attribute created
        """
        return self.post('products/attributes',
                         {
                             'attribute': {
                                 'attribute_code': attribute_code,
                                 'default_frontend_label': label,
                                 'frontend_input': frontendinput
                             }.update(data)
                         })

    def update(self, attributeCode, data):
        """
        Update attribute entity data.

        :param attribute:  Code of the attribute.
        :param data: Dictionary of entity data to update on attribute.

        :return: Dictionary
        """
        return self.post('products/attributes/%s' % attributeCode,
                         {
                             'attribute': {
                             }.update(data)
                         })

    def getTypes(self):
        """
        Get attribute frontend types.
        :return: Dictionary
        """
        return self.get('products/attributes/types',{})


class ProductAttributeSet(API):
    """
    Product Attribute Set API
    """
    __slots__ = ()

    def list(self):
        """
        Retrieve list of product attribute sets

        :return: `list` of `dict`
        """
        return self.call('catalog_product_attribute_set.list', [])

    def create(self, attribute_set_name, skeleton_set_id):
        """
        Create a new attribute set based on a "skeleton" attribute set.
        If unsure, use the "Default" attribute set as a skeleton.

        :param attribute_set_name: name of the new attribute set
        :param skeleton_set_id: id of the skeleton attribute set to base this set on.

        :return: Integer ID of new attribute set
        """
        return self.call('catalog_product_attribute_set.create', [attribute_set_name, skeleton_set_id])

    def attributeAdd(self, attribute_id, attribute_set_id):
        """
        Add an existing attribute to an attribute set.

        :param attribute_id: ID of the attribute to add
        :param attribute_set_id: ID of the attribute set to add to

        :return: Boolean
        """
        return self.call('catalog_product_attribute_set.attributeAdd', [attribute_id, attribute_set_id])

    def attributeRemove(self, attribute_id, attribute_set_id):
        """
        Remove an existing attribute to an attribute set.

        :param attribute_id: ID of the attribute to remove
        :param attribute_set_id: ID of the attribute set to remove from

        :return: Boolean
        """
        return self.call('catalog_product_attribute_set.attributeRemove', [attribute_id, attribute_set_id])



class ProductTypes(API):
    """
    Product Types API
    """
    __slots__ = ()

    def list(self):
        """
        Retrieve list of product types

        :return: `list` of `dict`
        """
        return self.call('catalog_product_type.list', [])


class ProductImages(API):
    """
    Product Images API
    """
    __slots__ = ()

    def currentStore(self, store_view=None):
        """
        Set/Get current store view

        :param store_view: Store view ID or Code
        :return: int
        """
        args = []
        if store_view:
            args = [store_view]
        return int(self.call('catalog_product_attribute_media.currentStore',
            args))

    def list(self, product, store_view=None, identifierType=None):
        """
        Retrieve product image list

        :param product: ID or SKU of product
        :param store_view: Code or ID of store view
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: `list` of `dict`
        """
        return self.call('catalog_product_attribute_media.list',
                [product, store_view, identifierType])

    def info(self, product, image_file, store_view=None, identifierType=None):
        """
        Retrieve product image data

        :param product: ID or SKU of product
        :param store_view: ID or Code of store view
        :param attributes: List of fields required
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: `list` of `dict`
        """
        return self.call('catalog_product_attribute_media.info',
                [product, image_file, store_view, identifierType])

    def types(self, attribute_set_id):
        """
        Retrieve product image types (image, small_image, thumbnail, etc.)

        :param attribute_set_id: ID of attribute set
        :return: `list` of `dict`
        """
        return self.call('catalog_product_attribute_media.types',
                [attribute_set_id])

    def create(self, product, data, store_view=None, identifierType=None):
        """
        Upload a new product image.

        :param product: ID or SKU of product
        :param data: `dict` of image data (label, position, exclude, types)
            Example: { 'label': 'description of photo',
                'position': '1', 'exclude': '0',
                'types': ['image', 'small_image', 'thumbnail']}
        :param store_view: Store view ID or Code
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: string - image file name
        """
        return self.call('catalog_product_attribute_media.create',
                [product, data, store_view, identifierType])

    def update(self, product, img_file_name, data, store_view=None,
               identifierType=None):
        """
        Update a product image.

        :param product: ID or SKU of product
        :param img_file_name: The image file name
            Example: '/m/y/my_image_thumb.jpg'
        :param data: `dict` of image data (label, position, exclude, types)
            Example: { 'label': 'description of photo',
                'position': '1', 'exclude': '0',
                'types': ['image', 'small_image', 'thumbnail']}
        :param store_view: Store view ID or Code
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: string - image file name
        """
        return self.call('catalog_product_attribute_media.update',
                [product, img_file_name, data, store_view, identifierType])

    def remove(self, product, img_file_name, identifierType=None):
        """
        Remove a product image.

        :param product: ID or SKU of product
        :param img_file_name: The image file name
            Example: '/m/y/my_image_thumb.jpg'
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: boolean
        """
        return self.call('catalog_product_attribute_media.remove',
                [product, img_file_name, identifierType])


class ProductTierPrice(API):
    """
    Product Tier Price API
    """
    __slots__ = ()

    def info(self, product, identifierType=None):
        """
        Retrieve product data

        :param product: ID or SKU of product
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: `list` of `dict`
        """
        return self.call('catalog_product_attribute_tier_price.info',
                         [product, identifierType])

    def update(self, product, data, identifierType=None):
        """
        Update product tier prices.

        Note: All existing tier prices for the product are replaced by the tier
        prices provided in data.

        :param product: ID or SKU of product
        :param data: List of dictionaries of tier price information
            Example:
                [{
                    'website': 'all',
                    'customer_group_id': '1',
                    'qty': '99.0000',
                    'price': '123.9900'
                },
                {
                    'website': 'all',
                    ...
                },...]
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: Boolean
        """
        return bool(self.call('catalog_product_attribute_tier_price.update',
                [product, data, identifierType]))


class ProductLinks(API):
    """
    Product links API (related, cross sells, up sells, grouped)
    """
    __slots__ = ()

    def list(self, link_type, product, identifierType=None):
        """
        Retrieve list of linked products

        :param link_type: type of link, one of 'cross_sell', 'up_sell',
                'related' or 'grouped'
        :param product: ID or SKU of product
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: `list` of `dict`
        """
        return self.call('catalog_product_link.list',
                         [link_type, product, identifierType])

    def assign(self, link_type, product, linked_product, data=None,
               identifierType=None):
        """
        Assign a product link

        :param link_type: type of link, one of 'cross_sell', 'up_sell',
                'related' or 'grouped'
        :param product: ID or SKU of product
        :param linked_product: ID or SKU of linked product
        :param data: dictionary of link data, (position, qty, etc.)
                Example: { 'position': '0', 'qty': 1}
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: boolean
        """
        return bool(self.call('catalog_product_link.assign',
                [link_type, product, linked_product, data, identifierType]))

    def update(self, link_type, product, linked_product, data=None,
               identifierType=None):
        """
        Update a product link

        :param link_type: type of link, one of 'cross_sell', 'up_sell',
                'related' or 'grouped'
        :param product: ID or SKU of product
        :param linked_product: ID or SKU of linked product
        :param data: dictionary of link data, (position, qty, etc.)
                Example: { 'position': '0', 'qty': 1}
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: boolean
        """
        return bool(self.call('catalog_product_link.update',
                [link_type, product, linked_product, data, identifierType]))

    def remove(self, link_type, product, linked_product, identifierType=None):
        """
        Remove a product link

        :param link_type: type of link, one of 'cross_sell', 'up_sell',
                'related' or 'grouped'
        :param product: ID or SKU of product
        :param linked_product: ID or SKU of linked product to unlink
        :param identifierType: Defines whether the product or SKU value is
                               passed in the "product" parameter.

        :return: boolean
        """
        return bool(self.call('catalog_product_link.remove',
                [link_type, product, linked_product, identifierType]))

    def types(self):
        """
        Retrieve a list of product link types

        :return: `list` of types
        """
        return self.call('catalog_product_link.types', [])

    def attributes(self, link_type):
        """
        Retrieve a list of attributes of a product link type

        :param link_type: type of link, one of 'cross_sell', 'up_sell',
                'related' or 'grouped'
        :return: `list` of `dict`
               Format :
                   `[{'code': <attribute code>, 'type': <attribute type>}, ...]`
               Example :
                   `[{'code': 'position', 'type': 'int'},
                     {'code': 'qty', 'type': 'decimal'}]`
        """
        return self.call('catalog_product_link.attributes', [link_type])


class ProductConfigurable(API):
    """
    Product Configurable API for magento.

    These API endpoints only work if you have zikzakmedia's
    magento_webservices Magento plugin installed.
    """
    __slots__ = ()

    def info(self, product):
        """
        Configurable product Info

        :param product: ID or SKU of product
        :return: List
        """
        return self.call('ol_catalog_product_link.list', [product])

    def getSuperAttributes(self, product):
        """
        Configurable Attributes product

        :param product: ID or SKU of product
        :return: List
        """
        return self.call('ol_catalog_product_link.listSuperAttributes',
            [product])

    def setSuperAttributeValues(self, product, attribute):
        """
        Configurable Attributes product

        :param product: ID or SKU of product
        :param attribute: ID attribute
        :return: List
        """
        return self.call('ol_catalog_product_link.setSuperAttributeValues',
            [product, attribute])

    def update(self, product, linked_products, attributes):
        """
        Configurable Update product

        :param product: ID or SKU of product
        :param linked_products: List ID or SKU of linked product to link
        :param attributes: dicc
        :return: True/False
        """
        return bool(self.call('ol_catalog_product_link.assign',
            [product, linked_products, attributes]))

    def remove(self, product, linked_products):
        """
        Remove a product link configurable

        :param product: ID or SKU of product
        :param linked_products: List ID or SKU of linked product to unlink
        """
        return bool(self.call('ol_catalog_product_link.remove',
            [product, linked_products]))


class Inventory(API):
    """
    Allows to update stock attributes (status, quantity)
    """
    __slots__ = ()

    def list(self, products):
        """
        Retrieve inventory stock data by product ids

        :param products: list of IDs or SKUs of products
        :return: `list` of `dict`
        """
        return self.get('stockItems')

    def update(self, product, data):
        """
        Update inventory stock data

        :param product: ID or SKU of product
        :param data: Dictionary of data to change,
            eg dict(qty=99, is_in_stock='1')

        :return: boolean
        """
        return bool(
            self.call(
                'cataloginventory_stock_item.update',
                [product, data]
                )
            )

    def update_multi(self, product_data_pairs):
        """
        It is usually expensive to update inventory on magento and this
        uses the multi call api to make it faster. The expected argument is
        a list of pairs of product and data dictionaries.
        """
        return self.multiCall([
            [
                'cataloginventory_stock_item.update',
                product_data_pair
            ]
            for product_data_pair in product_data_pairs
        ])
