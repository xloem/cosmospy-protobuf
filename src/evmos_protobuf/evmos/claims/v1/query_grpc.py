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
    async def TotalUnclaimed(self, stream: 'grpclib.server.Stream[evmos.claims.v1.query_pb2.QueryTotalUnclaimedRequest, evmos.claims.v1.query_pb2.QueryTotalUnclaimedResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[evmos.claims.v1.query_pb2.QueryParamsRequest, evmos.claims.v1.query_pb2.QueryParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClaimsRecords(self, stream: 'grpclib.server.Stream[evmos.claims.v1.query_pb2.QueryClaimsRecordsRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClaimsRecord(self, stream: 'grpclib.server.Stream[evmos.claims.v1.query_pb2.QueryClaimsRecordRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.claims.v1.Query/TotalUnclaimed': grpclib.const.Handler(self.TotalUnclaimed, grpclib.const.Cardinality.UNARY_UNARY, evmos.claims.v1.query_pb2.QueryTotalUnclaimedRequest, evmos.claims.v1.query_pb2.QueryTotalUnclaimedResponse), '/evmos.claims.v1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, evmos.claims.v1.query_pb2.QueryParamsRequest, evmos.claims.v1.query_pb2.QueryParamsResponse), '/evmos.claims.v1.Query/ClaimsRecords': grpclib.const.Handler(self.ClaimsRecords, grpclib.const.Cardinality.UNARY_UNARY, evmos.claims.v1.query_pb2.QueryClaimsRecordsRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordsResponse), '/evmos.claims.v1.Query/ClaimsRecord': grpclib.const.Handler(self.ClaimsRecord, grpclib.const.Cardinality.UNARY_UNARY, evmos.claims.v1.query_pb2.QueryClaimsRecordRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TotalUnclaimed = grpclib.client.UnaryUnaryMethod(channel, '/evmos.claims.v1.Query/TotalUnclaimed', evmos.claims.v1.query_pb2.QueryTotalUnclaimedRequest, evmos.claims.v1.query_pb2.QueryTotalUnclaimedResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/evmos.claims.v1.Query/Params', evmos.claims.v1.query_pb2.QueryParamsRequest, evmos.claims.v1.query_pb2.QueryParamsResponse)
        self.ClaimsRecords = grpclib.client.UnaryUnaryMethod(channel, '/evmos.claims.v1.Query/ClaimsRecords', evmos.claims.v1.query_pb2.QueryClaimsRecordsRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordsResponse)
        self.ClaimsRecord = grpclib.client.UnaryUnaryMethod(channel, '/evmos.claims.v1.Query/ClaimsRecord', evmos.claims.v1.query_pb2.QueryClaimsRecordRequest, evmos.claims.v1.query_pb2.QueryClaimsRecordResponse)