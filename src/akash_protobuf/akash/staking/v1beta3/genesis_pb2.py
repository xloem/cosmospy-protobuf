"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.staking.v1beta3 import params_pb2 as akash_dot_staking_dot_v1beta3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#akash/staking/v1beta3/genesis.proto\x12\x15akash.staking.v1beta3\x1a\x14gogoproto/gogo.proto\x1a"akash/staking/v1beta3/params.proto"^\n\x0cGenesisState\x12N\n\x06params\x18\x01 \x01(\x0b2\x1d.akash.staking.v1beta3.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B<Z:github.com/akash-network/akash-api/go/node/staking/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.staking.v1beta3.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z:github.com/akash-network/akash-api/go/node/staking/v1beta3'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _globals['_GENESISSTATE']._serialized_start = 120
    _globals['_GENESISSTATE']._serialized_end = 214