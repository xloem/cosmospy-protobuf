"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/authz/v1beta1/event.proto\x12\x14cosmos.authz.v1beta1"D\n\nEventGrant\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\t"E\n\x0bEventRevoke\x12\x14\n\x0cmsg_type_url\x18\x02 \x01(\t\x12\x0f\n\x07granter\x18\x03 \x01(\t\x12\x0f\n\x07grantee\x18\x04 \x01(\tB&Z$github.com/cosmos/cosmos-sdk/x/authzb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.authz.v1beta1.event_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/authz'
    _globals['_EVENTGRANT']._serialized_start = 58
    _globals['_EVENTGRANT']._serialized_end = 126
    _globals['_EVENTREVOKE']._serialized_start = 128
    _globals['_EVENTREVOKE']._serialized_end = 197