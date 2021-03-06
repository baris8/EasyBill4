# coding: utf-8

# flake8: noqa
"""
    easybill REST API

     The first version of the easybill REST API. [CHANGELOG](https://api.easybill.de/rest/v1/CHANGELOG.md)  ## Authentication  You can choose between two available methods: `Basic Auth` or `Bearer Token`.  In each HTTP request, one of the following HTTP headers is required:  ``` # Basic Auth Authorization: Basic base64_encode('<email>:<api_key>') # Bearer Token Authorization: Bearer <api_key> ```  ## Limitations  ### Request Limit  * PLUS: 10 requests per minute * BUSINESS: 60 requests per minute  If the limit is exceeded, you will receive the HTTP error: `429 Too Many Requests`  ### Result Limit  All result lists are limited to 100 by default. This limit can be increased by the query parameter `limit` to a maximum of 1000.  ## Query filter  Many list resources can be filtered. In `/documents` you can filter e.g. by number with `/documents?number=111028654`. If you want to filter multiple numbers, you can either enter them separated by commas `/documents?number=111028654,222006895` or as an array `/documents?number[]=111028654&number[]=222006895`.  **Warning**: The maximum size of an HTTP request line in bytes is 4094. If this limit is exceeded, you will receive the HTTP error: `414 Request-URI Too Large`  ### Escape commas in query  You can escape commans in query `name=Patrick\\, Peter` if you submit the header `X-Easybill-Escape: true` in your request.  ## Property login_id  This is the login of your admin or employee account.  ## Date and Date-Time format Please use the timezone `Europe/Berlin`. * **date** = *Y-m-d* = `2016-12-31` * **date-time** = *Y-m-d H:i:s* = `2016-12-31 03:13:37`  Date or datetime can be `null` because the attributes have been added later and the entry is older.  # noqa: E501

    The version of the OpenAPI document: 1.48.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.attachment import Attachment
from openapi_client.models.attachments import Attachments
from openapi_client.models.attachments_all_of import AttachmentsAllOf
from openapi_client.models.contact import Contact
from openapi_client.models.contacts import Contacts
from openapi_client.models.contacts_all_of import ContactsAllOf
from openapi_client.models.customer import Customer
from openapi_client.models.customer_group import CustomerGroup
from openapi_client.models.customer_groups import CustomerGroups
from openapi_client.models.customer_groups_all_of import CustomerGroupsAllOf
from openapi_client.models.customer_snapshot import CustomerSnapshot
from openapi_client.models.customers import Customers
from openapi_client.models.customers_all_of import CustomersAllOf
from openapi_client.models.discount import Discount
from openapi_client.models.discount_position import DiscountPosition
from openapi_client.models.discount_position_group import DiscountPositionGroup
from openapi_client.models.discount_position_groups import DiscountPositionGroups
from openapi_client.models.discount_position_groups_all_of import DiscountPositionGroupsAllOf
from openapi_client.models.discount_positions import DiscountPositions
from openapi_client.models.discount_positions_all_of import DiscountPositionsAllOf
from openapi_client.models.document import Document
from openapi_client.models.document_address import DocumentAddress
from openapi_client.models.document_payment import DocumentPayment
from openapi_client.models.document_payments import DocumentPayments
from openapi_client.models.document_payments_all_of import DocumentPaymentsAllOf
from openapi_client.models.document_position import DocumentPosition
from openapi_client.models.document_recurring import DocumentRecurring
from openapi_client.models.documents import Documents
from openapi_client.models.documents_all_of import DocumentsAllOf
from openapi_client.models.list import List
from openapi_client.models.login import Login
from openapi_client.models.logins import Logins
from openapi_client.models.logins_all_of import LoginsAllOf
from openapi_client.models.pdf_template import PDFTemplate
from openapi_client.models.pdf_templates import PDFTemplates
from openapi_client.models.pdf_templates_all_of import PDFTemplatesAllOf
from openapi_client.models.position import Position
from openapi_client.models.position_export_identifier_extended import PositionExportIdentifierExtended
from openapi_client.models.position_group import PositionGroup
from openapi_client.models.position_groups import PositionGroups
from openapi_client.models.position_groups_all_of import PositionGroupsAllOf
from openapi_client.models.positions import Positions
from openapi_client.models.positions_all_of import PositionsAllOf
from openapi_client.models.post_box import PostBox
from openapi_client.models.post_box_request import PostBoxRequest
from openapi_client.models.post_boxes import PostBoxes
from openapi_client.models.post_boxes_all_of import PostBoxesAllOf
from openapi_client.models.project import Project
from openapi_client.models.projects import Projects
from openapi_client.models.projects_all_of import ProjectsAllOf
from openapi_client.models.sepa_payment import SEPAPayment
from openapi_client.models.sepa_payments import SEPAPayments
from openapi_client.models.sepa_payments_all_of import SEPAPaymentsAllOf
from openapi_client.models.serial_number import SerialNumber
from openapi_client.models.serial_numbers import SerialNumbers
from openapi_client.models.serial_numbers_all_of import SerialNumbersAllOf
from openapi_client.models.service_date import ServiceDate
from openapi_client.models.stock import Stock
from openapi_client.models.stocks import Stocks
from openapi_client.models.stocks_all_of import StocksAllOf
from openapi_client.models.task import Task
from openapi_client.models.tasks import Tasks
from openapi_client.models.tasks_all_of import TasksAllOf
from openapi_client.models.text_template import TextTemplate
from openapi_client.models.text_templates import TextTemplates
from openapi_client.models.text_templates_all_of import TextTemplatesAllOf
from openapi_client.models.time_tracking import TimeTracking
from openapi_client.models.time_trackings import TimeTrackings
from openapi_client.models.time_trackings_all_of import TimeTrackingsAllOf
from openapi_client.models.web_hook import WebHook
from openapi_client.models.web_hook_last_response import WebHookLastResponse
from openapi_client.models.web_hooks import WebHooks
from openapi_client.models.web_hooks_all_of import WebHooksAllOf
