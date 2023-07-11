"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.cert.v1beta2 import cert_pb2 as akash_dot_cert_dot_v1beta2_dot_cert__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eakash/cert/v1beta2/query.proto\x12\x12akash.cert.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1dakash/cert/v1beta2/cert.proto"\xa3\x01\n\x13CertificateResponse\x12_\n\x0bcertificate\x18\x01 \x01(\x0b2\x1f.akash.cert.v1beta2.CertificateB)\xc8\xde\x1f\x00\xea\xde\x1f\x0bcertificate\xf2\xde\x1f\x12yaml:"certificate"\x12+\n\x06serial\x18\x02 \x01(\tB\x1b\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial""\x93\x01\n\x18QueryCertificatesRequest\x12;\n\x06filter\x18\x01 \x01(\x0b2%.akash.cert.v1beta2.CertificateFilterB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb5\x01\n\x19QueryCertificatesResponse\x12[\n\x0ccertificates\x18\x01 \x03(\x0b2\'.akash.cert.v1beta2.CertificateResponseB\x1c\xc8\xde\x1f\x00\xaa\xdf\x1f\x14CertificatesResponse\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xa4\x01\n\x05Query\x12\x9a\x01\n\x0cCertificates\x12,.akash.cert.v1beta2.QueryCertificatesRequest\x1a-.akash.cert.v1beta2.QueryCertificatesResponse"-\x82\xd3\xe4\x93\x02\'\x12%/akash/cert/v1beta3/certificates/listB9Z7github.com/akash-network/akash-api/go/node/cert/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.cert.v1beta2.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/akash-network/akash-api/go/node/cert/v1beta2'
    _CERTIFICATERESPONSE.fields_by_name['certificate']._options = None
    _CERTIFICATERESPONSE.fields_by_name['certificate']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0bcertificate\xf2\xde\x1f\x12yaml:"certificate"'
    _CERTIFICATERESPONSE.fields_by_name['serial']._options = None
    _CERTIFICATERESPONSE.fields_by_name['serial']._serialized_options = b'\xea\xde\x1f\x06serial\xf2\xde\x1f\ryaml:"serial"'
    _QUERYCERTIFICATESREQUEST.fields_by_name['filter']._options = None
    _QUERYCERTIFICATESREQUEST.fields_by_name['filter']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYCERTIFICATESRESPONSE.fields_by_name['certificates']._options = None
    _QUERYCERTIFICATESRESPONSE.fields_by_name['certificates']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x14CertificatesResponse'
    _QUERY.methods_by_name['Certificates']._options = None
    _QUERY.methods_by_name['Certificates']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/akash/cert/v1beta3/certificates/list"
    _globals['_CERTIFICATERESPONSE']._serialized_start = 182
    _globals['_CERTIFICATERESPONSE']._serialized_end = 345
    _globals['_QUERYCERTIFICATESREQUEST']._serialized_start = 348
    _globals['_QUERYCERTIFICATESREQUEST']._serialized_end = 495
    _globals['_QUERYCERTIFICATESRESPONSE']._serialized_start = 498
    _globals['_QUERYCERTIFICATESRESPONSE']._serialized_end = 679
    _globals['_QUERY']._serialized_start = 682
    _globals['_QUERY']._serialized_end = 846