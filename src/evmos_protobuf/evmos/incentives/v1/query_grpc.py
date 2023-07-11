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
    async def Incentives(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryIncentivesRequest, evmos.incentives.v1.query_pb2.QueryIncentivesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Incentive(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryIncentiveRequest, evmos.incentives.v1.query_pb2.QueryIncentiveResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GasMeters(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryGasMetersRequest, evmos.incentives.v1.query_pb2.QueryGasMetersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GasMeter(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryGasMeterRequest, evmos.incentives.v1.query_pb2.QueryGasMeterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AllocationMeters(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryAllocationMetersRequest, evmos.incentives.v1.query_pb2.QueryAllocationMetersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AllocationMeter(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryAllocationMeterRequest, evmos.incentives.v1.query_pb2.QueryAllocationMeterResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[evmos.incentives.v1.query_pb2.QueryParamsRequest, evmos.incentives.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.incentives.v1.Query/Incentives': grpclib.const.Handler(self.Incentives, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryIncentivesRequest, evmos.incentives.v1.query_pb2.QueryIncentivesResponse), '/evmos.incentives.v1.Query/Incentive': grpclib.const.Handler(self.Incentive, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryIncentiveRequest, evmos.incentives.v1.query_pb2.QueryIncentiveResponse), '/evmos.incentives.v1.Query/GasMeters': grpclib.const.Handler(self.GasMeters, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryGasMetersRequest, evmos.incentives.v1.query_pb2.QueryGasMetersResponse), '/evmos.incentives.v1.Query/GasMeter': grpclib.const.Handler(self.GasMeter, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryGasMeterRequest, evmos.incentives.v1.query_pb2.QueryGasMeterResponse), '/evmos.incentives.v1.Query/AllocationMeters': grpclib.const.Handler(self.AllocationMeters, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryAllocationMetersRequest, evmos.incentives.v1.query_pb2.QueryAllocationMetersResponse), '/evmos.incentives.v1.Query/AllocationMeter': grpclib.const.Handler(self.AllocationMeter, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryAllocationMeterRequest, evmos.incentives.v1.query_pb2.QueryAllocationMeterResponse), '/evmos.incentives.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, evmos.incentives.v1.query_pb2.QueryParamsRequest, evmos.incentives.v1.query_pb2.QueryParamsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Incentives = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/Incentives', evmos.incentives.v1.query_pb2.QueryIncentivesRequest, evmos.incentives.v1.query_pb2.QueryIncentivesResponse)
        self.Incentive = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/Incentive', evmos.incentives.v1.query_pb2.QueryIncentiveRequest, evmos.incentives.v1.query_pb2.QueryIncentiveResponse)
        self.GasMeters = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/GasMeters', evmos.incentives.v1.query_pb2.QueryGasMetersRequest, evmos.incentives.v1.query_pb2.QueryGasMetersResponse)
        self.GasMeter = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/GasMeter', evmos.incentives.v1.query_pb2.QueryGasMeterRequest, evmos.incentives.v1.query_pb2.QueryGasMeterResponse)
        self.AllocationMeters = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/AllocationMeters', evmos.incentives.v1.query_pb2.QueryAllocationMetersRequest, evmos.incentives.v1.query_pb2.QueryAllocationMetersResponse)
        self.AllocationMeter = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/AllocationMeter', evmos.incentives.v1.query_pb2.QueryAllocationMeterRequest, evmos.incentives.v1.query_pb2.QueryAllocationMeterResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/evmos.incentives.v1.Query/Params', evmos.incentives.v1.query_pb2.QueryParamsRequest, evmos.incentives.v1.query_pb2.QueryParamsResponse)