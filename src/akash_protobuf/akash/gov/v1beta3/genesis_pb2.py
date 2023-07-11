"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.gov.v1beta3 import params_pb2 as akash_dot_gov_dot_v1beta3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fakash/gov/v1beta3/genesis.proto\x12\x11akash.gov.v1beta3\x1a\x14gogoproto/gogo.proto\x1a\x1eakash/gov/v1beta3/params.proto"y\n\x0cGenesisState\x12i\n\x0edeposit_params\x18\x01 \x01(\x0b2 .akash.gov.v1beta3.DepositParamsB/\xc8\xde\x1f\x00\xea\xde\x1f\x0edeposit_params\xf2\xde\x1f\x15yaml:"deposit_params"B8Z6github.com/akash-network/akash-api/go/node/gov/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.gov.v1beta3.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/node/gov/v1beta3'
    _GENESISSTATE.fields_by_name['deposit_params']._options = None
    _GENESISSTATE.fields_by_name['deposit_params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0edeposit_params\xf2\xde\x1f\x15yaml:"deposit_params"'
    _globals['_GENESISSTATE']._serialized_start = 108
    _globals['_GENESISSTATE']._serialized_end = 229