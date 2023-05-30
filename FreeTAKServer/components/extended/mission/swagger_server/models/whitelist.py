# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Whitelist(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, groups: List[str]=None, domain: str=None, token: str=None, private_group: bool=None, group: str=None):  # noqa: E501
        """Whitelist - a model defined in Swagger

        :param groups: The groups of this Whitelist.  # noqa: E501
        :type groups: List[str]
        :param domain: The domain of this Whitelist.  # noqa: E501
        :type domain: str
        :param token: The token of this Whitelist.  # noqa: E501
        :type token: str
        :param private_group: The private_group of this Whitelist.  # noqa: E501
        :type private_group: bool
        :param group: The group of this Whitelist.  # noqa: E501
        :type group: str
        """
        self.swagger_types = {
            'groups': List[str],
            'domain': str,
            'token': str,
            'private_group': bool,
            'group': str
        }

        self.attribute_map = {
            'groups': 'groups',
            'domain': 'domain',
            'token': 'token',
            'private_group': 'privateGroup',
            'group': 'group'
        }
        self._groups = groups
        self._domain = domain
        self._token = token
        self._private_group = private_group
        self._group = group

    @classmethod
    def from_dict(cls, dikt) -> 'Whitelist':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Whitelist of this Whitelist.  # noqa: E501
        :rtype: Whitelist
        """
        return util.deserialize_model(dikt, cls)

    @property
    def groups(self) -> List[str]:
        """Gets the groups of this Whitelist.


        :return: The groups of this Whitelist.
        :rtype: List[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups: List[str]):
        """Sets the groups of this Whitelist.


        :param groups: The groups of this Whitelist.
        :type groups: List[str]
        """

        self._groups = groups

    @property
    def domain(self) -> str:
        """Gets the domain of this Whitelist.


        :return: The domain of this Whitelist.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain: str):
        """Sets the domain of this Whitelist.


        :param domain: The domain of this Whitelist.
        :type domain: str
        """

        self._domain = domain

    @property
    def token(self) -> str:
        """Gets the token of this Whitelist.


        :return: The token of this Whitelist.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Whitelist.


        :param token: The token of this Whitelist.
        :type token: str
        """

        self._token = token

    @property
    def private_group(self) -> bool:
        """Gets the private_group of this Whitelist.


        :return: The private_group of this Whitelist.
        :rtype: bool
        """
        return self._private_group

    @private_group.setter
    def private_group(self, private_group: bool):
        """Sets the private_group of this Whitelist.


        :param private_group: The private_group of this Whitelist.
        :type private_group: bool
        """

        self._private_group = private_group

    @property
    def group(self) -> str:
        """Gets the group of this Whitelist.


        :return: The group of this Whitelist.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this Whitelist.


        :param group: The group of this Whitelist.
        :type group: str
        """

        self._group = group