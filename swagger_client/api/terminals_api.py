# coding: utf-8

"""
    Safemat Api

    The Safemat REST API permits applications to connect securely to the Safemat software to carry out a multitude of operations.  Authentication and token-based access control is enforced.  ### Token: <table><thead><tr><th>Name</th><th>Token type</th><th>Lifetime</th></tr></thead><tbody><tr><td>Access token</td><td><a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://jwt.io/\">JWT</a>., Bearer token</td><td>60m</td></tr></tbody></table>  ### Access token usage  API requests (where authorisation is required) must include the bearer access token in the header.  Once the access token expires it should be refreshed.   ### How to determine if the token has expired <ol> <li>The API returns a 401 error.</li> <li>Check the <code>exp</code> field in the token payloads.</li> </ol>  ### Token structure  <table><thead><tr><th>Key name</th><th>Description</th></tr></thead><tbody><tr><td>exp</td><td>Expiration date and time in UNIX format</td></tr><tr><td>uid</td><td>Token owner(Unique number of devices(terminal))</td></tr><tr><td>terminal_id</td><td>Id in base of devices(terminal`s)</td></tr><tr><td>iat</td><td>Created date and time in UNIX format</td></tr></tbody></table>    # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TerminalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_dispenser_levels(self, **kwargs):  # noqa: E501
        """Change cash levels  # noqa: E501

        Change cash levels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_dispenser_levels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: CreatedResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_dispenser_levels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.change_dispenser_levels_with_http_info(**kwargs)  # noqa: E501
            return data

    def change_dispenser_levels_with_http_info(self, **kwargs):  # noqa: E501
        """Change cash levels  # noqa: E501

        Change cash levels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_dispenser_levels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: CreatedResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_dispenser_levels" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/terminals/collection', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatedResponce',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dispenser_levels_info(self, **kwargs):  # noqa: E501
        """Info about levels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dispenser_levels_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CollectionResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dispenser_levels_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_dispenser_levels_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_dispenser_levels_info_with_http_info(self, **kwargs):  # noqa: E501
        """Info about levels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dispenser_levels_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: CollectionResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dispenser_levels_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/terminals/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionResponce',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def operation_acceptor(self, **kwargs):  # noqa: E501
        """Operation about accepter  # noqa: E501

        Operation about accepter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operation_acceptor(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: AccepterResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.operation_acceptor_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.operation_acceptor_with_http_info(**kwargs)  # noqa: E501
            return data

    def operation_acceptor_with_http_info(self, **kwargs):  # noqa: E501
        """Operation about accepter  # noqa: E501

        Operation about accepter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operation_acceptor_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: AccepterResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method operation_acceptor" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/terminals/accepter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccepterResponce',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def operation_d_get_settings(self, **kwargs):  # noqa: E501
        """Get settings for the terminal. If a new terminal is added to the list of new terminals  # noqa: E501

        Get settings for the terminal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operation_d_get_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: SettingsResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.operation_d_get_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.operation_d_get_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def operation_d_get_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Get settings for the terminal. If a new terminal is added to the list of new terminals  # noqa: E501

        Get settings for the terminal  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.operation_d_get_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :return: SettingsResponce
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method operation_d_get_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/terminals/settings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsResponce',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
