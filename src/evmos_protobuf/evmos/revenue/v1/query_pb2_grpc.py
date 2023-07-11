"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.revenue.v1 import query_pb2 as evmos_dot_revenue_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Revenues = channel.unary_unary('/evmos.revenue.v1.Query/Revenues', request_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesRequest.SerializeToString, response_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesResponse.FromString)
        self.Revenue = channel.unary_unary('/evmos.revenue.v1.Query/Revenue', request_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueRequest.SerializeToString, response_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueResponse.FromString)
        self.Params = channel.unary_unary('/evmos.revenue.v1.Query/Params', request_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.DeployerRevenues = channel.unary_unary('/evmos.revenue.v1.Query/DeployerRevenues', request_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesRequest.SerializeToString, response_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesResponse.FromString)
        self.WithdrawerRevenues = channel.unary_unary('/evmos.revenue.v1.Query/WithdrawerRevenues', request_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesRequest.SerializeToString, response_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Revenues(self, request, context):
        """Revenues retrieves all registered revenues
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Revenue(self, request, context):
        """Revenue retrieves a registered revenue for a given contract address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params retrieves the revenue module params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeployerRevenues(self, request, context):
        """DeployerRevenues retrieves all revenues that a given deployer has
        registered
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WithdrawerRevenues(self, request, context):
        """WithdrawerRevenues retrieves all revenues with a given withdrawer
        address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Revenues': grpc.unary_unary_rpc_method_handler(servicer.Revenues, request_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesRequest.FromString, response_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesResponse.SerializeToString), 'Revenue': grpc.unary_unary_rpc_method_handler(servicer.Revenue, request_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueRequest.FromString, response_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'DeployerRevenues': grpc.unary_unary_rpc_method_handler(servicer.DeployerRevenues, request_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesRequest.FromString, response_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesResponse.SerializeToString), 'WithdrawerRevenues': grpc.unary_unary_rpc_method_handler(servicer.WithdrawerRevenues, request_deserializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesRequest.FromString, response_serializer=evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.revenue.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Revenues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.revenue.v1.Query/Revenues', evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesRequest.SerializeToString, evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenuesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Revenue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.revenue.v1.Query/Revenue', evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueRequest.SerializeToString, evmos_dot_revenue_dot_v1_dot_query__pb2.QueryRevenueResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.revenue.v1.Query/Params', evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, evmos_dot_revenue_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeployerRevenues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.revenue.v1.Query/DeployerRevenues', evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesRequest.SerializeToString, evmos_dot_revenue_dot_v1_dot_query__pb2.QueryDeployerRevenuesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WithdrawerRevenues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.revenue.v1.Query/WithdrawerRevenues', evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesRequest.SerializeToString, evmos_dot_revenue_dot_v1_dot_query__pb2.QueryWithdrawerRevenuesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)