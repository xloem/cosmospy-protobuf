"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.feegrant.v1beta1 import feegrant_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/feegrant/v1beta1/genesis.proto\x12\x17cosmos.feegrant.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/feegrant/v1beta1/feegrant.proto"H\n\x0cGenesisState\x128\n\nallowances\x18\x01 \x03(\x0b2\x1e.cosmos.feegrant.v1beta1.GrantB\x04\xc8\xde\x1f\x00B)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z'github.com/cosmos/cosmos-sdk/x/feegrant"
    _GENESISSTATE.fields_by_name['allowances']._options = None
    _GENESISSTATE.fields_by_name['allowances']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 128
    _globals['_GENESISSTATE']._serialized_end = 200