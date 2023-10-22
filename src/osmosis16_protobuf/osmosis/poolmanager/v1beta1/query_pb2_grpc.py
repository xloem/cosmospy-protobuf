"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.poolmanager.v1beta1 import query_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/Params', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString)
        self.EstimateSwapExactAmountIn = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString)
        self.EstimateSinglePoolSwapExactAmountIn = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSinglePoolSwapExactAmountIn', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountInRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString)
        self.EstimateSwapExactAmountOut = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString)
        self.EstimateSinglePoolSwapExactAmountOut = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/EstimateSinglePoolSwapExactAmountOut', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountOutRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString)
        self.NumPools = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/NumPools', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.FromString)
        self.Pool = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/Pool', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolResponse.FromString)
        self.AllPools = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/AllPools', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsResponse.FromString)
        self.SpotPrice = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/SpotPrice', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceResponse.FromString)
        self.TotalPoolLiquidity = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/TotalPoolLiquidity', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityResponse.FromString)
        self.TotalLiquidity = channel.unary_unary('/osmosis.poolmanager.v1beta1.Query/TotalLiquidity', request_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountIn(self, request, context):
        """Estimates swap amount out given in.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSinglePoolSwapExactAmountIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSwapExactAmountOut(self, request, context):
        """Estimates swap amount in given out.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateSinglePoolSwapExactAmountOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NumPools(self, request, context):
        """Returns the total number of pools existing in Osmosis.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pool(self, request, context):
        """Pool returns the Pool specified by the pool id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllPools(self, request, context):
        """AllPools returns all pools on the Osmosis chain sorted by IDs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpotPrice(self, request, context):
        """SpotPrice defines a gRPC query handler that returns the spot price given
        a base denomination and a quote denomination.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalPoolLiquidity(self, request, context):
        """TotalPoolLiquidity returns the total liquidity of the specified pool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalLiquidity(self, request, context):
        """TotalLiquidity returns the total liquidity across all pools.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.SerializeToString), 'EstimateSwapExactAmountIn': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountIn, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.SerializeToString), 'EstimateSinglePoolSwapExactAmountIn': grpc.unary_unary_rpc_method_handler(servicer.EstimateSinglePoolSwapExactAmountIn, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountInRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.SerializeToString), 'EstimateSwapExactAmountOut': grpc.unary_unary_rpc_method_handler(servicer.EstimateSwapExactAmountOut, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.SerializeToString), 'EstimateSinglePoolSwapExactAmountOut': grpc.unary_unary_rpc_method_handler(servicer.EstimateSinglePoolSwapExactAmountOut, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountOutRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.SerializeToString), 'NumPools': grpc.unary_unary_rpc_method_handler(servicer.NumPools, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.SerializeToString), 'Pool': grpc.unary_unary_rpc_method_handler(servicer.Pool, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolResponse.SerializeToString), 'AllPools': grpc.unary_unary_rpc_method_handler(servicer.AllPools, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsResponse.SerializeToString), 'SpotPrice': grpc.unary_unary_rpc_method_handler(servicer.SpotPrice, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceResponse.SerializeToString), 'TotalPoolLiquidity': grpc.unary_unary_rpc_method_handler(servicer.TotalPoolLiquidity, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityResponse.SerializeToString), 'TotalLiquidity': grpc.unary_unary_rpc_method_handler(servicer.TotalLiquidity, request_deserializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.poolmanager.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/Params', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountIn(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSinglePoolSwapExactAmountIn(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSinglePoolSwapExactAmountIn', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountInRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountInResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSwapExactAmountOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateSinglePoolSwapExactAmountOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/EstimateSinglePoolSwapExactAmountOut', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSinglePoolSwapExactAmountOutRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.EstimateSwapExactAmountOutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NumPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/NumPools', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.NumPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/Pool', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.PoolResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/AllPools', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.AllPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpotPrice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/SpotPrice', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.SpotPriceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalPoolLiquidity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/TotalPoolLiquidity', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalPoolLiquidityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalLiquidity(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v1beta1.Query/TotalLiquidity', osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityRequest.SerializeToString, osmosis_dot_poolmanager_dot_v1beta1_dot_query__pb2.TotalLiquidityResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)