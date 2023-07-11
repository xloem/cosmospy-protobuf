"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.erc20.v1 import query_pb2 as evmos_dot_erc20_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TokenPairs = channel.unary_unary('/evmos.erc20.v1.Query/TokenPairs', request_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.SerializeToString, response_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.FromString)
        self.TokenPair = channel.unary_unary('/evmos.erc20.v1.Query/TokenPair', request_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.SerializeToString, response_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.FromString)
        self.Params = channel.unary_unary('/evmos.erc20.v1.Query/Params', request_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def TokenPairs(self, request, context):
        """TokenPairs retrieves registered token pairs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenPair(self, request, context):
        """TokenPair retrieves a registered token pair
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params retrieves the erc20 module params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'TokenPairs': grpc.unary_unary_rpc_method_handler(servicer.TokenPairs, request_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.FromString, response_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.SerializeToString), 'TokenPair': grpc.unary_unary_rpc_method_handler(servicer.TokenPair, request_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.FromString, response_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.erc20.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def TokenPairs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.erc20.v1.Query/TokenPairs', evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsRequest.SerializeToString, evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenPair(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.erc20.v1.Query/TokenPair', evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairRequest.SerializeToString, evmos_dot_erc20_dot_v1_dot_query__pb2.QueryTokenPairResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.erc20.v1.Query/Params', evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, evmos_dot_erc20_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)