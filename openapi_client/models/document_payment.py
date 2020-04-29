# coding: utf-8

"""
    easybill REST API

     The first version of the easybill REST API. [CHANGELOG](https://api.easybill.de/rest/v1/CHANGELOG.md)  ## Authentication  You can choose between two available methods: `Basic Auth` or `Bearer Token`.  In each HTTP request, one of the following HTTP headers is required:  ``` # Basic Auth Authorization: Basic base64_encode('<email>:<api_key>') # Bearer Token Authorization: Bearer <api_key> ```  ## Limitations  ### Request Limit  * PLUS: 10 requests per minute * BUSINESS: 60 requests per minute  If the limit is exceeded, you will receive the HTTP error: `429 Too Many Requests`  ### Result Limit  All result lists are limited to 100 by default. This limit can be increased by the query parameter `limit` to a maximum of 1000.  ## Query filter  Many list resources can be filtered. In `/documents` you can filter e.g. by number with `/documents?number=111028654`. If you want to filter multiple numbers, you can either enter them separated by commas `/documents?number=111028654,222006895` or as an array `/documents?number[]=111028654&number[]=222006895`.  **Warning**: The maximum size of an HTTP request line in bytes is 4094. If this limit is exceeded, you will receive the HTTP error: `414 Request-URI Too Large`  ### Escape commas in query  You can escape commans in query `name=Patrick\\, Peter` if you submit the header `X-Easybill-Escape: true` in your request.  ## Property login_id  This is the login of your admin or employee account.  ## Date and Date-Time format Please use the timezone `Europe/Berlin`. * **date** = *Y-m-d* = `2016-12-31` * **date-time** = *Y-m-d H:i:s* = `2016-12-31 03:13:37`  Date or datetime can be `null` because the attributes have been added later and the entry is older.  # noqa: E501

    The version of the OpenAPI document: 1.48.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DocumentPayment(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'int',
        'document_id': 'int',
        'id': 'int',
        'is_overdue_fee': 'bool',
        'login_id': 'int',
        'notice': 'str',
        'payment_at': 'date',
        'type': 'str',
        'provider': 'str',
        'reference': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'document_id': 'document_id',
        'id': 'id',
        'is_overdue_fee': 'is_overdue_fee',
        'login_id': 'login_id',
        'notice': 'notice',
        'payment_at': 'payment_at',
        'type': 'type',
        'provider': 'provider',
        'reference': 'reference'
    }

    def __init__(self, amount=None, document_id=None, id=None, is_overdue_fee=None, login_id=None, notice='', payment_at=None, type='', provider='', reference='', local_vars_configuration=None):  # noqa: E501
        """DocumentPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._document_id = None
        self._id = None
        self._is_overdue_fee = None
        self._login_id = None
        self._notice = None
        self._payment_at = None
        self._type = None
        self._provider = None
        self._reference = None
        self.discriminator = None

        self.amount = amount
        self.document_id = document_id
        if id is not None:
            self.id = id
        if is_overdue_fee is not None:
            self.is_overdue_fee = is_overdue_fee
        if login_id is not None:
            self.login_id = login_id
        if notice is not None:
            self.notice = notice
        if payment_at is not None:
            self.payment_at = payment_at
        if type is not None:
            self.type = type
        if provider is not None:
            self.provider = provider
        if reference is not None:
            self.reference = reference

    @property
    def amount(self):
        """Gets the amount of this DocumentPayment.  # noqa: E501


        :return: The amount of this DocumentPayment.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DocumentPayment.


        :param amount: The amount of this DocumentPayment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def document_id(self):
        """Gets the document_id of this DocumentPayment.  # noqa: E501


        :return: The document_id of this DocumentPayment.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentPayment.


        :param document_id: The document_id of this DocumentPayment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and document_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def id(self):
        """Gets the id of this DocumentPayment.  # noqa: E501


        :return: The id of this DocumentPayment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentPayment.


        :param id: The id of this DocumentPayment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_overdue_fee(self):
        """Gets the is_overdue_fee of this DocumentPayment.  # noqa: E501


        :return: The is_overdue_fee of this DocumentPayment.  # noqa: E501
        :rtype: bool
        """
        return self._is_overdue_fee

    @is_overdue_fee.setter
    def is_overdue_fee(self, is_overdue_fee):
        """Sets the is_overdue_fee of this DocumentPayment.


        :param is_overdue_fee: The is_overdue_fee of this DocumentPayment.  # noqa: E501
        :type: bool
        """

        self._is_overdue_fee = is_overdue_fee

    @property
    def login_id(self):
        """Gets the login_id of this DocumentPayment.  # noqa: E501


        :return: The login_id of this DocumentPayment.  # noqa: E501
        :rtype: int
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """Sets the login_id of this DocumentPayment.


        :param login_id: The login_id of this DocumentPayment.  # noqa: E501
        :type: int
        """

        self._login_id = login_id

    @property
    def notice(self):
        """Gets the notice of this DocumentPayment.  # noqa: E501


        :return: The notice of this DocumentPayment.  # noqa: E501
        :rtype: str
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        """Sets the notice of this DocumentPayment.


        :param notice: The notice of this DocumentPayment.  # noqa: E501
        :type: str
        """

        self._notice = notice

    @property
    def payment_at(self):
        """Gets the payment_at of this DocumentPayment.  # noqa: E501


        :return: The payment_at of this DocumentPayment.  # noqa: E501
        :rtype: date
        """
        return self._payment_at

    @payment_at.setter
    def payment_at(self, payment_at):
        """Sets the payment_at of this DocumentPayment.


        :param payment_at: The payment_at of this DocumentPayment.  # noqa: E501
        :type: date
        """

        self._payment_at = payment_at

    @property
    def type(self):
        """Gets the type of this DocumentPayment.  # noqa: E501


        :return: The type of this DocumentPayment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentPayment.


        :param type: The type of this DocumentPayment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 255):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501

        self._type = type

    @property
    def provider(self):
        """Gets the provider of this DocumentPayment.  # noqa: E501


        :return: The provider of this DocumentPayment.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this DocumentPayment.


        :param provider: The provider of this DocumentPayment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                provider is not None and len(provider) > 255):
            raise ValueError("Invalid value for `provider`, length must be less than or equal to `255`")  # noqa: E501

        self._provider = provider

    @property
    def reference(self):
        """Gets the reference of this DocumentPayment.  # noqa: E501


        :return: The reference of this DocumentPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DocumentPayment.


        :param reference: The reference of this DocumentPayment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 255):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `255`")  # noqa: E501

        self._reference = reference

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentPayment):
            return True

        return self.to_dict() != other.to_dict()
