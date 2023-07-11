"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.market.v1beta3 import order_pb2 as akash_dot_market_dot_v1beta3_dot_order__pb2
from ....akash.market.v1beta3 import lease_pb2 as akash_dot_market_dot_v1beta3_dot_lease__pb2
from ....akash.market.v1beta3 import bid_pb2 as akash_dot_market_dot_v1beta3_dot_bid__pb2
from ....akash.market.v1beta3 import params_pb2 as akash_dot_market_dot_v1beta3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/market/v1beta3/genesis.proto\x12\x14akash.market.v1beta3\x1a\x14gogoproto/gogo.proto\x1a akash/market/v1beta3/order.proto\x1a akash/market/v1beta3/lease.proto\x1a\x1eakash/market/v1beta3/bid.proto\x1a!akash/market/v1beta3/params.proto"\xbf\x02\n\x0cGenesisState\x12M\n\x06params\x18\x01 \x01(\x0b2\x1c.akash.market.v1beta3.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"\x12L\n\x06orders\x18\x02 \x03(\x0b2\x1b.akash.market.v1beta3.OrderB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06orders\xf2\xde\x1f\ryaml:"orders"\x12L\n\x06leases\x18\x03 \x03(\x0b2\x1b.akash.market.v1beta3.LeaseB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06leases\xf2\xde\x1f\ryaml:"leases"\x12D\n\x04bids\x18\x04 \x03(\x0b2\x19.akash.market.v1beta3.BidB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04bids\xf2\xde\x1f\x0byaml:"bids"B;Z9github.com/akash-network/akash-api/go/node/market/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.market.v1beta3.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/akash-network/akash-api/go/node/market/v1beta3'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _GENESISSTATE.fields_by_name['orders']._options = None
    _GENESISSTATE.fields_by_name['orders']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06orders\xf2\xde\x1f\ryaml:"orders"'
    _GENESISSTATE.fields_by_name['leases']._options = None
    _GENESISSTATE.fields_by_name['leases']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06leases\xf2\xde\x1f\ryaml:"leases"'
    _GENESISSTATE.fields_by_name['bids']._options = None
    _GENESISSTATE.fields_by_name['bids']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04bids\xf2\xde\x1f\x0byaml:"bids"'
    _globals['_GENESISSTATE']._serialized_start = 218
    _globals['_GENESISSTATE']._serialized_end = 537