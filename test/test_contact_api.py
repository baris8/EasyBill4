# coding: utf-8

"""
    easybill REST API

     The first version of the easybill REST API. [CHANGELOG](https://api.easybill.de/rest/v1/CHANGELOG.md)  ## Authentication  You can choose between two available methods: `Basic Auth` or `Bearer Token`.  In each HTTP request, one of the following HTTP headers is required:  ``` # Basic Auth Authorization: Basic base64_encode('<email>:<api_key>') # Bearer Token Authorization: Bearer <api_key> ```  ## Limitations  ### Request Limit  * PLUS: 10 requests per minute * BUSINESS: 60 requests per minute  If the limit is exceeded, you will receive the HTTP error: `429 Too Many Requests`  ### Result Limit  All result lists are limited to 100 by default. This limit can be increased by the query parameter `limit` to a maximum of 1000.  ## Query filter  Many list resources can be filtered. In `/documents` you can filter e.g. by number with `/documents?number=111028654`. If you want to filter multiple numbers, you can either enter them separated by commas `/documents?number=111028654,222006895` or as an array `/documents?number[]=111028654&number[]=222006895`.  **Warning**: The maximum size of an HTTP request line in bytes is 4094. If this limit is exceeded, you will receive the HTTP error: `414 Request-URI Too Large`  ### Escape commas in query  You can escape commans in query `name=Patrick\\, Peter` if you submit the header `X-Easybill-Escape: true` in your request.  ## Property login_id  This is the login of your admin or employee account.  ## Date and Date-Time format Please use the timezone `Europe/Berlin`. * **date** = *Y-m-d* = `2016-12-31` * **date-time** = *Y-m-d H:i:s* = `2016-12-31 03:13:37`  Date or datetime can be `null` because the attributes have been added later and the entry is older.  # noqa: E501

    The version of the OpenAPI document: 1.48.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.contact_api import ContactApi  # noqa: E501
from openapi_client.rest import ApiException


class TestContactApi(unittest.TestCase):
    """ContactApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.contact_api.ContactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_customer_id_contacts_get(self):
        """Test case for customers_customer_id_contacts_get

        Fetch customer contact list  # noqa: E501
        """
        pass

    def test_customers_customer_id_contacts_id_delete(self):
        """Test case for customers_customer_id_contacts_id_delete

        Delete contact  # noqa: E501
        """
        pass

    def test_customers_customer_id_contacts_id_get(self):
        """Test case for customers_customer_id_contacts_id_get

        Fetch contact  # noqa: E501
        """
        pass

    def test_customers_customer_id_contacts_id_put(self):
        """Test case for customers_customer_id_contacts_id_put

        Update Contact  # noqa: E501
        """
        pass

    def test_customers_customer_id_contacts_post(self):
        """Test case for customers_customer_id_contacts_post

        Create new contact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
