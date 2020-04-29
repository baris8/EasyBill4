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


class SerialNumber(object):
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
        'id': 'int',
        'serial_number': 'str',
        'position_id': 'int',
        'document_id': 'int',
        'document_position_id': 'int',
        'used_at': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'serial_number': 'serial_number',
        'position_id': 'position_id',
        'document_id': 'document_id',
        'document_position_id': 'document_position_id',
        'used_at': 'used_at',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, serial_number=None, position_id=None, document_id=None, document_position_id=None, used_at=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """SerialNumber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._serial_number = None
        self._position_id = None
        self._document_id = None
        self._document_position_id = None
        self._used_at = None
        self._created_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.serial_number = serial_number
        self.position_id = position_id
        self.document_id = document_id
        self.document_position_id = document_position_id
        self.used_at = used_at
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this SerialNumber.  # noqa: E501


        :return: The id of this SerialNumber.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SerialNumber.


        :param id: The id of this SerialNumber.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def serial_number(self):
        """Gets the serial_number of this SerialNumber.  # noqa: E501


        :return: The serial_number of this SerialNumber.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SerialNumber.


        :param serial_number: The serial_number of this SerialNumber.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and serial_number is None:  # noqa: E501
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def position_id(self):
        """Gets the position_id of this SerialNumber.  # noqa: E501


        :return: The position_id of this SerialNumber.  # noqa: E501
        :rtype: int
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this SerialNumber.


        :param position_id: The position_id of this SerialNumber.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and position_id is None:  # noqa: E501
            raise ValueError("Invalid value for `position_id`, must not be `None`")  # noqa: E501

        self._position_id = position_id

    @property
    def document_id(self):
        """Gets the document_id of this SerialNumber.  # noqa: E501


        :return: The document_id of this SerialNumber.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SerialNumber.


        :param document_id: The document_id of this SerialNumber.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def document_position_id(self):
        """Gets the document_position_id of this SerialNumber.  # noqa: E501


        :return: The document_position_id of this SerialNumber.  # noqa: E501
        :rtype: int
        """
        return self._document_position_id

    @document_position_id.setter
    def document_position_id(self, document_position_id):
        """Sets the document_position_id of this SerialNumber.


        :param document_position_id: The document_position_id of this SerialNumber.  # noqa: E501
        :type: int
        """

        self._document_position_id = document_position_id

    @property
    def used_at(self):
        """Gets the used_at of this SerialNumber.  # noqa: E501


        :return: The used_at of this SerialNumber.  # noqa: E501
        :rtype: str
        """
        return self._used_at

    @used_at.setter
    def used_at(self, used_at):
        """Sets the used_at of this SerialNumber.


        :param used_at: The used_at of this SerialNumber.  # noqa: E501
        :type: str
        """

        self._used_at = used_at

    @property
    def created_at(self):
        """Gets the created_at of this SerialNumber.  # noqa: E501


        :return: The created_at of this SerialNumber.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SerialNumber.


        :param created_at: The created_at of this SerialNumber.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if not isinstance(other, SerialNumber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SerialNumber):
            return True

        return self.to_dict() != other.to_dict()
