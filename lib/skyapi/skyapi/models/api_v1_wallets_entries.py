# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.25.1
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ApiV1WalletsEntries(object):
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
        'public_key': 'str',
        'address': 'str'
    }

    attribute_map = {
        'public_key': 'public_key',
        'address': 'address'
    }

    def __init__(self, public_key=None, address=None):  # noqa: E501
        """ApiV1WalletsEntries - a model defined in OpenAPI"""  # noqa: E501

        self._public_key = None
        self._address = None
        self.discriminator = None

        if public_key is not None:
            self.public_key = public_key
        if address is not None:
            self.address = address

    @property
    def public_key(self):
        """Gets the public_key of this ApiV1WalletsEntries.  # noqa: E501


        :return: The public_key of this ApiV1WalletsEntries.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this ApiV1WalletsEntries.


        :param public_key: The public_key of this ApiV1WalletsEntries.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def address(self):
        """Gets the address of this ApiV1WalletsEntries.  # noqa: E501


        :return: The address of this ApiV1WalletsEntries.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ApiV1WalletsEntries.


        :param address: The address of this ApiV1WalletsEntries.  # noqa: E501
        :type: str
        """

        self._address = address

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
        if not isinstance(other, ApiV1WalletsEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
