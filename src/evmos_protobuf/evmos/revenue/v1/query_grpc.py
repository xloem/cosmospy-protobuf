import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import evmos
from .... import gogoproto
from .... import google

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Revenues(self, stream: 'grpclib.server.Stream[evmos.revenue.v1.query_pb2.QueryRevenuesRequest, evmos.revenue.v1.query_pb2.QueryRevenuesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Revenue(self, stream: 'grpclib.server.Stream[evmos.revenue.v1.query_pb2.QueryRevenueRequest, evmos.revenue.v1.query_pb2.QueryRevenueResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[evmos.revenue.v1.query_pb2.QueryParamsRequest, evmos.revenue.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeployerRevenues(self, stream: 'grpclib.server.Stream[evmos.revenue.v1.query_pb2.QueryDeployerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryDeployerRevenuesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def WithdrawerRevenues(self, stream: 'grpclib.server.Stream[evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.revenue.v1.Query/Revenues': grpclib.const.Handler(self.Revenues, grpclib.const.Cardinality.UNARY_UNARY, evmos.revenue.v1.query_pb2.QueryRevenuesRequest, evmos.revenue.v1.query_pb2.QueryRevenuesResponse), '/evmos.revenue.v1.Query/Revenue': grpclib.const.Handler(self.Revenue, grpclib.const.Cardinality.UNARY_UNARY, evmos.revenue.v1.query_pb2.QueryRevenueRequest, evmos.revenue.v1.query_pb2.QueryRevenueResponse), '/evmos.revenue.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, evmos.revenue.v1.query_pb2.QueryParamsRequest, evmos.revenue.v1.query_pb2.QueryParamsResponse), '/evmos.revenue.v1.Query/DeployerRevenues': grpclib.const.Handler(self.DeployerRevenues, grpclib.const.Cardinality.UNARY_UNARY, evmos.revenue.v1.query_pb2.QueryDeployerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryDeployerRevenuesResponse), '/evmos.revenue.v1.Query/WithdrawerRevenues': grpclib.const.Handler(self.WithdrawerRevenues, grpclib.const.Cardinality.UNARY_UNARY, evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Revenues = grpclib.client.UnaryUnaryMethod(channel, '/evmos.revenue.v1.Query/Revenues', evmos.revenue.v1.query_pb2.QueryRevenuesRequest, evmos.revenue.v1.query_pb2.QueryRevenuesResponse)
        self.Revenue = grpclib.client.UnaryUnaryMethod(channel, '/evmos.revenue.v1.Query/Revenue', evmos.revenue.v1.query_pb2.QueryRevenueRequest, evmos.revenue.v1.query_pb2.QueryRevenueResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/evmos.revenue.v1.Query/Params', evmos.revenue.v1.query_pb2.QueryParamsRequest, evmos.revenue.v1.query_pb2.QueryParamsResponse)
        self.DeployerRevenues = grpclib.client.UnaryUnaryMethod(channel, '/evmos.revenue.v1.Query/DeployerRevenues', evmos.revenue.v1.query_pb2.QueryDeployerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryDeployerRevenuesResponse)
        self.WithdrawerRevenues = grpclib.client.UnaryUnaryMethod(channel, '/evmos.revenue.v1.Query/WithdrawerRevenues', evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesRequest, evmos.revenue.v1.query_pb2.QueryWithdrawerRevenuesResponse)