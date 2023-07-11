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
    async def EpochInfos(self, stream: 'grpclib.server.Stream[evmos.epochs.v1.query_pb2.QueryEpochsInfoRequest, evmos.epochs.v1.query_pb2.QueryEpochsInfoResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CurrentEpoch(self, stream: 'grpclib.server.Stream[evmos.epochs.v1.query_pb2.QueryCurrentEpochRequest, evmos.epochs.v1.query_pb2.QueryCurrentEpochResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/evmos.epochs.v1.Query/EpochInfos': grpclib.const.Handler(self.EpochInfos, grpclib.const.Cardinality.UNARY_UNARY, evmos.epochs.v1.query_pb2.QueryEpochsInfoRequest, evmos.epochs.v1.query_pb2.QueryEpochsInfoResponse), '/evmos.epochs.v1.Query/CurrentEpoch': grpclib.const.Handler(self.CurrentEpoch, grpclib.const.Cardinality.UNARY_UNARY, evmos.epochs.v1.query_pb2.QueryCurrentEpochRequest, evmos.epochs.v1.query_pb2.QueryCurrentEpochResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.EpochInfos = grpclib.client.UnaryUnaryMethod(channel, '/evmos.epochs.v1.Query/EpochInfos', evmos.epochs.v1.query_pb2.QueryEpochsInfoRequest, evmos.epochs.v1.query_pb2.QueryEpochsInfoResponse)
        self.CurrentEpoch = grpclib.client.UnaryUnaryMethod(channel, '/evmos.epochs.v1.Query/CurrentEpoch', evmos.epochs.v1.query_pb2.QueryCurrentEpochRequest, evmos.epochs.v1.query_pb2.QueryCurrentEpochResponse)