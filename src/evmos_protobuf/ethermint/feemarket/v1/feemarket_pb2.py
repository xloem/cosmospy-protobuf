"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&ethermint/feemarket/v1/feemarket.proto\x12\x16ethermint.feemarket.v1\x1a\x14gogoproto/gogo.proto"\xe5\x02\n\x06Params\x12\x13\n\x0bno_base_fee\x18\x01 \x01(\x08\x12#\n\x1bbase_fee_change_denominator\x18\x02 \x01(\r\x12\x1d\n\x15elasticity_multiplier\x18\x03 \x01(\r\x12\x15\n\renable_height\x18\x05 \x01(\x03\x12@\n\x08base_fee\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12E\n\rmin_gas_price\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12J\n\x12min_gas_multiplier\x18\x08 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.DecJ\x04\x08\x04\x10\x05R\x10initial_base_feeB.Z,github.com/evmos/evmos/v13/x/feemarket/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.feemarket.v1.feemarket_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/feemarket/types'
    _PARAMS.fields_by_name['base_fee']._options = None
    _PARAMS.fields_by_name['base_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _PARAMS.fields_by_name['min_gas_price']._options = None
    _PARAMS.fields_by_name['min_gas_price']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _PARAMS.fields_by_name['min_gas_multiplier']._options = None
    _PARAMS.fields_by_name['min_gas_multiplier']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_PARAMS']._serialized_start = 89
    _globals['_PARAMS']._serialized_end = 446