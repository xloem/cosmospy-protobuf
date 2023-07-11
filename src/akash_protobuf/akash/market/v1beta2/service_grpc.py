import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import akash

class MsgBase(abc.ABC):

    @abc.abstractmethod
    async def CreateBid(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.bid_pb2.MsgCreateBid, akash.market.v1beta2.bid_pb2.MsgCreateBidResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CloseBid(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.bid_pb2.MsgCloseBid, akash.market.v1beta2.bid_pb2.MsgCloseBidResponse]') -> None:
        pass

    @abc.abstractmethod
    async def WithdrawLease(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.lease_pb2.MsgWithdrawLease, akash.market.v1beta2.lease_pb2.MsgWithdrawLeaseResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateLease(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.lease_pb2.MsgCreateLease, akash.market.v1beta2.lease_pb2.MsgCreateLeaseResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CloseLease(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.lease_pb2.MsgCloseLease, akash.market.v1beta2.lease_pb2.MsgCloseLeaseResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.market.v1beta2.Msg/CreateBid': grpclib.const.Handler(self.CreateBid, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.bid_pb2.MsgCreateBid, akash.market.v1beta2.bid_pb2.MsgCreateBidResponse), '/akash.market.v1beta2.Msg/CloseBid': grpclib.const.Handler(self.CloseBid, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.bid_pb2.MsgCloseBid, akash.market.v1beta2.bid_pb2.MsgCloseBidResponse), '/akash.market.v1beta2.Msg/WithdrawLease': grpclib.const.Handler(self.WithdrawLease, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.lease_pb2.MsgWithdrawLease, akash.market.v1beta2.lease_pb2.MsgWithdrawLeaseResponse), '/akash.market.v1beta2.Msg/CreateLease': grpclib.const.Handler(self.CreateLease, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.lease_pb2.MsgCreateLease, akash.market.v1beta2.lease_pb2.MsgCreateLeaseResponse), '/akash.market.v1beta2.Msg/CloseLease': grpclib.const.Handler(self.CloseLease, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.lease_pb2.MsgCloseLease, akash.market.v1beta2.lease_pb2.MsgCloseLeaseResponse)}

class MsgStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateBid = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Msg/CreateBid', akash.market.v1beta2.bid_pb2.MsgCreateBid, akash.market.v1beta2.bid_pb2.MsgCreateBidResponse)
        self.CloseBid = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Msg/CloseBid', akash.market.v1beta2.bid_pb2.MsgCloseBid, akash.market.v1beta2.bid_pb2.MsgCloseBidResponse)
        self.WithdrawLease = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Msg/WithdrawLease', akash.market.v1beta2.lease_pb2.MsgWithdrawLease, akash.market.v1beta2.lease_pb2.MsgWithdrawLeaseResponse)
        self.CreateLease = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Msg/CreateLease', akash.market.v1beta2.lease_pb2.MsgCreateLease, akash.market.v1beta2.lease_pb2.MsgCreateLeaseResponse)
        self.CloseLease = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Msg/CloseLease', akash.market.v1beta2.lease_pb2.MsgCloseLease, akash.market.v1beta2.lease_pb2.MsgCloseLeaseResponse)