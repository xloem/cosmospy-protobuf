"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......ibc.applications.interchain_accounts.controller.v1 import controller_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_controller_dot_v1_dot_controller__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>ibc/applications/interchain_accounts/controller/v1/query.proto\x122ibc.applications.interchain_accounts.controller.v1\x1aCibc/applications/interchain_accounts/controller/v1/controller.proto\x1a\x1cgoogle/api/annotations.proto"\x14\n\x12QueryParamsRequest"a\n\x13QueryParamsResponse\x12J\n\x06params\x18\x01 \x01(\x0b2:.ibc.applications.interchain_accounts.controller.v1.Params2\xdf\x01\n\x05Query\x12\xd5\x01\n\x06Params\x12F.ibc.applications.interchain_accounts.controller.v1.QueryParamsRequest\x1aG.ibc.applications.interchain_accounts.controller.v1.QueryParamsResponse":\x82\xd3\xe4\x93\x024\x122/ibc/apps/interchain_accounts/controller/v1/paramsBRZPgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.controller.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZPgithub.com/cosmos/ibc-go/v3/modules/apps/27-interchain-accounts/controller/types'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/ibc/apps/interchain_accounts/controller/v1/params'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 217
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 237
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 239
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 336
    _globals['_QUERY']._serialized_start = 339
    _globals['_QUERY']._serialized_end = 562