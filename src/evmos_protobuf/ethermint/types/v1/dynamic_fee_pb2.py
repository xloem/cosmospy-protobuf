"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$ethermint/types/v1/dynamic_fee.proto\x12\x12ethermint.types.v1\x1a\x14gogoproto/gogo.proto"i\n\x1bExtensionOptionDynamicFeeTx\x12J\n\x12max_priority_price\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntB"Z github.com/evmos/evmos/v13/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.types.v1.dynamic_fee_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z github.com/evmos/evmos/v13/types'
    _EXTENSIONOPTIONDYNAMICFEETX.fields_by_name['max_priority_price']._options = None
    _EXTENSIONOPTIONDYNAMICFEETX.fields_by_name['max_priority_price']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _globals['_EXTENSIONOPTIONDYNAMICFEETX']._serialized_start = 82
    _globals['_EXTENSIONOPTIONDYNAMICFEETX']._serialized_end = 187