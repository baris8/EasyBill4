# coding: utf-8

"""
    easybill REST API

     The first version of the easybill REST API. [CHANGELOG](https://api.easybill.de/rest/v1/CHANGELOG.md)  ## Authentication  You can choose between two available methods: `Basic Auth` or `Bearer Token`.  In each HTTP request, one of the following HTTP headers is required:  ``` # Basic Auth Authorization: Basic base64_encode('<email>:<api_key>') # Bearer Token Authorization: Bearer <api_key> ```  ## Limitations  ### Request Limit  * PLUS: 10 requests per minute * BUSINESS: 60 requests per minute  If the limit is exceeded, you will receive the HTTP error: `429 Too Many Requests`  ### Result Limit  All result lists are limited to 100 by default. This limit can be increased by the query parameter `limit` to a maximum of 1000.  ## Query filter  Many list resources can be filtered. In `/documents` you can filter e.g. by number with `/documents?number=111028654`. If you want to filter multiple numbers, you can either enter them separated by commas `/documents?number=111028654,222006895` or as an array `/documents?number[]=111028654&number[]=222006895`.  **Warning**: The maximum size of an HTTP request line in bytes is 4094. If this limit is exceeded, you will receive the HTTP error: `414 Request-URI Too Large`  ### Escape commas in query  You can escape commans in query `name=Patrick\\, Peter` if you submit the header `X-Easybill-Escape: true` in your request.  ## Property login_id  This is the login of your admin or employee account.  ## Date and Date-Time format Please use the timezone `Europe/Berlin`. * **date** = *Y-m-d* = `2016-12-31` * **date-time** = *Y-m-d H:i:s* = `2016-12-31 03:13:37`  Date or datetime can be `null` because the attributes have been added later and the entry is older.  # noqa: E501

    The version of the OpenAPI document: 1.48.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.documents import Documents  # noqa: E501
from openapi_client.rest import ApiException

class TestDocuments(unittest.TestCase):
    """Documents unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Documents
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.documents.Documents()  # noqa: E501
        if include_optional :
            return Documents(
                items = [
                    openapi_client.models.document.Document(
                        address = openapi_client.models.address.address(), 
                        attachment_ids = [], 
                        label_address = openapi_client.models.label_address.label_address(), 
                        amount = 56, 
                        amount_net = 56, 
                        bank_debit_form = '0', 
                        billing_country = '0', 
                        calc_vat_from = 0, 
                        cancel_id = 56, 
                        cash_allowance = 1.337, 
                        cash_allowance_days = 56, 
                        cash_allowance_text = '0', 
                        contact_id = 56, 
                        contact_label = '0', 
                        contact_text = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        currency = 'EUR', 
                        customer_id = 56, 
                        customer_snapshot = openapi_client.models.customer_snapshot.customer_snapshot(), 
                        discount = '0', 
                        discount_type = 'PERCENT', 
                        document_date = 'Thu Feb 07 01:00:00 CET 2019', 
                        due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        edited_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        external_id = '0', 
                        replica_url = '0', 
                        grace_period = 56, 
                        due_in_days = 56, 
                        id = 56, 
                        is_archive = False, 
                        is_draft = True, 
                        is_replica = False, 
                        items = [
                            openapi_client.models.document_position.DocumentPosition(
                                number = '0', 
                                description = '0', 
                                quantity = 1.0, 
                                quantity_str = '0', 
                                unit = '0', 
                                type = 'POSITION', 
                                position = 56, 
                                single_price_net = 1.337, 
                                single_price_gross = 1.337, 
                                vat_percent = 0.0, 
                                discount = 1.337, 
                                discount_type = 'PERCENT', 
                                position_id = 56, 
                                total_price_net = 1.337, 
                                total_price_gross = 1.337, 
                                total_vat = 1.337, 
                                serial_number_id = '0', 
                                serial_number = '0', 
                                booking_account = '0', 
                                export_cost_1 = '0', 
                                export_cost_2 = '0', 
                                cost_price_net = 1.337, 
                                cost_price_total = 1.337, 
                                cost_price_charge = 1.337, 
                                cost_price_charge_type = 'PERCENT', 
                                item_type = 'UNDEFINED', 
                                id = 56, )
                            ], 
                        last_postbox_id = 56, 
                        login_id = 56, 
                        number = '0', 
                        order_number = '0', 
                        paid_amount = 56, 
                        paid_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        pdf_pages = 56, 
                        pdf_template = '0', 
                        project_id = 56, 
                        recurring_options = openapi_client.models.recurring_options.recurring_options(), 
                        ref_id = 56, 
                        service_date = openapi_client.models.service_date.service_date(), 
                        shipping_country = '0', 
                        status = 'ACCEPT', 
                        text = 'Vielen Dank für Ihren Auftrag!\n\nBitte begleichen Sie den offenen Betrag bis zum %DOKUMENT.DATUM-FAELLIG%.\n\nMit freundlichen Grüßen\n\n%FIRMA.FIRMA%\n', 
                        text_prefix = '%KUNDE.ANREDE%,\nnachfolgend berechnen wir Ihnen wie vorab besprochen:\n', 
                        text_tax = '0', 
                        title = '0', 
                        type = 'INVOICE', 
                        use_shipping_address = False, 
                        vat_country = '0', 
                        fulfillment_country = '0', 
                        vat_option = 'NULL', )
                    ]
            )
        else :
            return Documents(
        )

    def testDocuments(self):
        """Test Documents"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()