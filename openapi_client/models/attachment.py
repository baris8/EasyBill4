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


class Attachment(object):
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
        'created_at': 'date',
        'customer_id': 'int',
        'document_id': 'int',
        'file_name': 'str',
        'id': 'int',
        'project_id': 'int',
        'size': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'customer_id': 'customer_id',
        'document_id': 'document_id',
        'file_name': 'file_name',
        'id': 'id',
        'project_id': 'project_id',
        'size': 'size'
    }

    def __init__(self, created_at=None, customer_id=None, document_id=None, file_name=None, id=None, project_id=None, size=None, local_vars_configuration=None):  # noqa: E501
        """Attachment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._customer_id = None
        self._document_id = None
        self._file_name = None
        self._id = None
        self._project_id = None
        self._size = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        self.customer_id = customer_id
        self.document_id = document_id
        if file_name is not None:
            self.file_name = file_name
        if id is not None:
            self.id = id
        self.project_id = project_id
        if size is not None:
            self.size = size

    @property
    def created_at(self):
        """Gets the created_at of this Attachment.  # noqa: E501


        :return: The created_at of this Attachment.  # noqa: E501
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Attachment.


        :param created_at: The created_at of this Attachment.  # noqa: E501
        :type: date
        """

        self._created_at = created_at

    @property
    def customer_id(self):
        """Gets the customer_id of this Attachment.  # noqa: E501


        :return: The customer_id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Attachment.


        :param customer_id: The customer_id of this Attachment.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def document_id(self):
        """Gets the document_id of this Attachment.  # noqa: E501


        :return: The document_id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Attachment.


        :param document_id: The document_id of this Attachment.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def file_name(self):
        """Gets the file_name of this Attachment.  # noqa: E501


        :return: The file_name of this Attachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Attachment.


        :param file_name: The file_name of this Attachment.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def id(self):
        """Gets the id of this Attachment.  # noqa: E501


        :return: The id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attachment.


        :param id: The id of this Attachment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Attachment.  # noqa: E501


        :return: The project_id of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Attachment.


        :param project_id: The project_id of this Attachment.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def size(self):
        """Gets the size of this Attachment.  # noqa: E501

        In byte  # noqa: E501

        :return: The size of this Attachment.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Attachment.

        In byte  # noqa: E501

        :param size: The size of this Attachment.  # noqa: E501
        :type: int
        """

        self._size = size

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
        if not isinstance(other, Attachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attachment):
            return True

        return self.to_dict() != other.to_dict()
