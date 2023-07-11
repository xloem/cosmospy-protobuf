from gogoproto import gogo_pb2 as _gogo_pb2
from google.api import annotations_pb2 as _annotations_pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as _pagination_pb2
from akash.market.v1beta3 import order_pb2 as _order_pb2
from akash.market.v1beta3 import bid_pb2 as _bid_pb2
from akash.market.v1beta3 import lease_pb2 as _lease_pb2
from akash.escrow.v1beta3 import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryOrdersRequest(_message.Message):
    __slots__ = ['filters', 'pagination']
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    filters: _order_pb2.OrderFilters
    pagination: _pagination_pb2.PageRequest

    def __init__(self, filters: _Optional[_Union[_order_pb2.OrderFilters, _Mapping]]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QueryOrdersResponse(_message.Message):
    __slots__ = ['orders', 'pagination']
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[_order_pb2.Order]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, orders: _Optional[_Iterable[_Union[_order_pb2.Order, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QueryOrderRequest(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _order_pb2.OrderID

    def __init__(self, id: _Optional[_Union[_order_pb2.OrderID, _Mapping]]=...) -> None:
        ...

class QueryOrderResponse(_message.Message):
    __slots__ = ['order']
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _order_pb2.Order

    def __init__(self, order: _Optional[_Union[_order_pb2.Order, _Mapping]]=...) -> None:
        ...

class QueryBidsRequest(_message.Message):
    __slots__ = ['filters', 'pagination']
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    filters: _bid_pb2.BidFilters
    pagination: _pagination_pb2.PageRequest

    def __init__(self, filters: _Optional[_Union[_bid_pb2.BidFilters, _Mapping]]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QueryBidsResponse(_message.Message):
    __slots__ = ['bids', 'pagination']
    BIDS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    bids: _containers.RepeatedCompositeFieldContainer[QueryBidResponse]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, bids: _Optional[_Iterable[_Union[QueryBidResponse, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QueryBidRequest(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _bid_pb2.BidID

    def __init__(self, id: _Optional[_Union[_bid_pb2.BidID, _Mapping]]=...) -> None:
        ...

class QueryBidResponse(_message.Message):
    __slots__ = ['bid', 'escrow_account']
    BID_FIELD_NUMBER: _ClassVar[int]
    ESCROW_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    bid: _bid_pb2.Bid
    escrow_account: _types_pb2.Account

    def __init__(self, bid: _Optional[_Union[_bid_pb2.Bid, _Mapping]]=..., escrow_account: _Optional[_Union[_types_pb2.Account, _Mapping]]=...) -> None:
        ...

class QueryLeasesRequest(_message.Message):
    __slots__ = ['filters', 'pagination']
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    filters: _lease_pb2.LeaseFilters
    pagination: _pagination_pb2.PageRequest

    def __init__(self, filters: _Optional[_Union[_lease_pb2.LeaseFilters, _Mapping]]=..., pagination: _Optional[_Union[_pagination_pb2.PageRequest, _Mapping]]=...) -> None:
        ...

class QueryLeasesResponse(_message.Message):
    __slots__ = ['leases', 'pagination']
    LEASES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    leases: _containers.RepeatedCompositeFieldContainer[QueryLeaseResponse]
    pagination: _pagination_pb2.PageResponse

    def __init__(self, leases: _Optional[_Iterable[_Union[QueryLeaseResponse, _Mapping]]]=..., pagination: _Optional[_Union[_pagination_pb2.PageResponse, _Mapping]]=...) -> None:
        ...

class QueryLeaseRequest(_message.Message):
    __slots__ = ['id']
    ID_FIELD_NUMBER: _ClassVar[int]
    id: _lease_pb2.LeaseID

    def __init__(self, id: _Optional[_Union[_lease_pb2.LeaseID, _Mapping]]=...) -> None:
        ...

class QueryLeaseResponse(_message.Message):
    __slots__ = ['lease', 'escrow_payment']
    LEASE_FIELD_NUMBER: _ClassVar[int]
    ESCROW_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    lease: _lease_pb2.Lease
    escrow_payment: _types_pb2.FractionalPayment

    def __init__(self, lease: _Optional[_Union[_lease_pb2.Lease, _Mapping]]=..., escrow_payment: _Optional[_Union[_types_pb2.FractionalPayment, _Mapping]]=...) -> None:
        ...