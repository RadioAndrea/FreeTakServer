# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.auth_server import AuthServer  # noqa: F401,E501
from swagger_server.models.client import Client  # noqa: F401,E501
from swagger_server import util


class Oauth(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, client: List[Client]=None, auth_server: List[AuthServer]=None, oauth_add_anonymous: bool=None, read_only_group: str=None, read_group_suffix: str=None, write_group_suffix: str=None, groupprefix: str=None):  # noqa: E501
        """Oauth - a model defined in Swagger

        :param client: The client of this Oauth.  # noqa: E501
        :type client: List[Client]
        :param auth_server: The auth_server of this Oauth.  # noqa: E501
        :type auth_server: List[AuthServer]
        :param oauth_add_anonymous: The oauth_add_anonymous of this Oauth.  # noqa: E501
        :type oauth_add_anonymous: bool
        :param read_only_group: The read_only_group of this Oauth.  # noqa: E501
        :type read_only_group: str
        :param read_group_suffix: The read_group_suffix of this Oauth.  # noqa: E501
        :type read_group_suffix: str
        :param write_group_suffix: The write_group_suffix of this Oauth.  # noqa: E501
        :type write_group_suffix: str
        :param groupprefix: The groupprefix of this Oauth.  # noqa: E501
        :type groupprefix: str
        """
        self.swagger_types = {
            'client': List[Client],
            'auth_server': List[AuthServer],
            'oauth_add_anonymous': bool,
            'read_only_group': str,
            'read_group_suffix': str,
            'write_group_suffix': str,
            'groupprefix': str
        }

        self.attribute_map = {
            'client': 'client',
            'auth_server': 'authServer',
            'oauth_add_anonymous': 'oauthAddAnonymous',
            'read_only_group': 'readOnlyGroup',
            'read_group_suffix': 'readGroupSuffix',
            'write_group_suffix': 'writeGroupSuffix',
            'groupprefix': 'groupprefix'
        }
        self._client = client
        self._auth_server = auth_server
        self._oauth_add_anonymous = oauth_add_anonymous
        self._read_only_group = read_only_group
        self._read_group_suffix = read_group_suffix
        self._write_group_suffix = write_group_suffix
        self._groupprefix = groupprefix

    @classmethod
    def from_dict(cls, dikt) -> 'Oauth':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Oauth of this Oauth.  # noqa: E501
        :rtype: Oauth
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client(self) -> List[Client]:
        """Gets the client of this Oauth.


        :return: The client of this Oauth.
        :rtype: List[Client]
        """
        return self._client

    @client.setter
    def client(self, client: List[Client]):
        """Sets the client of this Oauth.


        :param client: The client of this Oauth.
        :type client: List[Client]
        """

        self._client = client

    @property
    def auth_server(self) -> List[AuthServer]:
        """Gets the auth_server of this Oauth.


        :return: The auth_server of this Oauth.
        :rtype: List[AuthServer]
        """
        return self._auth_server

    @auth_server.setter
    def auth_server(self, auth_server: List[AuthServer]):
        """Sets the auth_server of this Oauth.


        :param auth_server: The auth_server of this Oauth.
        :type auth_server: List[AuthServer]
        """

        self._auth_server = auth_server

    @property
    def oauth_add_anonymous(self) -> bool:
        """Gets the oauth_add_anonymous of this Oauth.


        :return: The oauth_add_anonymous of this Oauth.
        :rtype: bool
        """
        return self._oauth_add_anonymous

    @oauth_add_anonymous.setter
    def oauth_add_anonymous(self, oauth_add_anonymous: bool):
        """Sets the oauth_add_anonymous of this Oauth.


        :param oauth_add_anonymous: The oauth_add_anonymous of this Oauth.
        :type oauth_add_anonymous: bool
        """

        self._oauth_add_anonymous = oauth_add_anonymous

    @property
    def read_only_group(self) -> str:
        """Gets the read_only_group of this Oauth.


        :return: The read_only_group of this Oauth.
        :rtype: str
        """
        return self._read_only_group

    @read_only_group.setter
    def read_only_group(self, read_only_group: str):
        """Sets the read_only_group of this Oauth.


        :param read_only_group: The read_only_group of this Oauth.
        :type read_only_group: str
        """

        self._read_only_group = read_only_group

    @property
    def read_group_suffix(self) -> str:
        """Gets the read_group_suffix of this Oauth.


        :return: The read_group_suffix of this Oauth.
        :rtype: str
        """
        return self._read_group_suffix

    @read_group_suffix.setter
    def read_group_suffix(self, read_group_suffix: str):
        """Sets the read_group_suffix of this Oauth.


        :param read_group_suffix: The read_group_suffix of this Oauth.
        :type read_group_suffix: str
        """

        self._read_group_suffix = read_group_suffix

    @property
    def write_group_suffix(self) -> str:
        """Gets the write_group_suffix of this Oauth.


        :return: The write_group_suffix of this Oauth.
        :rtype: str
        """
        return self._write_group_suffix

    @write_group_suffix.setter
    def write_group_suffix(self, write_group_suffix: str):
        """Sets the write_group_suffix of this Oauth.


        :param write_group_suffix: The write_group_suffix of this Oauth.
        :type write_group_suffix: str
        """

        self._write_group_suffix = write_group_suffix

    @property
    def groupprefix(self) -> str:
        """Gets the groupprefix of this Oauth.


        :return: The groupprefix of this Oauth.
        :rtype: str
        """
        return self._groupprefix

    @groupprefix.setter
    def groupprefix(self, groupprefix: str):
        """Sets the groupprefix of this Oauth.


        :param groupprefix: The groupprefix of this Oauth.
        :type groupprefix: str
        """

        self._groupprefix = groupprefix