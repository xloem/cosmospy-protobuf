"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.capability.v1beta1 import capability_pb2 as cosmos_dot_capability_dot_v1beta1_dot_capability__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/capability/v1beta1/genesis.proto\x12\x19cosmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/capability/v1beta1/capability.proto"~\n\rGenesisOwners\x12\r\n\x05index\x18\x01 \x01(\x04\x12^\n\x0cindex_owners\x18\x02 \x01(\x0b2+.cosmos.capability.v1beta1.CapabilityOwnersB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"index_owners""]\n\x0cGenesisState\x12\r\n\x05index\x18\x01 \x01(\x04\x12>\n\x06owners\x18\x02 \x03(\x0b2(.cosmos.capability.v1beta1.GenesisOwnersB\x04\xc8\xde\x1f\x00B1Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.capability.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/cosmos/cosmos-sdk/x/capability/types'
    _GENESISOWNERS.fields_by_name['index_owners']._options = None
    _GENESISOWNERS.fields_by_name['index_owners']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"index_owners"'
    _GENESISSTATE.fields_by_name['owners']._options = None
    _GENESISSTATE.fields_by_name['owners']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISOWNERS']._serialized_start = 136
    _globals['_GENESISOWNERS']._serialized_end = 262
    _globals['_GENESISSTATE']._serialized_start = 264
    _globals['_GENESISSTATE']._serialized_end = 357