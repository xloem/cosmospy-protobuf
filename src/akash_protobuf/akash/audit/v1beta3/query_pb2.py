"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.audit.v1beta3 import audit_pb2 as akash_dot_audit_dot_v1beta3_dot_audit__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fakash/audit/v1beta3/query.proto\x12\x13akash.audit.v1beta3\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1fakash/audit/v1beta3/audit.proto"\x9a\x01\n\x16QueryProvidersResponse\x12C\n\tproviders\x18\x01 \x03(\x0b2\x1d.akash.audit.v1beta3.ProviderB\x11\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"6\n\x14QueryProviderRequest\x12\x0f\n\x07auditor\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t"`\n"QueryAllProvidersAttributesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"k\n\x1eQueryProviderAttributesRequest\x12\r\n\x05owner\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"=\n\x1bQueryProviderAuditorRequest\x12\x0f\n\x07auditor\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t"l\n\x1dQueryAuditorAttributesRequest\x12\x0f\n\x07auditor\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest2\xde\x05\n\x05Query\x12\xb2\x01\n\x16AllProvidersAttributes\x127.akash.audit.v1beta3.QueryAllProvidersAttributesRequest\x1a+.akash.audit.v1beta3.QueryProvidersResponse"2\x82\xd3\xe4\x93\x02,\x12*/akash/audit/v1beta3/audit/attributes/list\x12\xb2\x01\n\x12ProviderAttributes\x123.akash.audit.v1beta3.QueryProviderAttributesRequest\x1a+.akash.audit.v1beta3.QueryProvidersResponse":\x82\xd3\xe4\x93\x024\x122/akash/audit/v1beta3/audit/attributes/{owner}/list\x12\xbb\x01\n\x19ProviderAuditorAttributes\x120.akash.audit.v1beta3.QueryProviderAuditorRequest\x1a+.akash.audit.v1beta3.QueryProvidersResponse"?\x82\xd3\xe4\x93\x029\x127/akash/audit/v1beta3/audit/attributes/{auditor}/{owner}\x12\xac\x01\n\x11AuditorAttributes\x122.akash.audit.v1beta3.QueryAuditorAttributesRequest\x1a+.akash.audit.v1beta3.QueryProvidersResponse"6\x82\xd3\xe4\x93\x020\x12./akash/provider/v1beta3/auditor/{auditor}/listB:Z8github.com/akash-network/akash-api/go/node/audit/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.audit.v1beta3.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/audit/v1beta3'
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._options = None
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders'
    _QUERY.methods_by_name['AllProvidersAttributes']._options = None
    _QUERY.methods_by_name['AllProvidersAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/akash/audit/v1beta3/audit/attributes/list'
    _QUERY.methods_by_name['ProviderAttributes']._options = None
    _QUERY.methods_by_name['ProviderAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/akash/audit/v1beta3/audit/attributes/{owner}/list'
    _QUERY.methods_by_name['ProviderAuditorAttributes']._options = None
    _QUERY.methods_by_name['ProviderAuditorAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/akash/audit/v1beta3/audit/attributes/{auditor}/{owner}'
    _QUERY.methods_by_name['AuditorAttributes']._options = None
    _QUERY.methods_by_name['AuditorAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./akash/provider/v1beta3/auditor/{auditor}/list'
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_start = 186
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_end = 340
    _globals['_QUERYPROVIDERREQUEST']._serialized_start = 342
    _globals['_QUERYPROVIDERREQUEST']._serialized_end = 396
    _globals['_QUERYALLPROVIDERSATTRIBUTESREQUEST']._serialized_start = 398
    _globals['_QUERYALLPROVIDERSATTRIBUTESREQUEST']._serialized_end = 494
    _globals['_QUERYPROVIDERATTRIBUTESREQUEST']._serialized_start = 496
    _globals['_QUERYPROVIDERATTRIBUTESREQUEST']._serialized_end = 603
    _globals['_QUERYPROVIDERAUDITORREQUEST']._serialized_start = 605
    _globals['_QUERYPROVIDERAUDITORREQUEST']._serialized_end = 666
    _globals['_QUERYAUDITORATTRIBUTESREQUEST']._serialized_start = 668
    _globals['_QUERYAUDITORATTRIBUTESREQUEST']._serialized_end = 776
    _globals['_QUERY']._serialized_start = 779
    _globals['_QUERY']._serialized_end = 1513