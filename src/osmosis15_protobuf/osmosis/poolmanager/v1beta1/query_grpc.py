import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import osmosis
from .... import cosmos
from .... import google
import google.protobuf.any_pb2
from .... import cosmos_proto
import google.protobuf.timestamp_pb2

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[osmosis.poolmanager.v1beta1.query_pb2.ParamsRequest, osmosis.poolmanager.v1beta1.query_pb2.ParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EstimateSwapExactAmountIn(self, stream: 'grpclib.server.Stream[osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EstimateSwapExactAmountOut(self, stream: 'grpclib.server.Stream[osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NumPools(self, stream: 'grpclib.server.Stream[osmosis.poolmanager.v1beta1.query_pb2.NumPoolsRequest, osmosis.poolmanager.v1beta1.query_pb2.NumPoolsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/osmosis.poolmanager.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, osmosis.poolmanager.v1beta1.query_pb2.ParamsRequest, osmosis.poolmanager.v1beta1.query_pb2.ParamsResponse), '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn': grpclib.const.Handler(self.EstimateSwapExactAmountIn, grpclib.const.Cardinality.UNARY_UNARY, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInResponse), '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut': grpclib.const.Handler(self.EstimateSwapExactAmountOut, grpclib.const.Cardinality.UNARY_UNARY, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutResponse), '/osmosis.poolmanager.v1beta1.Query/NumPools': grpclib.const.Handler(self.NumPools, grpclib.const.Cardinality.UNARY_UNARY, osmosis.poolmanager.v1beta1.query_pb2.NumPoolsRequest, osmosis.poolmanager.v1beta1.query_pb2.NumPoolsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.poolmanager.v1beta1.Query/Params', osmosis.poolmanager.v1beta1.query_pb2.ParamsRequest, osmosis.poolmanager.v1beta1.query_pb2.ParamsResponse)
        self.EstimateSwapExactAmountIn = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountIn', osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountInResponse)
        self.EstimateSwapExactAmountOut = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.poolmanager.v1beta1.Query/EstimateSwapExactAmountOut', osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutRequest, osmosis.poolmanager.v1beta1.query_pb2.EstimateSwapExactAmountOutResponse)
        self.NumPools = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.poolmanager.v1beta1.Query/NumPools', osmosis.poolmanager.v1beta1.query_pb2.NumPoolsRequest, osmosis.poolmanager.v1beta1.query_pb2.NumPoolsResponse)