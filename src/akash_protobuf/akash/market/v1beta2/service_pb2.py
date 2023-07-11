"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....akash.market.v1beta2 import bid_pb2 as akash_dot_market_dot_v1beta2_dot_bid__pb2
from ....akash.market.v1beta2 import lease_pb2 as akash_dot_market_dot_v1beta2_dot_lease__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/market/v1beta2/service.proto\x12\x14akash.market.v1beta2\x1a\x1eakash/market/v1beta2/bid.proto\x1a akash/market/v1beta2/lease.proto2\xe8\x03\n\x03Msg\x12[\n\tCreateBid\x12".akash.market.v1beta2.MsgCreateBid\x1a*.akash.market.v1beta2.MsgCreateBidResponse\x12X\n\x08CloseBid\x12!.akash.market.v1beta2.MsgCloseBid\x1a).akash.market.v1beta2.MsgCloseBidResponse\x12g\n\rWithdrawLease\x12&.akash.market.v1beta2.MsgWithdrawLease\x1a..akash.market.v1beta2.MsgWithdrawLeaseResponse\x12a\n\x0bCreateLease\x12$.akash.market.v1beta2.MsgCreateLease\x1a,.akash.market.v1beta2.MsgCreateLeaseResponse\x12^\n\nCloseLease\x12#.akash.market.v1beta2.MsgCloseLease\x1a+.akash.market.v1beta2.MsgCloseLeaseResponseB;Z9github.com/akash-network/akash-api/go/node/market/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.market.v1beta2.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/akash-network/akash-api/go/node/market/v1beta2'
    _globals['_MSG']._serialized_start = 127
    _globals['_MSG']._serialized_end = 615