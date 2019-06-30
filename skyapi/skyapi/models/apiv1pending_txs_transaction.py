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


class Apiv1pendingTxsTransaction(object):
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
        'outputs': 'list[Apiv1exploreraddressOutputs]',
        'inner_hash': 'str',
        'inputs': 'list[str]',
        'sigs': 'list[str]',
        'length': 'int',
        'txid': 'str',
        'type': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'outputs': 'outputs',
        'inner_hash': 'inner_hash',
        'inputs': 'inputs',
        'sigs': 'sigs',
        'length': 'length',
        'txid': 'txid',
        'type': 'type',
        'timestamp': 'timestamp'
    }

    def __init__(self, outputs=None, inner_hash=None, inputs=None, sigs=None, length=None, txid=None, type=None, timestamp=None):  # noqa: E501
        """Apiv1pendingTxsTransaction - a model defined in OpenAPI"""  # noqa: E501

        self._outputs = None
        self._inner_hash = None
        self._inputs = None
        self._sigs = None
        self._length = None
        self._txid = None
        self._type = None
        self._timestamp = None
        self.discriminator = None

        if outputs is not None:
            self.outputs = outputs
        if inner_hash is not None:
            self.inner_hash = inner_hash
        if inputs is not None:
            self.inputs = inputs
        if sigs is not None:
            self.sigs = sigs
        if length is not None:
            self.length = length
        if txid is not None:
            self.txid = txid
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def outputs(self):
        """Gets the outputs of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The outputs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: list[Apiv1exploreraddressOutputs]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Apiv1pendingTxsTransaction.


        :param outputs: The outputs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: list[Apiv1exploreraddressOutputs]
        """

        self._outputs = outputs

    @property
    def inner_hash(self):
        """Gets the inner_hash of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The inner_hash of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._inner_hash

    @inner_hash.setter
    def inner_hash(self, inner_hash):
        """Sets the inner_hash of this Apiv1pendingTxsTransaction.


        :param inner_hash: The inner_hash of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: str
        """

        self._inner_hash = inner_hash

    @property
    def inputs(self):
        """Gets the inputs of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The inputs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this Apiv1pendingTxsTransaction.


        :param inputs: The inputs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def sigs(self):
        """Gets the sigs of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The sigs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._sigs

    @sigs.setter
    def sigs(self, sigs):
        """Sets the sigs of this Apiv1pendingTxsTransaction.


        :param sigs: The sigs of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: list[str]
        """

        self._sigs = sigs

    @property
    def length(self):
        """Gets the length of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The length of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Apiv1pendingTxsTransaction.


        :param length: The length of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def txid(self):
        """Gets the txid of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The txid of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: str
        """
        return self._txid

    @txid.setter
    def txid(self, txid):
        """Sets the txid of this Apiv1pendingTxsTransaction.


        :param txid: The txid of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: str
        """

        self._txid = txid

    @property
    def type(self):
        """Gets the type of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The type of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Apiv1pendingTxsTransaction.


        :param type: The type of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this Apiv1pendingTxsTransaction.  # noqa: E501


        :return: The timestamp of this Apiv1pendingTxsTransaction.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Apiv1pendingTxsTransaction.


        :param timestamp: The timestamp of this Apiv1pendingTxsTransaction.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, Apiv1pendingTxsTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
