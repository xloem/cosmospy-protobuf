"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/base/kv/v1beta1/kv.proto\x12\x16cosmos.base.kv.v1beta1\x1a\x14gogoproto/gogo.proto":\n\x05Pairs\x121\n\x05pairs\x18\x01 \x03(\x0b2\x1c.cosmos.base.kv.v1beta1.PairB\x04\xc8\xde\x1f\x00""\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0cB\'Z%github.com/cosmos/cosmos-sdk/types/kvb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.kv.v1beta1.kv_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/kv'
    _PAIRS.fields_by_name['pairs']._options = None
    _PAIRS.fields_by_name['pairs']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PAIRS']._serialized_start = 81
    _globals['_PAIRS']._serialized_end = 139
    _globals['_PAIR']._serialized_start = 141
    _globals['_PAIR']._serialized_end = 175