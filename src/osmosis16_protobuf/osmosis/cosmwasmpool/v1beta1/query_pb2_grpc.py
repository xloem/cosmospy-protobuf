"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.cosmwasmpool.v1beta1 import query_pb2 as osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Pools = channel.unary_unary('/osmosis.cosmwasmpool.v1beta1.Query/Pools', request_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsRequest.SerializeToString, response_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsResponse.FromString)
        self.Params = channel.unary_unary('/osmosis.cosmwasmpool.v1beta1.Query/Params', request_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, response_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString)
        self.ContractInfoByPoolId = channel.unary_unary('/osmosis.cosmwasmpool.v1beta1.Query/ContractInfoByPoolId', request_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdRequest.SerializeToString, response_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Pools(self, request, context):
        """Pools returns all cosmwasm pools
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params returns the parameters of the x/cosmwasmpool module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractInfoByPoolId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Pools': grpc.unary_unary_rpc_method_handler(servicer.Pools, request_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsRequest.FromString, response_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsRequest.FromString, response_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsResponse.SerializeToString), 'ContractInfoByPoolId': grpc.unary_unary_rpc_method_handler(servicer.ContractInfoByPoolId, request_deserializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdRequest.FromString, response_serializer=osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.cosmwasmpool.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Pools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.cosmwasmpool.v1beta1.Query/Pools', osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsRequest.SerializeToString, osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.PoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.cosmwasmpool.v1beta1.Query/Params', osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsRequest.SerializeToString, osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContractInfoByPoolId(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.cosmwasmpool.v1beta1.Query/ContractInfoByPoolId', osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdRequest.SerializeToString, osmosis_dot_cosmwasmpool_dot_v1beta1_dot_query__pb2.ContractInfoByPoolIdResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)