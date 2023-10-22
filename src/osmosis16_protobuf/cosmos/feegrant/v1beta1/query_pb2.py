"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.feegrant.v1beta1 import feegrant_pb2 as cosmos_dot_feegrant_dot_v1beta1_dot_feegrant__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/feegrant/v1beta1/query.proto\x12\x17cosmos.feegrant.v1beta1\x1a&cosmos/feegrant/v1beta1/feegrant.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19cosmos_proto/cosmos.proto"m\n\x15QueryAllowanceRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12)\n\x07grantee\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"K\n\x16QueryAllowanceResponse\x121\n\tallowance\x18\x01 \x01(\x0b2\x1e.cosmos.feegrant.v1beta1.Grant"\x7f\n\x16QueryAllowancesRequest\x12)\n\x07grantee\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8a\x01\n\x17QueryAllowancesResponse\x122\n\nallowances\x18\x01 \x03(\x0b2\x1e.cosmos.feegrant.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x88\x01\n\x1fQueryAllowancesByGranterRequest\x12)\n\x07granter\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x93\x01\n QueryAllowancesByGranterResponse\x122\n\nallowances\x18\x01 \x03(\x0b2\x1e.cosmos.feegrant.v1beta1.Grant\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\x9f\x04\n\x05Query\x12\xac\x01\n\tAllowance\x12..cosmos.feegrant.v1beta1.QueryAllowanceRequest\x1a/.cosmos.feegrant.v1beta1.QueryAllowanceResponse">\x82\xd3\xe4\x93\x028\x126/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}\x12\xa6\x01\n\nAllowances\x12/.cosmos.feegrant.v1beta1.QueryAllowancesRequest\x1a0.cosmos.feegrant.v1beta1.QueryAllowancesResponse"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/feegrant/v1beta1/allowances/{grantee}\x12\xbd\x01\n\x13AllowancesByGranter\x128.cosmos.feegrant.v1beta1.QueryAllowancesByGranterRequest\x1a9.cosmos.feegrant.v1beta1.QueryAllowancesByGranterResponse"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/feegrant/v1beta1/issued/{granter}B)Z\'github.com/cosmos/cosmos-sdk/x/feegrantb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.feegrant.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z'github.com/cosmos/cosmos-sdk/x/feegrant"
    _QUERYALLOWANCEREQUEST.fields_by_name['granter']._options = None
    _QUERYALLOWANCEREQUEST.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYALLOWANCEREQUEST.fields_by_name['grantee']._options = None
    _QUERYALLOWANCEREQUEST.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYALLOWANCESREQUEST.fields_by_name['grantee']._options = None
    _QUERYALLOWANCESREQUEST.fields_by_name['grantee']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYALLOWANCESBYGRANTERREQUEST.fields_by_name['granter']._options = None
    _QUERYALLOWANCESBYGRANTERREQUEST.fields_by_name['granter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERY.methods_by_name['Allowance']._options = None
    _QUERY.methods_by_name['Allowance']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/cosmos/feegrant/v1beta1/allowance/{granter}/{grantee}'
    _QUERY.methods_by_name['Allowances']._options = None
    _QUERY.methods_by_name['Allowances']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/cosmos/feegrant/v1beta1/allowances/{grantee}'
    _QUERY.methods_by_name['AllowancesByGranter']._options = None
    _QUERY.methods_by_name['AllowancesByGranter']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/cosmos/feegrant/v1beta1/issued/{granter}'
    _globals['_QUERYALLOWANCEREQUEST']._serialized_start = 205
    _globals['_QUERYALLOWANCEREQUEST']._serialized_end = 314
    _globals['_QUERYALLOWANCERESPONSE']._serialized_start = 316
    _globals['_QUERYALLOWANCERESPONSE']._serialized_end = 391
    _globals['_QUERYALLOWANCESREQUEST']._serialized_start = 393
    _globals['_QUERYALLOWANCESREQUEST']._serialized_end = 520
    _globals['_QUERYALLOWANCESRESPONSE']._serialized_start = 523
    _globals['_QUERYALLOWANCESRESPONSE']._serialized_end = 661
    _globals['_QUERYALLOWANCESBYGRANTERREQUEST']._serialized_start = 664
    _globals['_QUERYALLOWANCESBYGRANTERREQUEST']._serialized_end = 800
    _globals['_QUERYALLOWANCESBYGRANTERRESPONSE']._serialized_start = 803
    _globals['_QUERYALLOWANCESBYGRANTERRESPONSE']._serialized_end = 950
    _globals['_QUERY']._serialized_start = 953
    _globals['_QUERY']._serialized_end = 1496