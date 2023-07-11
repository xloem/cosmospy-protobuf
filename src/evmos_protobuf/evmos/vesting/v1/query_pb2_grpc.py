"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.vesting.v1 import query_pb2 as evmos_dot_vesting_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Balances = channel.unary_unary('/evmos.vesting.v1.Query/Balances', request_serializer=evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesRequest.SerializeToString, response_deserializer=evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Balances(self, request, context):
        """Balances retrieves the unvested, vested and locked tokens for a vesting account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Balances': grpc.unary_unary_rpc_method_handler(servicer.Balances, request_deserializer=evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesRequest.FromString, response_serializer=evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.vesting.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Balances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.vesting.v1.Query/Balances', evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesRequest.SerializeToString, evmos_dot_vesting_dot_v1_dot_query__pb2.QueryBalancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)