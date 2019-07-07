# coding: utf-8

"""
    Hardware Wallet Daemon API

    This is the hardware-wallet-daemon API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: steve@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SignMessageRequest(object):
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
        'address_n': 'int',
        'message': 'str'
    }

    attribute_map = {
        'address_n': 'address_n',
        'message': 'message'
    }

    def __init__(self, address_n=None, message=None):  # noqa: E501
        """SignMessageRequest - a model defined in OpenAPI"""  # noqa: E501

        self._address_n = None
        self._message = None
        self.discriminator = None

        self.address_n = address_n
        self.message = message

    @property
    def address_n(self):
        """Gets the address_n of this SignMessageRequest.  # noqa: E501


        :return: The address_n of this SignMessageRequest.  # noqa: E501
        :rtype: int
        """
        return self._address_n

    @address_n.setter
    def address_n(self, address_n):
        """Sets the address_n of this SignMessageRequest.


        :param address_n: The address_n of this SignMessageRequest.  # noqa: E501
        :type: int
        """
        if address_n is None:
            raise ValueError("Invalid value for `address_n`, must not be `None`")  # noqa: E501

        self._address_n = address_n

    @property
    def message(self):
        """Gets the message of this SignMessageRequest.  # noqa: E501


        :return: The message of this SignMessageRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SignMessageRequest.


        :param message: The message of this SignMessageRequest.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, SignMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
