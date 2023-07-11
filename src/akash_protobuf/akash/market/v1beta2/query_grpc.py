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
    async def Orders(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryOrdersRequest, akash.market.v1beta2.query_pb2.QueryOrdersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Order(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryOrderRequest, akash.market.v1beta2.query_pb2.QueryOrderResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Bids(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryBidsRequest, akash.market.v1beta2.query_pb2.QueryBidsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Bid(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryBidRequest, akash.market.v1beta2.query_pb2.QueryBidResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Leases(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryLeasesRequest, akash.market.v1beta2.query_pb2.QueryLeasesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Lease(self, stream: 'grpclib.server.Stream[akash.market.v1beta2.query_pb2.QueryLeaseRequest, akash.market.v1beta2.query_pb2.QueryLeaseResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/akash.market.v1beta2.Query/Orders': grpclib.const.Handler(self.Orders, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryOrdersRequest, akash.market.v1beta2.query_pb2.QueryOrdersResponse), '/akash.market.v1beta2.Query/Order': grpclib.const.Handler(self.Order, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryOrderRequest, akash.market.v1beta2.query_pb2.QueryOrderResponse), '/akash.market.v1beta2.Query/Bids': grpclib.const.Handler(self.Bids, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryBidsRequest, akash.market.v1beta2.query_pb2.QueryBidsResponse), '/akash.market.v1beta2.Query/Bid': grpclib.const.Handler(self.Bid, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryBidRequest, akash.market.v1beta2.query_pb2.QueryBidResponse), '/akash.market.v1beta2.Query/Leases': grpclib.const.Handler(self.Leases, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryLeasesRequest, akash.market.v1beta2.query_pb2.QueryLeasesResponse), '/akash.market.v1beta2.Query/Lease': grpclib.const.Handler(self.Lease, grpclib.const.Cardinality.UNARY_UNARY, akash.market.v1beta2.query_pb2.QueryLeaseRequest, akash.market.v1beta2.query_pb2.QueryLeaseResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Orders = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Orders', akash.market.v1beta2.query_pb2.QueryOrdersRequest, akash.market.v1beta2.query_pb2.QueryOrdersResponse)
        self.Order = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Order', akash.market.v1beta2.query_pb2.QueryOrderRequest, akash.market.v1beta2.query_pb2.QueryOrderResponse)
        self.Bids = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Bids', akash.market.v1beta2.query_pb2.QueryBidsRequest, akash.market.v1beta2.query_pb2.QueryBidsResponse)
        self.Bid = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Bid', akash.market.v1beta2.query_pb2.QueryBidRequest, akash.market.v1beta2.query_pb2.QueryBidResponse)
        self.Leases = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Leases', akash.market.v1beta2.query_pb2.QueryLeasesRequest, akash.market.v1beta2.query_pb2.QueryLeasesResponse)
        self.Lease = grpclib.client.UnaryUnaryMethod(channel, '/akash.market.v1beta2.Query/Lease', akash.market.v1beta2.query_pb2.QueryLeaseRequest, akash.market.v1beta2.query_pb2.QueryLeaseResponse)