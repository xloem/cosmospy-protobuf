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
    async def TokenPairs(self, stream: 'grpclib.server.Stream[evmos.erc20.v1.query_pb2.QueryTokenPairsRequest, evmos.erc20.v1.query_pb2.QueryTokenPairsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TokenPair(self, stream: 'grpclib.server.Stream[evmos.erc20.v1.query_pb2.QueryTokenPairRequest, evmos.erc20.v1.query_pb2.QueryTokenPairResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[evmos.erc20.v1.query_pb2.QueryParamsRequest, evmos.erc20.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.erc20.v1.Query/TokenPairs': grpclib.const.Handler(self.TokenPairs, grpclib.const.Cardinality.UNARY_UNARY, evmos.erc20.v1.query_pb2.QueryTokenPairsRequest, evmos.erc20.v1.query_pb2.QueryTokenPairsResponse), '/evmos.erc20.v1.Query/TokenPair': grpclib.const.Handler(self.TokenPair, grpclib.const.Cardinality.UNARY_UNARY, evmos.erc20.v1.query_pb2.QueryTokenPairRequest, evmos.erc20.v1.query_pb2.QueryTokenPairResponse), '/evmos.erc20.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, evmos.erc20.v1.query_pb2.QueryParamsRequest, evmos.erc20.v1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TokenPairs = grpclib.client.UnaryUnaryMethod(channel, '/evmos.erc20.v1.Query/TokenPairs', evmos.erc20.v1.query_pb2.QueryTokenPairsRequest, evmos.erc20.v1.query_pb2.QueryTokenPairsResponse)
        self.TokenPair = grpclib.client.UnaryUnaryMethod(channel, '/evmos.erc20.v1.Query/TokenPair', evmos.erc20.v1.query_pb2.QueryTokenPairRequest, evmos.erc20.v1.query_pb2.QueryTokenPairResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/evmos.erc20.v1.Query/Params', evmos.erc20.v1.query_pb2.QueryParamsRequest, evmos.erc20.v1.query_pb2.QueryParamsResponse)