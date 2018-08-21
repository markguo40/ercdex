# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from erc_dex.models.account import Account  # noqa: F401,E501


class RebateContract(object):
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
        'id': 'float',
        'date_created': 'datetime',
        'date_updated': 'datetime',
        'tx_hash': 'str',
        'contract_address': 'str',
        'principal': 'str',
        'partner': 'str',
        'referrer': 'str',
        'account_id': 'float',
        'account': 'Account'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'tx_hash': 'txHash',
        'contract_address': 'contractAddress',
        'principal': 'principal',
        'partner': 'partner',
        'referrer': 'referrer',
        'account_id': 'accountId',
        'account': 'account'
    }

    def __init__(self, id=None, date_created=None, date_updated=None, tx_hash=None, contract_address=None, principal=None, partner=None, referrer=None, account_id=None, account=None):  # noqa: E501
        """RebateContract - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._date_updated = None
        self._tx_hash = None
        self._contract_address = None
        self._principal = None
        self._partner = None
        self._referrer = None
        self._account_id = None
        self._account = None
        self.discriminator = None

        self.id = id
        self.date_created = date_created
        self.date_updated = date_updated
        self.tx_hash = tx_hash
        self.contract_address = contract_address
        self.principal = principal
        self.partner = partner
        if referrer is not None:
            self.referrer = referrer
        self.account_id = account_id
        self.account = account

    @property
    def id(self):
        """Gets the id of this RebateContract.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this RebateContract.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RebateContract.

        Unique Identifier  # noqa: E501

        :param id: The id of this RebateContract.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this RebateContract.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The date_created of this RebateContract.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this RebateContract.

        Date of creation  # noqa: E501

        :param date_created: The date_created of this RebateContract.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this RebateContract.  # noqa: E501

        Date of updated  # noqa: E501

        :return: The date_updated of this RebateContract.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this RebateContract.

        Date of updated  # noqa: E501

        :param date_updated: The date_updated of this RebateContract.  # noqa: E501
        :type: datetime
        """
        if date_updated is None:
            raise ValueError("Invalid value for `date_updated`, must not be `None`")  # noqa: E501

        self._date_updated = date_updated

    @property
    def tx_hash(self):
        """Gets the tx_hash of this RebateContract.  # noqa: E501


        :return: The tx_hash of this RebateContract.  # noqa: E501
        :rtype: str
        """
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, tx_hash):
        """Sets the tx_hash of this RebateContract.


        :param tx_hash: The tx_hash of this RebateContract.  # noqa: E501
        :type: str
        """
        if tx_hash is None:
            raise ValueError("Invalid value for `tx_hash`, must not be `None`")  # noqa: E501

        self._tx_hash = tx_hash

    @property
    def contract_address(self):
        """Gets the contract_address of this RebateContract.  # noqa: E501


        :return: The contract_address of this RebateContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this RebateContract.


        :param contract_address: The contract_address of this RebateContract.  # noqa: E501
        :type: str
        """
        if contract_address is None:
            raise ValueError("Invalid value for `contract_address`, must not be `None`")  # noqa: E501

        self._contract_address = contract_address

    @property
    def principal(self):
        """Gets the principal of this RebateContract.  # noqa: E501


        :return: The principal of this RebateContract.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this RebateContract.


        :param principal: The principal of this RebateContract.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

    @property
    def partner(self):
        """Gets the partner of this RebateContract.  # noqa: E501


        :return: The partner of this RebateContract.  # noqa: E501
        :rtype: str
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this RebateContract.


        :param partner: The partner of this RebateContract.  # noqa: E501
        :type: str
        """
        if partner is None:
            raise ValueError("Invalid value for `partner`, must not be `None`")  # noqa: E501

        self._partner = partner

    @property
    def referrer(self):
        """Gets the referrer of this RebateContract.  # noqa: E501


        :return: The referrer of this RebateContract.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this RebateContract.


        :param referrer: The referrer of this RebateContract.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

    @property
    def account_id(self):
        """Gets the account_id of this RebateContract.  # noqa: E501


        :return: The account_id of this RebateContract.  # noqa: E501
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RebateContract.


        :param account_id: The account_id of this RebateContract.  # noqa: E501
        :type: float
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def account(self):
        """Gets the account of this RebateContract.  # noqa: E501


        :return: The account of this RebateContract.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this RebateContract.


        :param account: The account of this RebateContract.  # noqa: E501
        :type: Account
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RebateContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other