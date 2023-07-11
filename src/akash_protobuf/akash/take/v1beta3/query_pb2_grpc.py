"""Client and server classes corresponding to protobuf-defined services."""
import grpc

class QueryStub(object):
    """Query defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """

class QueryServicer(object):
    """Query defines the gRPC querier service
    """

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {}
    generic_handler = grpc.method_handlers_generic_handler('akash.take.v1beta3.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service
    """