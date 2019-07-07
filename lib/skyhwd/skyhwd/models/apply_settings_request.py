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


class ApplySettingsRequest(object):
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
        'label': 'str',
        'use_passphrase': 'bool'
    }

    attribute_map = {
        'label': 'label',
        'use_passphrase': 'use_passphrase'
    }

    def __init__(self, label=None, use_passphrase=None):  # noqa: E501
        """ApplySettingsRequest - a model defined in OpenAPI"""  # noqa: E501

        self._label = None
        self._use_passphrase = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if use_passphrase is not None:
            self.use_passphrase = use_passphrase

    @property
    def label(self):
        """Gets the label of this ApplySettingsRequest.  # noqa: E501


        :return: The label of this ApplySettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ApplySettingsRequest.


        :param label: The label of this ApplySettingsRequest.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def use_passphrase(self):
        """Gets the use_passphrase of this ApplySettingsRequest.  # noqa: E501


        :return: The use_passphrase of this ApplySettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_passphrase

    @use_passphrase.setter
    def use_passphrase(self, use_passphrase):
        """Sets the use_passphrase of this ApplySettingsRequest.


        :param use_passphrase: The use_passphrase of this ApplySettingsRequest.  # noqa: E501
        :type: bool
        """

        self._use_passphrase = use_passphrase

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
        if not isinstance(other, ApplySettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
