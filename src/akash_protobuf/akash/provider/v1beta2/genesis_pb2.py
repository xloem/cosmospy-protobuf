"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.provider.v1beta2 import provider_pb2 as akash_dot_provider_dot_v1beta2_dot_provider__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/provider/v1beta2/genesis.proto\x12\x16akash.provider.v1beta2\x1a\x14gogoproto/gogo.proto\x1a%akash/provider/v1beta2/provider.proto"j\n\x0cGenesisState\x12Z\n\tproviders\x18\x01 \x03(\x0b2 .akash.provider.v1beta2.ProviderB%\xc8\xde\x1f\x00\xea\xde\x1f\tproviders\xf2\xde\x1f\x10yaml:"providers"B=Z;github.com/akash-network/akash-api/go/node/provider/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.provider.v1beta2.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/akash-network/akash-api/go/node/provider/v1beta2'
    _GENESISSTATE.fields_by_name['providers']._options = None
    _GENESISSTATE.fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tproviders\xf2\xde\x1f\x10yaml:"providers"'
    _globals['_GENESISSTATE']._serialized_start = 125
    _globals['_GENESISSTATE']._serialized_end = 231