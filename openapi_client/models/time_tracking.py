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


class TimeTracking(object):
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
        'cleared_at': 'datetime',
        'created_at': 'datetime',
        'date_from_at': 'datetime',
        'date_thru_at': 'datetime',
        'description': 'str',
        'hourly_rate': 'float',
        'id': 'int',
        'note': 'str',
        'number': 'str',
        'position_id': 'int',
        'project_id': 'int',
        'login_id': 'int',
        'timer_value': 'int'
    }

    attribute_map = {
        'cleared_at': 'cleared_at',
        'created_at': 'created_at',
        'date_from_at': 'date_from_at',
        'date_thru_at': 'date_thru_at',
        'description': 'description',
        'hourly_rate': 'hourly_rate',
        'id': 'id',
        'note': 'note',
        'number': 'number',
        'position_id': 'position_id',
        'project_id': 'project_id',
        'login_id': 'login_id',
        'timer_value': 'timer_value'
    }

    def __init__(self, cleared_at=None, created_at=None, date_from_at=None, date_thru_at=None, description=None, hourly_rate=0.0, id=None, note='null', number=None, position_id=None, project_id=None, login_id=None, timer_value=None, local_vars_configuration=None):  # noqa: E501
        """TimeTracking - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cleared_at = None
        self._created_at = None
        self._date_from_at = None
        self._date_thru_at = None
        self._description = None
        self._hourly_rate = None
        self._id = None
        self._note = None
        self._number = None
        self._position_id = None
        self._project_id = None
        self._login_id = None
        self._timer_value = None
        self.discriminator = None

        self.cleared_at = cleared_at
        if created_at is not None:
            self.created_at = created_at
        self.date_from_at = date_from_at
        self.date_thru_at = date_thru_at
        self.description = description
        if hourly_rate is not None:
            self.hourly_rate = hourly_rate
        if id is not None:
            self.id = id
        self.note = note
        self.number = number
        self.position_id = position_id
        self.project_id = project_id
        self.login_id = login_id
        self.timer_value = timer_value

    @property
    def cleared_at(self):
        """Gets the cleared_at of this TimeTracking.  # noqa: E501


        :return: The cleared_at of this TimeTracking.  # noqa: E501
        :rtype: datetime
        """
        return self._cleared_at

    @cleared_at.setter
    def cleared_at(self, cleared_at):
        """Sets the cleared_at of this TimeTracking.


        :param cleared_at: The cleared_at of this TimeTracking.  # noqa: E501
        :type: datetime
        """

        self._cleared_at = cleared_at

    @property
    def created_at(self):
        """Gets the created_at of this TimeTracking.  # noqa: E501


        :return: The created_at of this TimeTracking.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TimeTracking.


        :param created_at: The created_at of this TimeTracking.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def date_from_at(self):
        """Gets the date_from_at of this TimeTracking.  # noqa: E501


        :return: The date_from_at of this TimeTracking.  # noqa: E501
        :rtype: datetime
        """
        return self._date_from_at

    @date_from_at.setter
    def date_from_at(self, date_from_at):
        """Sets the date_from_at of this TimeTracking.


        :param date_from_at: The date_from_at of this TimeTracking.  # noqa: E501
        :type: datetime
        """

        self._date_from_at = date_from_at

    @property
    def date_thru_at(self):
        """Gets the date_thru_at of this TimeTracking.  # noqa: E501


        :return: The date_thru_at of this TimeTracking.  # noqa: E501
        :rtype: datetime
        """
        return self._date_thru_at

    @date_thru_at.setter
    def date_thru_at(self, date_thru_at):
        """Sets the date_thru_at of this TimeTracking.


        :param date_thru_at: The date_thru_at of this TimeTracking.  # noqa: E501
        :type: datetime
        """

        self._date_thru_at = date_thru_at

    @property
    def description(self):
        """Gets the description of this TimeTracking.  # noqa: E501


        :return: The description of this TimeTracking.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimeTracking.


        :param description: The description of this TimeTracking.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def hourly_rate(self):
        """Gets the hourly_rate of this TimeTracking.  # noqa: E501

        Hourly rate in cents (e.g. \"150\" = 1.50€)  # noqa: E501

        :return: The hourly_rate of this TimeTracking.  # noqa: E501
        :rtype: float
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate):
        """Sets the hourly_rate of this TimeTracking.

        Hourly rate in cents (e.g. \"150\" = 1.50€)  # noqa: E501

        :param hourly_rate: The hourly_rate of this TimeTracking.  # noqa: E501
        :type: float
        """

        self._hourly_rate = hourly_rate

    @property
    def id(self):
        """Gets the id of this TimeTracking.  # noqa: E501


        :return: The id of this TimeTracking.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimeTracking.


        :param id: The id of this TimeTracking.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def note(self):
        """Gets the note of this TimeTracking.  # noqa: E501


        :return: The note of this TimeTracking.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TimeTracking.


        :param note: The note of this TimeTracking.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def number(self):
        """Gets the number of this TimeTracking.  # noqa: E501

        Can be chosen freely  # noqa: E501

        :return: The number of this TimeTracking.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TimeTracking.

        Can be chosen freely  # noqa: E501

        :param number: The number of this TimeTracking.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def position_id(self):
        """Gets the position_id of this TimeTracking.  # noqa: E501


        :return: The position_id of this TimeTracking.  # noqa: E501
        :rtype: int
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """Sets the position_id of this TimeTracking.


        :param position_id: The position_id of this TimeTracking.  # noqa: E501
        :type: int
        """

        self._position_id = position_id

    @property
    def project_id(self):
        """Gets the project_id of this TimeTracking.  # noqa: E501


        :return: The project_id of this TimeTracking.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TimeTracking.


        :param project_id: The project_id of this TimeTracking.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def login_id(self):
        """Gets the login_id of this TimeTracking.  # noqa: E501

        If omitted or null, the currently active login is used.  # noqa: E501

        :return: The login_id of this TimeTracking.  # noqa: E501
        :rtype: int
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """Sets the login_id of this TimeTracking.

        If omitted or null, the currently active login is used.  # noqa: E501

        :param login_id: The login_id of this TimeTracking.  # noqa: E501
        :type: int
        """

        self._login_id = login_id

    @property
    def timer_value(self):
        """Gets the timer_value of this TimeTracking.  # noqa: E501

        Tracked time in minutes  # noqa: E501

        :return: The timer_value of this TimeTracking.  # noqa: E501
        :rtype: int
        """
        return self._timer_value

    @timer_value.setter
    def timer_value(self, timer_value):
        """Sets the timer_value of this TimeTracking.

        Tracked time in minutes  # noqa: E501

        :param timer_value: The timer_value of this TimeTracking.  # noqa: E501
        :type: int
        """

        self._timer_value = timer_value

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
        if not isinstance(other, TimeTracking):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeTracking):
            return True

        return self.to_dict() != other.to_dict()
