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


class Apiv1wallettransactionHoursSelection(object):
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
        'mode': 'str',
        'share_factor': 'str',
        'type': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'share_factor': 'share_factor',
        'type': 'type'
    }

    def __init__(self, mode=None, share_factor=None, type=None):  # noqa: E501
        """Apiv1wallettransactionHoursSelection - a model defined in OpenAPI"""  # noqa: E501

        self._mode = None
        self._share_factor = None
        self._type = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if share_factor is not None:
            self.share_factor = share_factor
        if type is not None:
            self.type = type

    @property
    def mode(self):
        """Gets the mode of this Apiv1wallettransactionHoursSelection.  # noqa: E501


        :return: The mode of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Apiv1wallettransactionHoursSelection.


        :param mode: The mode of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def share_factor(self):
        """Gets the share_factor of this Apiv1wallettransactionHoursSelection.  # noqa: E501


        :return: The share_factor of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :rtype: str
        """
        return self._share_factor

    @share_factor.setter
    def share_factor(self, share_factor):
        """Sets the share_factor of this Apiv1wallettransactionHoursSelection.


        :param share_factor: The share_factor of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :type: str
        """

        self._share_factor = share_factor

    @property
    def type(self):
        """Gets the type of this Apiv1wallettransactionHoursSelection.  # noqa: E501


        :return: The type of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Apiv1wallettransactionHoursSelection.


        :param type: The type of this Apiv1wallettransactionHoursSelection.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, Apiv1wallettransactionHoursSelection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
