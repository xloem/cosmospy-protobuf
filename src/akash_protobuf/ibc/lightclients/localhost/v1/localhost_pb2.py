"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-ibc/lightclients/localhost/v1/localhost.proto\x12\x1dibc.lightclients.localhost.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto"l\n\x0bClientState\x12%\n\x08chain_id\x18\x01 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"chain_id"\x120\n\x06height\x18\x02 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00BFZDgithub.com/cosmos/ibc-go/v4/modules/light-clients/09-localhost/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.localhost.v1.localhost_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZDgithub.com/cosmos/ibc-go/v4/modules/light-clients/09-localhost/types'
    _CLIENTSTATE.fields_by_name['chain_id']._options = None
    _CLIENTSTATE.fields_by_name['chain_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"chain_id"'
    _CLIENTSTATE.fields_by_name['height']._options = None
    _CLIENTSTATE.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _CLIENTSTATE._options = None
    _CLIENTSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_CLIENTSTATE']._serialized_start = 135
    _globals['_CLIENTSTATE']._serialized_end = 243