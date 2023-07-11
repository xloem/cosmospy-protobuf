"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....ethermint.feemarket.v1 import feemarket_pb2 as ethermint_dot_feemarket_dot_v1_dot_feemarket__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"ethermint/feemarket/v1/query.proto\x12\x16ethermint.feemarket.v1\x1a&ethermint/feemarket/v1/feemarket.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto"\x14\n\x12QueryParamsRequest"K\n\x13QueryParamsResponse\x124\n\x06params\x18\x01 \x01(\x0b2\x1e.ethermint.feemarket.v1.ParamsB\x04\xc8\xde\x1f\x00"\x15\n\x13QueryBaseFeeRequest"T\n\x14QueryBaseFeeResponse\x12<\n\x08base_fee\x18\x01 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"\x16\n\x14QueryBlockGasRequest"$\n\x15QueryBlockGasResponse\x12\x0b\n\x03gas\x18\x01 \x01(\x032\xad\x03\n\x05Query\x12\x85\x01\n\x06Params\x12*.ethermint.feemarket.v1.QueryParamsRequest\x1a+.ethermint.feemarket.v1.QueryParamsResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/feemarket/v1/params\x12\x8a\x01\n\x07BaseFee\x12+.ethermint.feemarket.v1.QueryBaseFeeRequest\x1a,.ethermint.feemarket.v1.QueryBaseFeeResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/evmos/feemarket/v1/base_fee\x12\x8e\x01\n\x08BlockGas\x12,.ethermint.feemarket.v1.QueryBlockGasRequest\x1a-.ethermint.feemarket.v1.QueryBlockGasResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/evmos/feemarket/v1/block_gasB.Z,github.com/evmos/evmos/v13/x/feemarket/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.feemarket.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/evmos/evmos/v13/x/feemarket/types'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYBASEFEERESPONSE.fields_by_name['base_fee']._options = None
    _QUERYBASEFEERESPONSE.fields_by_name['base_fee']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/feemarket/v1/params'
    _QUERY.methods_by_name['BaseFee']._options = None
    _QUERY.methods_by_name['BaseFee']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/evmos/feemarket/v1/base_fee'
    _QUERY.methods_by_name['BlockGas']._options = None
    _QUERY.methods_by_name['BlockGas']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/evmos/feemarket/v1/block_gas'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 154
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 174
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 176
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 251
    _globals['_QUERYBASEFEEREQUEST']._serialized_start = 253
    _globals['_QUERYBASEFEEREQUEST']._serialized_end = 274
    _globals['_QUERYBASEFEERESPONSE']._serialized_start = 276
    _globals['_QUERYBASEFEERESPONSE']._serialized_end = 360
    _globals['_QUERYBLOCKGASREQUEST']._serialized_start = 362
    _globals['_QUERYBLOCKGASREQUEST']._serialized_end = 384
    _globals['_QUERYBLOCKGASRESPONSE']._serialized_start = 386
    _globals['_QUERYBLOCKGASRESPONSE']._serialized_end = 422
    _globals['_QUERY']._serialized_start = 425
    _globals['_QUERY']._serialized_end = 854