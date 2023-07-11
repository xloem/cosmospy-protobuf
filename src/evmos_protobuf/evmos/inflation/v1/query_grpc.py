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
    async def Period(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QueryPeriodRequest, evmos.inflation.v1.query_pb2.QueryPeriodResponse]') -> None:
        pass

    @abc.abstractmethod
    async def EpochMintProvision(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QueryEpochMintProvisionRequest, evmos.inflation.v1.query_pb2.QueryEpochMintProvisionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SkippedEpochs(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QuerySkippedEpochsRequest, evmos.inflation.v1.query_pb2.QuerySkippedEpochsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CirculatingSupply(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QueryCirculatingSupplyRequest, evmos.inflation.v1.query_pb2.QueryCirculatingSupplyResponse]') -> None:
        pass

    @abc.abstractmethod
    async def InflationRate(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QueryInflationRateRequest, evmos.inflation.v1.query_pb2.QueryInflationRateResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[evmos.inflation.v1.query_pb2.QueryParamsRequest, evmos.inflation.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.inflation.v1.Query/Period': grpclib.const.Handler(self.Period, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QueryPeriodRequest, evmos.inflation.v1.query_pb2.QueryPeriodResponse), '/evmos.inflation.v1.Query/EpochMintProvision': grpclib.const.Handler(self.EpochMintProvision, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QueryEpochMintProvisionRequest, evmos.inflation.v1.query_pb2.QueryEpochMintProvisionResponse), '/evmos.inflation.v1.Query/SkippedEpochs': grpclib.const.Handler(self.SkippedEpochs, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QuerySkippedEpochsRequest, evmos.inflation.v1.query_pb2.QuerySkippedEpochsResponse), '/evmos.inflation.v1.Query/CirculatingSupply': grpclib.const.Handler(self.CirculatingSupply, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QueryCirculatingSupplyRequest, evmos.inflation.v1.query_pb2.QueryCirculatingSupplyResponse), '/evmos.inflation.v1.Query/InflationRate': grpclib.const.Handler(self.InflationRate, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QueryInflationRateRequest, evmos.inflation.v1.query_pb2.QueryInflationRateResponse), '/evmos.inflation.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, evmos.inflation.v1.query_pb2.QueryParamsRequest, evmos.inflation.v1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Period = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/Period', evmos.inflation.v1.query_pb2.QueryPeriodRequest, evmos.inflation.v1.query_pb2.QueryPeriodResponse)
        self.EpochMintProvision = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/EpochMintProvision', evmos.inflation.v1.query_pb2.QueryEpochMintProvisionRequest, evmos.inflation.v1.query_pb2.QueryEpochMintProvisionResponse)
        self.SkippedEpochs = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/SkippedEpochs', evmos.inflation.v1.query_pb2.QuerySkippedEpochsRequest, evmos.inflation.v1.query_pb2.QuerySkippedEpochsResponse)
        self.CirculatingSupply = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/CirculatingSupply', evmos.inflation.v1.query_pb2.QueryCirculatingSupplyRequest, evmos.inflation.v1.query_pb2.QueryCirculatingSupplyResponse)
        self.InflationRate = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/InflationRate', evmos.inflation.v1.query_pb2.QueryInflationRateRequest, evmos.inflation.v1.query_pb2.QueryInflationRateResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/evmos.inflation.v1.Query/Params', evmos.inflation.v1.query_pb2.QueryParamsRequest, evmos.inflation.v1.query_pb2.QueryParamsResponse)