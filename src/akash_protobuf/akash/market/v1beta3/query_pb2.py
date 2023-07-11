"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.market.v1beta3 import order_pb2 as akash_dot_market_dot_v1beta3_dot_order__pb2
from ....akash.market.v1beta3 import bid_pb2 as akash_dot_market_dot_v1beta3_dot_bid__pb2
from ....akash.market.v1beta3 import lease_pb2 as akash_dot_market_dot_v1beta3_dot_lease__pb2
from ....akash.escrow.v1beta3 import types_pb2 as akash_dot_escrow_dot_v1beta3_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/market/v1beta3/query.proto\x12\x14akash.market.v1beta3\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a akash/market/v1beta3/order.proto\x1a\x1eakash/market/v1beta3/bid.proto\x1a akash/market/v1beta3/lease.proto\x1a akash/escrow/v1beta3/types.proto"\x8b\x01\n\x12QueryOrdersRequest\x129\n\x07filters\x18\x01 \x01(\x0b2".akash.market.v1beta3.OrderFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8f\x01\n\x13QueryOrdersResponse\x12;\n\x06orders\x18\x01 \x03(\x0b2\x1b.akash.market.v1beta3.OrderB\x0e\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Orders\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"J\n\x11QueryOrderRequest\x125\n\x02id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta3.OrderIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"F\n\x12QueryOrderResponse\x120\n\x05order\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta3.OrderB\x04\xc8\xde\x1f\x00"\x87\x01\n\x10QueryBidsRequest\x127\n\x07filters\x18\x01 \x01(\x0b2 .akash.market.v1beta3.BidFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8c\x01\n\x11QueryBidsResponse\x12:\n\x04bids\x18\x01 \x03(\x0b2&.akash.market.v1beta3.QueryBidResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"F\n\x0fQueryBidRequest\x123\n\x02id\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta3.BidIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"}\n\x10QueryBidResponse\x12,\n\x03bid\x18\x01 \x01(\x0b2\x19.akash.market.v1beta3.BidB\x04\xc8\xde\x1f\x00\x12;\n\x0eescrow_account\x18\x02 \x01(\x0b2\x1d.akash.escrow.v1beta3.AccountB\x04\xc8\xde\x1f\x00"\x8b\x01\n\x12QueryLeasesRequest\x129\n\x07filters\x18\x01 \x01(\x0b2".akash.market.v1beta3.LeaseFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x92\x01\n\x13QueryLeasesResponse\x12>\n\x06leases\x18\x01 \x03(\x0b2(.akash.market.v1beta3.QueryLeaseResponseB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"J\n\x11QueryLeaseRequest\x125\n\x02id\x18\x01 \x01(\x0b2\x1d.akash.market.v1beta3.LeaseIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"\x8d\x01\n\x12QueryLeaseResponse\x120\n\x05lease\x18\x01 \x01(\x0b2\x1b.akash.market.v1beta3.LeaseB\x04\xc8\xde\x1f\x00\x12E\n\x0eescrow_payment\x18\x02 \x01(\x0b2\'.akash.escrow.v1beta3.FractionalPaymentB\x04\xc8\xde\x1f\x002\xaf\x06\n\x05Query\x12\x88\x01\n\x06Orders\x12(.akash.market.v1beta3.QueryOrdersRequest\x1a).akash.market.v1beta3.QueryOrdersResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/orders/list\x12\x85\x01\n\x05Order\x12\'.akash.market.v1beta3.QueryOrderRequest\x1a(.akash.market.v1beta3.QueryOrderResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/orders/info\x12\x80\x01\n\x04Bids\x12&.akash.market.v1beta3.QueryBidsRequest\x1a\'.akash.market.v1beta3.QueryBidsResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta3/bids/list\x12}\n\x03Bid\x12%.akash.market.v1beta3.QueryBidRequest\x1a&.akash.market.v1beta3.QueryBidResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta3/bids/info\x12\x88\x01\n\x06Leases\x12(.akash.market.v1beta3.QueryLeasesRequest\x1a).akash.market.v1beta3.QueryLeasesResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/leases/list\x12\x85\x01\n\x05Lease\x12\'.akash.market.v1beta3.QueryLeaseRequest\x1a(.akash.market.v1beta3.QueryLeaseResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/leases/infoB;Z9github.com/akash-network/akash-api/go/node/market/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.market.v1beta3.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/akash-network/akash-api/go/node/market/v1beta3'
    _QUERYORDERSREQUEST.fields_by_name['filters']._options = None
    _QUERYORDERSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYORDERSRESPONSE.fields_by_name['orders']._options = None
    _QUERYORDERSRESPONSE.fields_by_name['orders']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x06Orders'
    _QUERYORDERREQUEST.fields_by_name['id']._options = None
    _QUERYORDERREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYORDERRESPONSE.fields_by_name['order']._options = None
    _QUERYORDERRESPONSE.fields_by_name['order']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDSREQUEST.fields_by_name['filters']._options = None
    _QUERYBIDSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDSRESPONSE.fields_by_name['bids']._options = None
    _QUERYBIDSRESPONSE.fields_by_name['bids']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDREQUEST.fields_by_name['id']._options = None
    _QUERYBIDREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYBIDRESPONSE.fields_by_name['bid']._options = None
    _QUERYBIDRESPONSE.fields_by_name['bid']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBIDRESPONSE.fields_by_name['escrow_account']._options = None
    _QUERYBIDRESPONSE.fields_by_name['escrow_account']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASESREQUEST.fields_by_name['filters']._options = None
    _QUERYLEASESREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASESRESPONSE.fields_by_name['leases']._options = None
    _QUERYLEASESRESPONSE.fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASEREQUEST.fields_by_name['id']._options = None
    _QUERYLEASEREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYLEASERESPONSE.fields_by_name['lease']._options = None
    _QUERYLEASERESPONSE.fields_by_name['lease']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYLEASERESPONSE.fields_by_name['escrow_payment']._options = None
    _QUERYLEASERESPONSE.fields_by_name['escrow_payment']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Orders']._options = None
    _QUERY.methods_by_name['Orders']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/orders/list'
    _QUERY.methods_by_name['Order']._options = None
    _QUERY.methods_by_name['Order']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/orders/info'
    _QUERY.methods_by_name['Bids']._options = None
    _QUERY.methods_by_name['Bids']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta3/bids/list'
    _QUERY.methods_by_name['Bid']._options = None
    _QUERY.methods_by_name['Bid']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/akash/market/v1beta3/bids/info'
    _QUERY.methods_by_name['Leases']._options = None
    _QUERY.methods_by_name['Leases']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/leases/list'
    _QUERY.methods_by_name['Lease']._options = None
    _QUERY.methods_by_name['Lease']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/market/v1beta3/leases/info'
    _globals['_QUERYORDERSREQUEST']._serialized_start = 289
    _globals['_QUERYORDERSREQUEST']._serialized_end = 428
    _globals['_QUERYORDERSRESPONSE']._serialized_start = 431
    _globals['_QUERYORDERSRESPONSE']._serialized_end = 574
    _globals['_QUERYORDERREQUEST']._serialized_start = 576
    _globals['_QUERYORDERREQUEST']._serialized_end = 650
    _globals['_QUERYORDERRESPONSE']._serialized_start = 652
    _globals['_QUERYORDERRESPONSE']._serialized_end = 722
    _globals['_QUERYBIDSREQUEST']._serialized_start = 725
    _globals['_QUERYBIDSREQUEST']._serialized_end = 860
    _globals['_QUERYBIDSRESPONSE']._serialized_start = 863
    _globals['_QUERYBIDSRESPONSE']._serialized_end = 1003
    _globals['_QUERYBIDREQUEST']._serialized_start = 1005
    _globals['_QUERYBIDREQUEST']._serialized_end = 1075
    _globals['_QUERYBIDRESPONSE']._serialized_start = 1077
    _globals['_QUERYBIDRESPONSE']._serialized_end = 1202
    _globals['_QUERYLEASESREQUEST']._serialized_start = 1205
    _globals['_QUERYLEASESREQUEST']._serialized_end = 1344
    _globals['_QUERYLEASESRESPONSE']._serialized_start = 1347
    _globals['_QUERYLEASESRESPONSE']._serialized_end = 1493
    _globals['_QUERYLEASEREQUEST']._serialized_start = 1495
    _globals['_QUERYLEASEREQUEST']._serialized_end = 1569
    _globals['_QUERYLEASERESPONSE']._serialized_start = 1572
    _globals['_QUERYLEASERESPONSE']._serialized_end = 1713
    _globals['_QUERY']._serialized_start = 1716
    _globals['_QUERY']._serialized_end = 2531