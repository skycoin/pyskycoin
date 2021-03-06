# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.26.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NetworkConnectionSchemaUnconfirmedVerifyTransaction(object):
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
        'burn_factor': 'int',
        'max_decimals': 'int',
        'max_transaction_size': 'int'
    }

    attribute_map = {
        'burn_factor': 'burn_factor',
        'max_decimals': 'max_decimals',
        'max_transaction_size': 'max_transaction_size'
    }

    def __init__(self, burn_factor=None, max_decimals=None, max_transaction_size=None):  # noqa: E501
        """NetworkConnectionSchemaUnconfirmedVerifyTransaction - a model defined in OpenAPI"""  # noqa: E501

        self._burn_factor = None
        self._max_decimals = None
        self._max_transaction_size = None
        self.discriminator = None

        if burn_factor is not None:
            self.burn_factor = burn_factor
        if max_decimals is not None:
            self.max_decimals = max_decimals
        if max_transaction_size is not None:
            self.max_transaction_size = max_transaction_size

    @property
    def burn_factor(self):
        """Gets the burn_factor of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501


        :return: The burn_factor of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :rtype: int
        """
        return self._burn_factor

    @burn_factor.setter
    def burn_factor(self, burn_factor):
        """Sets the burn_factor of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.


        :param burn_factor: The burn_factor of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :type: int
        """

        self._burn_factor = burn_factor

    @property
    def max_decimals(self):
        """Gets the max_decimals of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501


        :return: The max_decimals of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :rtype: int
        """
        return self._max_decimals

    @max_decimals.setter
    def max_decimals(self, max_decimals):
        """Sets the max_decimals of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.


        :param max_decimals: The max_decimals of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :type: int
        """

        self._max_decimals = max_decimals

    @property
    def max_transaction_size(self):
        """Gets the max_transaction_size of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501


        :return: The max_transaction_size of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :rtype: int
        """
        return self._max_transaction_size

    @max_transaction_size.setter
    def max_transaction_size(self, max_transaction_size):
        """Sets the max_transaction_size of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.


        :param max_transaction_size: The max_transaction_size of this NetworkConnectionSchemaUnconfirmedVerifyTransaction.  # noqa: E501
        :type: int
        """

        self._max_transaction_size = max_transaction_size

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
        if not isinstance(other, NetworkConnectionSchemaUnconfirmedVerifyTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
