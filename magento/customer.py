# -*- coding: UTF-8 -*-
'''
    magento.customer

    Customer API for magento


    :license: BSD, see LICENSE for more details
'''
from magento.api import API


class Customer(API):
    """
    Customer API

    Example usage::

        from magento import Customer as CustomerAPI

        with CustomerAPI(url, username, password) as customer_api:
            return customer_api.list()
    """
    __slots__ = ()

    def list(self, filters=None):
        """
        Retreive list of customers

        :param filters: Dictionary of filters.

            Format: `{<attribute>:{<operator>:<value>}}`

            Example: `{'firstname':{'ilike':'sharoon'}}`
        :return: List of dictionaries of matching records
        """
        return self.get('customers',
                        {
                            'filters': filters
                        })

    def create(self, data):
        """
        Create a customer using the given data

        :param data: Dictionary of values
        :return: Integer ID of new record
        """
        return int(self.post('customers',
                             {
                                 'data': data
                             })
                   )

    def info(self, id, attributes=None):
        """
        Retrieve customer data

        :param id: ID of customer
        :param attributes: `List` of attributes needed
        """
        if attributes:
            return self.get('customers/%s' % (id,), {
                'attributes': attributes
            }
                            )

    def update(self, id, data):
        """
        Update a customer using the given data

        :param id: ID of the customer record to modify
        :param data: Dictionary of values
        :return: Boolean
        """
        return self.put('customers/%s' % (id,), {
            'data': data
        }
                        )

    def delete(self, id):
        """
        Delete a customer

        :param id: ID of customer to delete
        :return: Boolean
        """
        return self.delete('customers/%s' % (id,))


class CustomerGroup(API):
    """
    Customer Group API to connect to magento
    """
    __slots__ = ()

    def list(self):
        """
        Retreive list of customers

        :return: List of dictionaries of matching records
        """
        return self.get('customerGroups')


class CustomerAddress(API):
    """
    Customer Address API
    """
    __slots__ = ()

    def list(self, customer_id):
        """
        Retreive list of customer Addresses

        :param customer_id: ID of customer whose address needs to be fetched
        :return: List of dictionaries of matching records
        """
        return self.get('customers/addresses/%s' % (customer_id,))

    def create(self, customer_id, data):
        """
        Create a customer using the given data

        :param customer_id: ID of customer, whose address is being added
        :param data: Dictionary of values (country, zip, city, etc...)
        :return: Integer ID of new record
        """
        return int(self.post('customers',
                             {
                                 'data': data
                             })
                   )

    def info(self, id):
        """
        Retrieve customer data

        :param id: ID of customer
        """
        return self.get('customers/addresses/%s' % (id,))

    def update(self, id, data):
        """
        Update a customer address using the given data

        :param id: ID of the customer address record to modify
        :param data: Dictionary of values
        :return: Boolean
        """
        return self.put('customer_address.update', [id, data])

    def delete(self, id):
        """
        Delete a customer address

        :param id: ID of address to delete
        :return: Boolean
        """
        return self.delete('customer_address.delete', [id])
