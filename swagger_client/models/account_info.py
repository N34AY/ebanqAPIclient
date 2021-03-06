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

class AccountInfo(object):
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
        'id_user': 'int',
        'name': 'str',
        'account_bank_id': 'int',
        'bank': 'str',
        'balance': 'str',
        'type': 'str',
        'currency': 'str',
        'updated_at': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_user': 'id_user',
        'name': 'name',
        'account_bank_id': 'account_bank_id',
        'bank': 'bank',
        'balance': 'balance',
        'type': 'type',
        'currency': 'currency',
        'updated_at': 'updatedAt',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, id_user=None, name=None, account_bank_id=None, bank=None, balance=None, type=None, currency=None, updated_at=None, created_at=None):  # noqa: E501
        """AccountInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_user = None
        self._name = None
        self._account_bank_id = None
        self._bank = None
        self._balance = None
        self._type = None
        self._currency = None
        self._updated_at = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_user is not None:
            self.id_user = id_user
        if name is not None:
            self.name = name
        if account_bank_id is not None:
            self.account_bank_id = account_bank_id
        if bank is not None:
            self.bank = bank
        if balance is not None:
            self.balance = balance
        if type is not None:
            self.type = type
        if currency is not None:
            self.currency = currency
        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this AccountInfo.  # noqa: E501


        :return: The id of this AccountInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountInfo.


        :param id: The id of this AccountInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_user(self):
        """Gets the id_user of this AccountInfo.  # noqa: E501


        :return: The id_user of this AccountInfo.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this AccountInfo.


        :param id_user: The id_user of this AccountInfo.  # noqa: E501
        :type: int
        """

        self._id_user = id_user

    @property
    def name(self):
        """Gets the name of this AccountInfo.  # noqa: E501


        :return: The name of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountInfo.


        :param name: The name of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_bank_id(self):
        """Gets the account_bank_id of this AccountInfo.  # noqa: E501


        :return: The account_bank_id of this AccountInfo.  # noqa: E501
        :rtype: int
        """
        return self._account_bank_id

    @account_bank_id.setter
    def account_bank_id(self, account_bank_id):
        """Sets the account_bank_id of this AccountInfo.


        :param account_bank_id: The account_bank_id of this AccountInfo.  # noqa: E501
        :type: int
        """

        self._account_bank_id = account_bank_id

    @property
    def bank(self):
        """Gets the bank of this AccountInfo.  # noqa: E501


        :return: The bank of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this AccountInfo.


        :param bank: The bank of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._bank = bank

    @property
    def balance(self):
        """Gets the balance of this AccountInfo.  # noqa: E501


        :return: The balance of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountInfo.


        :param balance: The balance of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def type(self):
        """Gets the type of this AccountInfo.  # noqa: E501


        :return: The type of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountInfo.


        :param type: The type of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def currency(self):
        """Gets the currency of this AccountInfo.  # noqa: E501


        :return: The currency of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountInfo.


        :param currency: The currency of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def updated_at(self):
        """Gets the updated_at of this AccountInfo.  # noqa: E501


        :return: The updated_at of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AccountInfo.


        :param updated_at: The updated_at of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this AccountInfo.  # noqa: E501


        :return: The created_at of this AccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AccountInfo.


        :param created_at: The created_at of this AccountInfo.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(AccountInfo, dict):
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
        if not isinstance(other, AccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
