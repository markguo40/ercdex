# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from erc_dex.api_client import ApiClient


class OrdersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_orders(self, request, **kwargs):  # noqa: E501
        """cancel_orders  # noqa: E501

        Cancel one or more orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_orders(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param ICancelOrdersRequest request: (required)
        :return: list[ICancelOrderResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.cancel_orders_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_orders_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def cancel_orders_with_http_info(self, request, **kwargs):  # noqa: E501
        """cancel_orders  # noqa: E501

        Cancel one or more orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_orders_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param ICancelOrdersRequest request: (required)
        :return: list[ICancelOrderResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_orders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `cancel_orders`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/orders/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ICancelOrderResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_order(self, request, **kwargs):  # noqa: E501
        """create_order  # noqa: E501

        Submit a signed order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param IOrderCreationRequest request: (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_order_with_http_info(request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_order_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def create_order_with_http_info(self, request, **kwargs):  # noqa: E501
        """create_order  # noqa: E501

        Submit a signed order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order_with_http_info(request, async=True)
        >>> result = thread.get()

        :param async bool
        :param IOrderCreationRequest request: (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `create_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fee_recipients(self, **kwargs):  # noqa: E501
        """get_fee_recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fee_recipients(async=True)
        >>> result = thread.get()

        :param async bool
        :return: IFeeRecipientsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_fee_recipients_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fee_recipients_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_fee_recipients_with_http_info(self, **kwargs):  # noqa: E501
        """get_fee_recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_fee_recipients_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: IFeeRecipientsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fee_recipients" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/fee_recipients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IFeeRecipientsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_by_hash(self, order_hash, **kwargs):  # noqa: E501
        """get_order_by_hash  # noqa: E501

        Get a single order by hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_hash(order_hash, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_hash: Hex format hash of order parameters (required)
        :return: IOrderData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_order_by_hash_with_http_info(order_hash, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_by_hash_with_http_info(order_hash, **kwargs)  # noqa: E501
            return data

    def get_order_by_hash_with_http_info(self, order_hash, **kwargs):  # noqa: E501
        """get_order_by_hash  # noqa: E501

        Get a single order by hash  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_hash_with_http_info(order_hash, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_hash: Hex format hash of order parameters (required)
        :return: IOrderData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_hash']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_by_hash" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_hash' is set
        if ('order_hash' not in params or
                params['order_hash'] is None):
            raise ValueError("Missing the required parameter `order_hash` when calling `get_order_by_hash`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'order_hash' in params:
            path_params['orderHash'] = params['order_hash']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/{orderHash}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IOrderData',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_by_id(self, order_id, **kwargs):  # noqa: E501
        """get_order_by_id  # noqa: E501

        Get a single order by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_id(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param float order_id: (required)
        :return: IOrderData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_order_by_id_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_by_id_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def get_order_by_id_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """get_order_by_id  # noqa: E501

        Get a single order by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_id_with_http_info(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param float order_id: (required)
        :return: IOrderData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IOrderData',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_config(self, maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, **kwargs):  # noqa: E501
        """get_order_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_config(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str maker_address: (required)
        :param str taker_address: (required)
        :param str maker_asset_amount: (required)
        :param str taker_asset_amount: (required)
        :param str maker_asset_data: (required)
        :param str taker_asset_data: (required)
        :param str exchange_address: (required)
        :return: IOrderConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_order_config_with_http_info(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_config_with_http_info(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, **kwargs)  # noqa: E501
            return data

    def get_order_config_with_http_info(self, maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, **kwargs):  # noqa: E501
        """get_order_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_config_with_http_info(maker_address, taker_address, maker_asset_amount, taker_asset_amount, maker_asset_data, taker_asset_data, exchange_address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str maker_address: (required)
        :param str taker_address: (required)
        :param str maker_asset_amount: (required)
        :param str taker_asset_amount: (required)
        :param str maker_asset_data: (required)
        :param str taker_asset_data: (required)
        :param str exchange_address: (required)
        :return: IOrderConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['maker_address', 'taker_address', 'maker_asset_amount', 'taker_asset_amount', 'maker_asset_data', 'taker_asset_data', 'exchange_address']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_config" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'maker_address' is set
        if ('maker_address' not in params or
                params['maker_address'] is None):
            raise ValueError("Missing the required parameter `maker_address` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'taker_address' is set
        if ('taker_address' not in params or
                params['taker_address'] is None):
            raise ValueError("Missing the required parameter `taker_address` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'maker_asset_amount' is set
        if ('maker_asset_amount' not in params or
                params['maker_asset_amount'] is None):
            raise ValueError("Missing the required parameter `maker_asset_amount` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'taker_asset_amount' is set
        if ('taker_asset_amount' not in params or
                params['taker_asset_amount'] is None):
            raise ValueError("Missing the required parameter `taker_asset_amount` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'maker_asset_data' is set
        if ('maker_asset_data' not in params or
                params['maker_asset_data'] is None):
            raise ValueError("Missing the required parameter `maker_asset_data` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'taker_asset_data' is set
        if ('taker_asset_data' not in params or
                params['taker_asset_data'] is None):
            raise ValueError("Missing the required parameter `taker_asset_data` when calling `get_order_config`")  # noqa: E501
        # verify the required parameter 'exchange_address' is set
        if ('exchange_address' not in params or
                params['exchange_address'] is None):
            raise ValueError("Missing the required parameter `exchange_address` when calling `get_order_config`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'maker_address' in params:
            query_params.append(('makerAddress', params['maker_address']))  # noqa: E501
        if 'taker_address' in params:
            query_params.append(('takerAddress', params['taker_address']))  # noqa: E501
        if 'maker_asset_amount' in params:
            query_params.append(('makerAssetAmount', params['maker_asset_amount']))  # noqa: E501
        if 'taker_asset_amount' in params:
            query_params.append(('takerAssetAmount', params['taker_asset_amount']))  # noqa: E501
        if 'maker_asset_data' in params:
            query_params.append(('makerAssetData', params['maker_asset_data']))  # noqa: E501
        if 'taker_asset_data' in params:
            query_params.append(('takerAssetData', params['taker_asset_data']))  # noqa: E501
        if 'exchange_address' in params:
            query_params.append(('exchangeAddress', params['exchange_address']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order_config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IOrderConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_orderbook(self, base_asset_data, quote_asset_data, **kwargs):  # noqa: E501
        """get_orderbook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_orderbook(base_asset_data, quote_asset_data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str base_asset_data: (required)
        :param str quote_asset_data: (required)
        :param float per_page:
        :param float page:
        :return: IOrderbookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_orderbook_with_http_info(base_asset_data, quote_asset_data, **kwargs)  # noqa: E501
        else:
            (data) = self.get_orderbook_with_http_info(base_asset_data, quote_asset_data, **kwargs)  # noqa: E501
            return data

    def get_orderbook_with_http_info(self, base_asset_data, quote_asset_data, **kwargs):  # noqa: E501
        """get_orderbook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_orderbook_with_http_info(base_asset_data, quote_asset_data, async=True)
        >>> result = thread.get()

        :param async bool
        :param str base_asset_data: (required)
        :param str quote_asset_data: (required)
        :param float per_page:
        :param float page:
        :return: IOrderbookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['base_asset_data', 'quote_asset_data', 'per_page', 'page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orderbook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'base_asset_data' is set
        if ('base_asset_data' not in params or
                params['base_asset_data'] is None):
            raise ValueError("Missing the required parameter `base_asset_data` when calling `get_orderbook`")  # noqa: E501
        # verify the required parameter 'quote_asset_data' is set
        if ('quote_asset_data' not in params or
                params['quote_asset_data'] is None):
            raise ValueError("Missing the required parameter `quote_asset_data` when calling `get_orderbook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'base_asset_data' in params:
            query_params.append(('baseAssetData', params['base_asset_data']))  # noqa: E501
        if 'quote_asset_data' in params:
            query_params.append(('quoteAssetData', params['quote_asset_data']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/orderbook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IOrderbookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_orders(self, **kwargs):  # noqa: E501
        """get_orders  # noqa: E501

        Get a list of orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_orders(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool open: Include orders that are open; if false, only closed orders are returned
        :param float page: Page number
        :param float per_page: Page size
        :param str exchange_address: 0x contract exchange address
        :param str fee_recipient_address: Fee recipient address
        :param str taker_asset_data: Encoded taker asset data
        :param str maker_asset_data: Encoded maker asset data
        :param str sender_address: Designated address to execute orders
        :param str trader_asset_data: Encoded asset data (could be maker or taker)
        :param str trader_address: Trader address (could be makerAddress or takerAddress)
        :param str taker_asset_address: Token address of taker asset
        :param str taker_address: Address of order taker
        :param str maker_asset_address: Token address of maker asset
        :param str maker_address: Address of order maker
        :param str maker_asset_proxy_id: Maker asset proxy ID (ERC20 proxy only
        :param str taker_asset_proxy_id: Taker asset proxy ID (ERC20 proxy only)
        :param str pair:
        :return: IGetOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_orders_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_orders_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_orders_with_http_info(self, **kwargs):  # noqa: E501
        """get_orders  # noqa: E501

        Get a list of orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_orders_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool open: Include orders that are open; if false, only closed orders are returned
        :param float page: Page number
        :param float per_page: Page size
        :param str exchange_address: 0x contract exchange address
        :param str fee_recipient_address: Fee recipient address
        :param str taker_asset_data: Encoded taker asset data
        :param str maker_asset_data: Encoded maker asset data
        :param str sender_address: Designated address to execute orders
        :param str trader_asset_data: Encoded asset data (could be maker or taker)
        :param str trader_address: Trader address (could be makerAddress or takerAddress)
        :param str taker_asset_address: Token address of taker asset
        :param str taker_address: Address of order taker
        :param str maker_asset_address: Token address of maker asset
        :param str maker_address: Address of order maker
        :param str maker_asset_proxy_id: Maker asset proxy ID (ERC20 proxy only
        :param str taker_asset_proxy_id: Taker asset proxy ID (ERC20 proxy only)
        :param str pair:
        :return: IGetOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['open', 'page', 'per_page', 'exchange_address', 'fee_recipient_address', 'taker_asset_data', 'maker_asset_data', 'sender_address', 'trader_asset_data', 'trader_address', 'taker_asset_address', 'taker_address', 'maker_asset_address', 'maker_address', 'maker_asset_proxy_id', 'taker_asset_proxy_id', 'pair']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orders" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'open' in params:
            query_params.append(('open', params['open']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'exchange_address' in params:
            query_params.append(('exchangeAddress', params['exchange_address']))  # noqa: E501
        if 'fee_recipient_address' in params:
            query_params.append(('feeRecipientAddress', params['fee_recipient_address']))  # noqa: E501
        if 'taker_asset_data' in params:
            query_params.append(('takerAssetData', params['taker_asset_data']))  # noqa: E501
        if 'maker_asset_data' in params:
            query_params.append(('makerAssetData', params['maker_asset_data']))  # noqa: E501
        if 'sender_address' in params:
            query_params.append(('senderAddress', params['sender_address']))  # noqa: E501
        if 'trader_asset_data' in params:
            query_params.append(('traderAssetData', params['trader_asset_data']))  # noqa: E501
        if 'trader_address' in params:
            query_params.append(('traderAddress', params['trader_address']))  # noqa: E501
        if 'taker_asset_address' in params:
            query_params.append(('takerAssetAddress', params['taker_asset_address']))  # noqa: E501
        if 'taker_address' in params:
            query_params.append(('takerAddress', params['taker_address']))  # noqa: E501
        if 'maker_asset_address' in params:
            query_params.append(('makerAssetAddress', params['maker_asset_address']))  # noqa: E501
        if 'maker_address' in params:
            query_params.append(('makerAddress', params['maker_address']))  # noqa: E501
        if 'maker_asset_proxy_id' in params:
            query_params.append(('makerAssetProxyId', params['maker_asset_proxy_id']))  # noqa: E501
        if 'taker_asset_proxy_id' in params:
            query_params.append(('takerAssetProxyId', params['taker_asset_proxy_id']))  # noqa: E501
        if 'pair' in params:
            query_params.append(('pair', params['pair']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IGetOrdersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
