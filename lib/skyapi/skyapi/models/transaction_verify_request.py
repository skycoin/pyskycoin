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


class TransactionVerifyRequest(object):
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
        'unsigned': 'bool',
        'encoded_transaction': 'str'
    }

    attribute_map = {
        'unsigned': 'unsigned',
        'encoded_transaction': 'encoded_transaction'
    }

    def __init__(self, unsigned=None, encoded_transaction=None):  # noqa: E501
        """TransactionVerifyRequest - a model defined in OpenAPI"""  # noqa: E501

        self._unsigned = None
        self._encoded_transaction = None
        self.discriminator = None

        if unsigned is not None:
            self.unsigned = unsigned
        if encoded_transaction is not None:
            self.encoded_transaction = encoded_transaction

    @property
    def unsigned(self):
        """Gets the unsigned of this TransactionVerifyRequest.  # noqa: E501


        :return: The unsigned of this TransactionVerifyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unsigned

    @unsigned.setter
    def unsigned(self, unsigned):
        """Sets the unsigned of this TransactionVerifyRequest.


        :param unsigned: The unsigned of this TransactionVerifyRequest.  # noqa: E501
        :type: bool
        """

        self._unsigned = unsigned

    @property
    def encoded_transaction(self):
        """Gets the encoded_transaction of this TransactionVerifyRequest.  # noqa: E501


        :return: The encoded_transaction of this TransactionVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._encoded_transaction

    @encoded_transaction.setter
    def encoded_transaction(self, encoded_transaction):
        """Sets the encoded_transaction of this TransactionVerifyRequest.


        :param encoded_transaction: The encoded_transaction of this TransactionVerifyRequest.  # noqa: E501
        :type: str
        """

        self._encoded_transaction = encoded_transaction

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
        if not isinstance(other, TransactionVerifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
