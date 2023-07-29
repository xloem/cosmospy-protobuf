"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.client.v1 import genesis_pb2 as ibc_dot_core_dot_client_dot_v1_dot_genesis__pb2
from .....ibc.core.connection.v1 import genesis_pb2 as ibc_dot_core_dot_connection_dot_v1_dot_genesis__pb2
from .....ibc.core.channel.v1 import genesis_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_genesis__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/types/v1/genesis.proto\x12\x11ibc.core.types.v1\x1a\x14gogoproto/gogo.proto\x1a ibc/core/client/v1/genesis.proto\x1a$ibc/core/connection/v1/genesis.proto\x1a!ibc/core/channel/v1/genesis.proto"\xa8\x02\n\x0cGenesisState\x12W\n\x0eclient_genesis\x18\x01 \x01(\x0b2 .ibc.core.client.v1.GenesisStateB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"client_genesis"\x12c\n\x12connection_genesis\x18\x02 \x01(\x0b2$.ibc.core.connection.v1.GenesisStateB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"connection_genesis"\x12Z\n\x0fchannel_genesis\x18\x03 \x01(\x0b2!.ibc.core.channel.v1.GenesisStateB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"channel_genesis"B0Z.github.com/cosmos/ibc-go/v4/modules/core/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.types.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/cosmos/ibc-go/v4/modules/core/types'
    _GENESISSTATE.fields_by_name['client_genesis']._options = None
    _GENESISSTATE.fields_by_name['client_genesis']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"client_genesis"'
    _GENESISSTATE.fields_by_name['connection_genesis']._options = None
    _GENESISSTATE.fields_by_name['connection_genesis']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"connection_genesis"'
    _GENESISSTATE.fields_by_name['channel_genesis']._options = None
    _GENESISSTATE.fields_by_name['channel_genesis']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"channel_genesis"'
    _globals['_GENESISSTATE']._serialized_start = 184
    _globals['_GENESISSTATE']._serialized_end = 480