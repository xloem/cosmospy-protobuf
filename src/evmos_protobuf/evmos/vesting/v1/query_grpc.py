import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import cosmos
from .... import gogoproto
from .... import google
from .... import evmos

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Balances(self, stream: 'grpclib.server.Stream[evmos.vesting.v1.query_pb2.QueryBalancesRequest, evmos.vesting.v1.query_pb2.QueryBalancesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.vesting.v1.Query/Balances': grpclib.const.Handler(self.Balances, grpclib.const.Cardinality.UNARY_UNARY, evmos.vesting.v1.query_pb2.QueryBalancesRequest, evmos.vesting.v1.query_pb2.QueryBalancesResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Balances = grpclib.client.UnaryUnaryMethod(channel, '/evmos.vesting.v1.Query/Balances', evmos.vesting.v1.query_pb2.QueryBalancesRequest, evmos.vesting.v1.query_pb2.QueryBalancesResponse)