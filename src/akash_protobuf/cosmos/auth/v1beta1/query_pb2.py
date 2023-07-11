"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/auth/v1beta1/query.proto\x12\x13cosmos.auth.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto\x1a\x19cosmos_proto/cosmos.proto"R\n\x14QueryAccountsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8a\x01\n\x15QueryAccountsResponse\x124\n\x08accounts\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08AccountI\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"0\n\x13QueryAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"K\n\x14QueryAccountResponse\x123\n\x07account\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x0c\xca\xb4-\x08AccountI"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.auth.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"/\n\x1fQueryModuleAccountByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"]\n QueryModuleAccountByNameResponse\x129\n\x07account\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x12\xca\xb4-\x0eModuleAccountI2\xe1\x04\n\x05Query\x12\x88\x01\n\x08Accounts\x12).cosmos.auth.v1beta1.QueryAccountsRequest\x1a*.cosmos.auth.v1beta1.QueryAccountsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/auth/v1beta1/accounts\x12\x8f\x01\n\x07Account\x12(.cosmos.auth.v1beta1.QueryAccountRequest\x1a).cosmos.auth.v1beta1.QueryAccountResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/auth/v1beta1/accounts/{address}\x12\x80\x01\n\x06Params\x12\'.cosmos.auth.v1beta1.QueryParamsRequest\x1a(.cosmos.auth.v1beta1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/auth/v1beta1/params\x12\xb7\x01\n\x13ModuleAccountByName\x124.cosmos.auth.v1beta1.QueryModuleAccountByNameRequest\x1a5.cosmos.auth.v1beta1.QueryModuleAccountByNameResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/auth/v1beta1/module_accounts/{name}B+Z)github.com/cosmos/cosmos-sdk/x/auth/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.auth.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/auth/types'
    _QUERYACCOUNTSRESPONSE.fields_by_name['accounts']._options = None
    _QUERYACCOUNTSRESPONSE.fields_by_name['accounts']._serialized_options = b'\xca\xb4-\x08AccountI'
    _QUERYACCOUNTREQUEST._options = None
    _QUERYACCOUNTREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYACCOUNTRESPONSE.fields_by_name['account']._options = None
    _QUERYACCOUNTRESPONSE.fields_by_name['account']._serialized_options = b'\xca\xb4-\x08AccountI'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYMODULEACCOUNTBYNAMERESPONSE.fields_by_name['account']._options = None
    _QUERYMODULEACCOUNTBYNAMERESPONSE.fields_by_name['account']._serialized_options = b'\xca\xb4-\x0eModuleAccountI'
    _QUERY.methods_by_name['Accounts']._options = None
    _QUERY.methods_by_name['Accounts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/auth/v1beta1/accounts'
    _QUERY.methods_by_name['Account']._options = None
    _QUERY.methods_by_name['Account']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/auth/v1beta1/accounts/{address}"
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/auth/v1beta1/params'
    _QUERY.methods_by_name['ModuleAccountByName']._options = None
    _QUERY.methods_by_name['ModuleAccountByName']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/auth/v1beta1/module_accounts/{name}'
    _globals['_QUERYACCOUNTSREQUEST']._serialized_start = 238
    _globals['_QUERYACCOUNTSREQUEST']._serialized_end = 320
    _globals['_QUERYACCOUNTSRESPONSE']._serialized_start = 323
    _globals['_QUERYACCOUNTSRESPONSE']._serialized_end = 461
    _globals['_QUERYACCOUNTREQUEST']._serialized_start = 463
    _globals['_QUERYACCOUNTREQUEST']._serialized_end = 511
    _globals['_QUERYACCOUNTRESPONSE']._serialized_start = 513
    _globals['_QUERYACCOUNTRESPONSE']._serialized_end = 588
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 590
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 610
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 612
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 684
    _globals['_QUERYMODULEACCOUNTBYNAMEREQUEST']._serialized_start = 686
    _globals['_QUERYMODULEACCOUNTBYNAMEREQUEST']._serialized_end = 733
    _globals['_QUERYMODULEACCOUNTBYNAMERESPONSE']._serialized_start = 735
    _globals['_QUERYMODULEACCOUNTBYNAMERESPONSE']._serialized_end = 828
    _globals['_QUERY']._serialized_start = 831
    _globals['_QUERY']._serialized_end = 1440