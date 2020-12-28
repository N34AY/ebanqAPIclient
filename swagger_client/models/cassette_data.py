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

class CassetteData(object):
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
        'id': 'int',
        'type': 'str',
        'denomination': 'str',
        'count': 'int',
        'banknote': 'CassetteDataBanknote'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'denomination': 'Denomination',
        'count': 'Count',
        'banknote': 'Banknote'
    }

    def __init__(self, id=None, type=None, denomination=None, count=None, banknote=None):  # noqa: E501
        """CassetteData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._denomination = None
        self._count = None
        self._banknote = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if denomination is not None:
            self.denomination = denomination
        if count is not None:
            self.count = count
        if banknote is not None:
            self.banknote = banknote

    @property
    def id(self):
        """Gets the id of this CassetteData.  # noqa: E501


        :return: The id of this CassetteData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CassetteData.


        :param id: The id of this CassetteData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this CassetteData.  # noqa: E501


        :return: The type of this CassetteData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CassetteData.


        :param type: The type of this CassetteData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def denomination(self):
        """Gets the denomination of this CassetteData.  # noqa: E501


        :return: The denomination of this CassetteData.  # noqa: E501
        :rtype: str
        """
        return self._denomination

    @denomination.setter
    def denomination(self, denomination):
        """Sets the denomination of this CassetteData.


        :param denomination: The denomination of this CassetteData.  # noqa: E501
        :type: str
        """

        self._denomination = denomination

    @property
    def count(self):
        """Gets the count of this CassetteData.  # noqa: E501


        :return: The count of this CassetteData.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CassetteData.


        :param count: The count of this CassetteData.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def banknote(self):
        """Gets the banknote of this CassetteData.  # noqa: E501


        :return: The banknote of this CassetteData.  # noqa: E501
        :rtype: CassetteDataBanknote
        """
        return self._banknote

    @banknote.setter
    def banknote(self, banknote):
        """Sets the banknote of this CassetteData.


        :param banknote: The banknote of this CassetteData.  # noqa: E501
        :type: CassetteDataBanknote
        """

        self._banknote = banknote

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
        if issubclass(CassetteData, dict):
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
        if not isinstance(other, CassetteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other