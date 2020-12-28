# coding: utf-8

"""
    Safemat Api

    The Safemat REST API permits applications to connect securely to the Safemat software to carry out a multitude of operations.  Authentication and token-based access control is enforced.  ### Token: <table><thead><tr><th>Name</th><th>Token type</th><th>Lifetime</th></tr></thead><tbody><tr><td>Access token</td><td><a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://jwt.io/\">JWT</a>., Bearer token</td><td>60m</td></tr></tbody></table>  ### Access token usage  API requests (where authorisation is required) must include the bearer access token in the header.  Once the access token expires it should be refreshed.   ### How to determine if the token has expired <ol> <li>The API returns a 401 error.</li> <li>Check the <code>exp</code> field in the token payloads.</li> </ol>  ### Token structure  <table><thead><tr><th>Key name</th><th>Description</th></tr></thead><tbody><tr><td>exp</td><td>Expiration date and time in UNIX format</td></tr><tr><td>uid</td><td>Token owner(Unique number of devices(terminal))</td></tr><tr><td>terminal_id</td><td>Id in base of devices(terminal`s)</td></tr><tr><td>iat</td><td>Created date and time in UNIX format</td></tr></tbody></table>    # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SettingsResponce(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'bool',
        'data': 'SettingsData'
    }

    attribute_map = {
        'status': 'status',
        'data': 'data'
    }

    def __init__(self, status=None, data=None):  # noqa: E501
        """SettingsResponce - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._data = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data

    @property
    def status(self):
        """Gets the status of this SettingsResponce.  # noqa: E501


        :return: The status of this SettingsResponce.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SettingsResponce.


        :param status: The status of this SettingsResponce.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def data(self):
        """Gets the data of this SettingsResponce.  # noqa: E501


        :return: The data of this SettingsResponce.  # noqa: E501
        :rtype: SettingsData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SettingsResponce.


        :param data: The data of this SettingsResponce.  # noqa: E501
        :type: SettingsData
        """

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SettingsResponce, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingsResponce):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
