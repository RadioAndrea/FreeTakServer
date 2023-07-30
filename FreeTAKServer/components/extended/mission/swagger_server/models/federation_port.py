# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FederationPort(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, port: int=None, tls_version: str=None):  # noqa: E501
        """FederationPort - a model defined in Swagger

        :param port: The port of this FederationPort.  # noqa: E501
        :type port: int
        :param tls_version: The tls_version of this FederationPort.  # noqa: E501
        :type tls_version: str
        """
        self.swagger_types = {
            'port': int,
            'tls_version': str
        }

        self.attribute_map = {
            'port': 'port',
            'tls_version': 'tlsVersion'
        }
        self._port = port
        self._tls_version = tls_version

    @classmethod
    def from_dict(cls, dikt) -> 'FederationPort':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FederationPort of this FederationPort.  # noqa: E501
        :rtype: FederationPort
        """
        return util.deserialize_model(dikt, cls)

    @property
    def port(self) -> int:
        """Gets the port of this FederationPort.


        :return: The port of this FederationPort.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this FederationPort.


        :param port: The port of this FederationPort.
        :type port: int
        """

        self._port = port

    @property
    def tls_version(self) -> str:
        """Gets the tls_version of this FederationPort.


        :return: The tls_version of this FederationPort.
        :rtype: str
        """
        return self._tls_version

    @tls_version.setter
    def tls_version(self, tls_version: str):
        """Sets the tls_version of this FederationPort.


        :param tls_version: The tls_version of this FederationPort.
        :type tls_version: str
        """

        self._tls_version = tls_version