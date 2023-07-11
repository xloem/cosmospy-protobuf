"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/inflation/v1beta2/params.proto\x12\x17akash.inflation.v1beta2\x1a\x14gogoproto/gogo.proto"\xab\x03\n\x06Params\x12\xa2\x01\n\x16inflation_decay_factor\x18\x01 \x01(\tB\x81\x01\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x14InflationDecayFactor\xea\xde\x1f\x16inflation_decay_factor\xf2\xde\x1f\x1dyaml:"inflation_decay_factor"\x12\x8e\x01\n\x11initial_inflation\x18\x02 \x01(\tBs\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x10InitialInflation\xea\xde\x1f\x11initial_inflation\xf2\xde\x1f\x18yaml:"initial_inflation"\x12k\n\x08variance\x18\x03 \x01(\tBY\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x08Variance\xea\xde\x1f\x08variance\xf2\xde\x1f\x0fyaml:"variance"BDZBgithub.com/akash-network/akash-api/go/node/inflation/types/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.inflation.v1beta2.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZBgithub.com/akash-network/akash-api/go/node/inflation/types/v1beta2'
    _PARAMS.fields_by_name['inflation_decay_factor']._options = None
    _PARAMS.fields_by_name['inflation_decay_factor']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x14InflationDecayFactor\xea\xde\x1f\x16inflation_decay_factor\xf2\xde\x1f\x1dyaml:"inflation_decay_factor"'
    _PARAMS.fields_by_name['initial_inflation']._options = None
    _PARAMS.fields_by_name['initial_inflation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x10InitialInflation\xea\xde\x1f\x11initial_inflation\xf2\xde\x1f\x18yaml:"initial_inflation"'
    _PARAMS.fields_by_name['variance']._options = None
    _PARAMS.fields_by_name['variance']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x08Variance\xea\xde\x1f\x08variance\xf2\xde\x1f\x0fyaml:"variance"'
    _globals['_PARAMS']._serialized_start = 88
    _globals['_PARAMS']._serialized_end = 515