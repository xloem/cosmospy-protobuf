"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fakash/take/v1beta3/params.proto\x12\x12akash.take.v1beta3\x1a\x14gogoproto/gogo.proto"\xb2\x02\n\x06Params\x12\x8f\x01\n\x10denom_take_rates\x18\x01 \x03(\x0b2..akash.take.v1beta3.Params.DenomTakeRatesEntryBE\xc8\xde\x1f\x00\xe2\xde\x1f\x0eDenomTakeRates\xea\xde\x1f\x10denom_take_rates\xf2\xde\x1f\x17yaml:"denom_take_rates"\x12_\n\x11default_take_rate\x18\x02 \x01(\rBD\xe2\xde\x1f\x0fDefaultTakeRate\xea\xde\x1f\x11default_take_rate\xf2\xde\x1f\x18yaml:"default_take_rate"\x1a5\n\x13DenomTakeRatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x028\x01B9Z7github.com/akash-network/akash-api/go/node/take/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.take.v1beta3.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/akash-network/akash-api/go/node/take/v1beta3'
    _PARAMS_DENOMTAKERATESENTRY._options = None
    _PARAMS_DENOMTAKERATESENTRY._serialized_options = b'8\x01'
    _PARAMS.fields_by_name['denom_take_rates']._options = None
    _PARAMS.fields_by_name['denom_take_rates']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0eDenomTakeRates\xea\xde\x1f\x10denom_take_rates\xf2\xde\x1f\x17yaml:"denom_take_rates"'
    _PARAMS.fields_by_name['default_take_rate']._options = None
    _PARAMS.fields_by_name['default_take_rate']._serialized_options = b'\xe2\xde\x1f\x0fDefaultTakeRate\xea\xde\x1f\x11default_take_rate\xf2\xde\x1f\x18yaml:"default_take_rate"'
    _globals['_PARAMS']._serialized_start = 78
    _globals['_PARAMS']._serialized_end = 384
    _globals['_PARAMS_DENOMTAKERATESENTRY']._serialized_start = 331
    _globals['_PARAMS_DENOMTAKERATESENTRY']._serialized_end = 384