"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/crisis/v1beta1/genesis.proto\x12\x15cosmos.crisis.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\\\n\x0cGenesisState\x12L\n\x0cconstant_fee\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"constant_fee"B-Z+github.com/cosmos/cosmos-sdk/x/crisis/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.crisis.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z+github.com/cosmos/cosmos-sdk/x/crisis/types'
    _GENESISSTATE.fields_by_name['constant_fee']._options = None
    _GENESISSTATE.fields_by_name['constant_fee']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"constant_fee"'
    _globals['_GENESISSTATE']._serialized_start = 116
    _globals['_GENESISSTATE']._serialized_end = 208