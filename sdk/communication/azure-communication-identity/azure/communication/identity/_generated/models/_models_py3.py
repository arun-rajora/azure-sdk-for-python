# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar code: Required. The error code.
    :vartype code: str
    :ivar message: Required. The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.identity.models.CommunicationError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.identity.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innererror', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        **kwargs
    ):
        """
        :keyword code: Required. The error code.
        :paramtype code: str
        :keyword message: Required. The error message.
        :paramtype message: str
        """
        super(CommunicationError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = None
        self.details = None
        self.inner_error = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :ivar error: Required. The Communication Services error.
    :vartype error: ~azure.communication.identity.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        error: "CommunicationError",
        **kwargs
    ):
        """
        :keyword error: Required. The Communication Services error.
        :paramtype error: ~azure.communication.identity.models.CommunicationError
        """
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = error


class CommunicationIdentity(msrest.serialization.Model):
    """A communication identity.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Required. Identifier of the identity.
    :vartype id: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: str,
        **kwargs
    ):
        """
        :keyword id: Required. Identifier of the identity.
        :paramtype id: str
        """
        super(CommunicationIdentity, self).__init__(**kwargs)
        self.id = id


class CommunicationIdentityAccessToken(msrest.serialization.Model):
    """An access token.

    All required parameters must be populated in order to send to Azure.

    :ivar token: Required. The access token issued for the identity.
    :vartype token: str
    :ivar expires_on: Required. The expiry time of the token.
    :vartype expires_on: ~datetime.datetime
    """

    _validation = {
        'token': {'required': True},
        'expires_on': {'required': True},
    }

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'expires_on': {'key': 'expiresOn', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        token: str,
        expires_on: datetime.datetime,
        **kwargs
    ):
        """
        :keyword token: Required. The access token issued for the identity.
        :paramtype token: str
        :keyword expires_on: Required. The expiry time of the token.
        :paramtype expires_on: ~datetime.datetime
        """
        super(CommunicationIdentityAccessToken, self).__init__(**kwargs)
        self.token = token
        self.expires_on = expires_on


class CommunicationIdentityAccessTokenRequest(msrest.serialization.Model):
    """CommunicationIdentityAccessTokenRequest.

    All required parameters must be populated in order to send to Azure.

    :ivar scopes: Required. List of scopes attached to the token.
    :vartype scopes: list[str or ~azure.communication.identity.models.CommunicationTokenScope]
    """

    _validation = {
        'scopes': {'required': True},
    }

    _attribute_map = {
        'scopes': {'key': 'scopes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        scopes: List[Union[str, "CommunicationTokenScope"]],
        **kwargs
    ):
        """
        :keyword scopes: Required. List of scopes attached to the token.
        :paramtype scopes: list[str or ~azure.communication.identity.models.CommunicationTokenScope]
        """
        super(CommunicationIdentityAccessTokenRequest, self).__init__(**kwargs)
        self.scopes = scopes


class CommunicationIdentityAccessTokenResult(msrest.serialization.Model):
    """A communication identity with access token.

    All required parameters must be populated in order to send to Azure.

    :ivar identity: Required. A communication identity.
    :vartype identity: ~azure.communication.identity.models.CommunicationIdentity
    :ivar access_token: An access token.
    :vartype access_token: ~azure.communication.identity.models.CommunicationIdentityAccessToken
    """

    _validation = {
        'identity': {'required': True},
    }

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'CommunicationIdentity'},
        'access_token': {'key': 'accessToken', 'type': 'CommunicationIdentityAccessToken'},
    }

    def __init__(
        self,
        *,
        identity: "CommunicationIdentity",
        access_token: Optional["CommunicationIdentityAccessToken"] = None,
        **kwargs
    ):
        """
        :keyword identity: Required. A communication identity.
        :paramtype identity: ~azure.communication.identity.models.CommunicationIdentity
        :keyword access_token: An access token.
        :paramtype access_token: ~azure.communication.identity.models.CommunicationIdentityAccessToken
        """
        super(CommunicationIdentityAccessTokenResult, self).__init__(**kwargs)
        self.identity = identity
        self.access_token = access_token


class CommunicationIdentityCreateRequest(msrest.serialization.Model):
    """CommunicationIdentityCreateRequest.

    :ivar create_token_with_scopes: Also create access token for the created identity.
    :vartype create_token_with_scopes: list[str or
     ~azure.communication.identity.models.CommunicationTokenScope]
    """

    _attribute_map = {
        'create_token_with_scopes': {'key': 'createTokenWithScopes', 'type': '[str]'},
    }

    def __init__(
        self,
        *,
        create_token_with_scopes: Optional[List[Union[str, "CommunicationTokenScope"]]] = None,
        **kwargs
    ):
        """
        :keyword create_token_with_scopes: Also create access token for the created identity.
        :paramtype create_token_with_scopes: list[str or
         ~azure.communication.identity.models.CommunicationTokenScope]
        """
        super(CommunicationIdentityCreateRequest, self).__init__(**kwargs)
        self.create_token_with_scopes = create_token_with_scopes


class TeamsUserExchangeTokenRequest(msrest.serialization.Model):
    """TeamsUserExchangeTokenRequest.

    All required parameters must be populated in order to send to Azure.

    :ivar token: Required. Azure AD access token of a Teams User to acquire a new Communication
     Identity access token.
    :vartype token: str
    :ivar app_id: Required. Client ID of an Azure AD application to be verified against the appid
     claim in the Azure AD access token.
    :vartype app_id: str
    :ivar user_id: Required. Object ID of an Azure AD user (Teams User) to be verified against the
     oid claim in the Azure AD access token.
    :vartype user_id: str
    """

    _validation = {
        'token': {'required': True},
        'app_id': {'required': True},
        'user_id': {'required': True},
    }

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'app_id': {'key': 'appId', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        token: str,
        app_id: str,
        user_id: str,
        **kwargs
    ):
        """
        :keyword token: Required. Azure AD access token of a Teams User to acquire a new Communication
         Identity access token.
        :paramtype token: str
        :keyword app_id: Required. Client ID of an Azure AD application to be verified against the
         appid claim in the Azure AD access token.
        :paramtype app_id: str
        :keyword user_id: Required. Object ID of an Azure AD user (Teams User) to be verified against
         the oid claim in the Azure AD access token.
        :paramtype user_id: str
        """
        super(TeamsUserExchangeTokenRequest, self).__init__(**kwargs)
        self.token = token
        self.app_id = app_id
        self.user_id = user_id
