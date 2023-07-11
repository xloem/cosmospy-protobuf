import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
from .... import cosmos
from .... import akash

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Accounts(self, stream: 'grpclib.server.Stream[akash.escrow.v1beta2.query_pb2.QueryAccountsRequest, akash.escrow.v1beta2.query_pb2.QueryAccountsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Payments(self, stream: 'grpclib.server.Stream[akash.escrow.v1beta2.query_pb2.QueryPaymentsRequest, akash.escrow.v1beta2.query_pb2.QueryPaymentsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.escrow.v1beta2.Query/Accounts': grpclib.const.Handler(self.Accounts, grpclib.const.Cardinality.UNARY_UNARY, akash.escrow.v1beta2.query_pb2.QueryAccountsRequest, akash.escrow.v1beta2.query_pb2.QueryAccountsResponse), '/akash.escrow.v1beta2.Query/Payments': grpclib.const.Handler(self.Payments, grpclib.const.Cardinality.UNARY_UNARY, akash.escrow.v1beta2.query_pb2.QueryPaymentsRequest, akash.escrow.v1beta2.query_pb2.QueryPaymentsResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Accounts = grpclib.client.UnaryUnaryMethod(channel, '/akash.escrow.v1beta2.Query/Accounts', akash.escrow.v1beta2.query_pb2.QueryAccountsRequest, akash.escrow.v1beta2.query_pb2.QueryAccountsResponse)
        self.Payments = grpclib.client.UnaryUnaryMethod(channel, '/akash.escrow.v1beta2.Query/Payments', akash.escrow.v1beta2.query_pb2.QueryPaymentsRequest, akash.escrow.v1beta2.query_pb2.QueryPaymentsResponse)