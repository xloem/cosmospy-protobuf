"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.provider.v1beta2 import provider_pb2 as akash_dot_provider_dot_v1beta2_dot_provider__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/provider/v1beta2/query.proto\x12\x16akash.provider.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a%akash/provider/v1beta2/provider.proto"S\n\x15QueryProvidersRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x9d\x01\n\x16QueryProvidersResponse\x12F\n\tproviders\x18\x01 \x03(\x0b2 .akash.provider.v1beta2.ProviderB\x11\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"%\n\x14QueryProviderRequest\x12\r\n\x05owner\x18\x01 \x01(\t"Q\n\x15QueryProviderResponse\x128\n\x08provider\x18\x01 \x01(\x0b2 .akash.provider.v1beta2.ProviderB\x04\xc8\xde\x1f\x002\xbc\x02\n\x05Query\x12\x95\x01\n\tProviders\x12-.akash.provider.v1beta2.QueryProvidersRequest\x1a..akash.provider.v1beta2.QueryProvidersResponse")\x82\xd3\xe4\x93\x02#\x12!/akash/provider/v1beta2/providers\x12\x9a\x01\n\x08Provider\x12,.akash.provider.v1beta2.QueryProviderRequest\x1a-.akash.provider.v1beta2.QueryProviderResponse"1\x82\xd3\xe4\x93\x02+\x12)/akash/provider/v1beta2/providers/{owner}B=Z;github.com/akash-network/akash-api/go/node/provider/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.provider.v1beta2.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/akash-network/akash-api/go/node/provider/v1beta2'
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._options = None
    _QUERYPROVIDERSRESPONSE.fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\tProviders'
    _QUERYPROVIDERRESPONSE.fields_by_name['provider']._options = None
    _QUERYPROVIDERRESPONSE.fields_by_name['provider']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Providers']._options = None
    _QUERY.methods_by_name['Providers']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/akash/provider/v1beta2/providers'
    _QUERY.methods_by_name['Provider']._options = None
    _QUERY.methods_by_name['Provider']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/akash/provider/v1beta2/providers/{owner}'
    _globals['_QUERYPROVIDERSREQUEST']._serialized_start = 197
    _globals['_QUERYPROVIDERSREQUEST']._serialized_end = 280
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_start = 283
    _globals['_QUERYPROVIDERSRESPONSE']._serialized_end = 440
    _globals['_QUERYPROVIDERREQUEST']._serialized_start = 442
    _globals['_QUERYPROVIDERREQUEST']._serialized_end = 479
    _globals['_QUERYPROVIDERRESPONSE']._serialized_start = 481
    _globals['_QUERYPROVIDERRESPONSE']._serialized_end = 562
    _globals['_QUERY']._serialized_start = 565
    _globals['_QUERY']._serialized_end = 881