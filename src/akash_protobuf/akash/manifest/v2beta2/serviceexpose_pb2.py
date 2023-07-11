"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.manifest.v2beta2 import httpoptions_pb2 as akash_dot_manifest_dot_v2beta2_dot_httpoptions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*akash/manifest/v2beta2/serviceexpose.proto\x12\x16akash.manifest.v2beta2\x1a\x14gogoproto/gogo.proto\x1a(akash/manifest/v2beta2/httpoptions.proto"\xc3\x04\n\rServiceExpose\x12%\n\x04port\x18\x01 \x01(\rB\x17\xea\xde\x1f\x04port\xf2\xde\x1f\x0byaml:"port"\x12>\n\rexternal_port\x18\x02 \x01(\rB\'\xea\xde\x1f\x0cexternalPort\xf2\xde\x1f\x13yaml:"externalPort"\x12;\n\x05proto\x18\x03 \x01(\tB,\xea\xde\x1f\x05proto\xf2\xde\x1f\x0cyaml:"proto"\xfa\xde\x1f\x0fServiceProtocol\x12.\n\x07service\x18\x04 \x01(\tB\x1d\xea\xde\x1f\x07service\xf2\xde\x1f\x0eyaml:"service"\x12+\n\x06global\x18\x05 \x01(\x08B\x1b\xea\xde\x1f\x06global\xf2\xde\x1f\ryaml:"global"\x12(\n\x05hosts\x18\x06 \x03(\tB\x19\xea\xde\x1f\x05hosts\xf2\xde\x1f\x0cyaml:"hosts"\x12\x80\x01\n\x0chttp_options\x18\x07 \x01(\x0b20.akash.manifest.v2beta2.ServiceExposeHTTPOptionsB8\xc8\xde\x1f\x00\xe2\xde\x1f\x0bHTTPOptions\xea\xde\x1f\x0bhttpOptions\xf2\xde\x1f\x12yaml:"httpOptions"\x12%\n\x02ip\x18\x08 \x01(\tB\x19\xe2\xde\x1f\x02IP\xea\xde\x1f\x02ip\xf2\xde\x1f\tyaml:"ip"\x12]\n\x18endpoint_sequence_number\x18\t \x01(\rB;\xea\xde\x1f\x16endpointSequenceNumber\xf2\xde\x1f\x1dyaml:"endpointSequenceNumber"B@Z6github.com/akash-network/akash-api/go/manifest/v2beta2\xd8\xe1\x1e\x00\x80\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.manifest.v2beta2.serviceexpose_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/manifest/v2beta2\xd8\xe1\x1e\x00\x80\xe2\x1e\x01'
    _SERVICEEXPOSE.fields_by_name['port']._options = None
    _SERVICEEXPOSE.fields_by_name['port']._serialized_options = b'\xea\xde\x1f\x04port\xf2\xde\x1f\x0byaml:"port"'
    _SERVICEEXPOSE.fields_by_name['external_port']._options = None
    _SERVICEEXPOSE.fields_by_name['external_port']._serialized_options = b'\xea\xde\x1f\x0cexternalPort\xf2\xde\x1f\x13yaml:"externalPort"'
    _SERVICEEXPOSE.fields_by_name['proto']._options = None
    _SERVICEEXPOSE.fields_by_name['proto']._serialized_options = b'\xea\xde\x1f\x05proto\xf2\xde\x1f\x0cyaml:"proto"\xfa\xde\x1f\x0fServiceProtocol'
    _SERVICEEXPOSE.fields_by_name['service']._options = None
    _SERVICEEXPOSE.fields_by_name['service']._serialized_options = b'\xea\xde\x1f\x07service\xf2\xde\x1f\x0eyaml:"service"'
    _SERVICEEXPOSE.fields_by_name['global']._options = None
    _SERVICEEXPOSE.fields_by_name['global']._serialized_options = b'\xea\xde\x1f\x06global\xf2\xde\x1f\ryaml:"global"'
    _SERVICEEXPOSE.fields_by_name['hosts']._options = None
    _SERVICEEXPOSE.fields_by_name['hosts']._serialized_options = b'\xea\xde\x1f\x05hosts\xf2\xde\x1f\x0cyaml:"hosts"'
    _SERVICEEXPOSE.fields_by_name['http_options']._options = None
    _SERVICEEXPOSE.fields_by_name['http_options']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0bHTTPOptions\xea\xde\x1f\x0bhttpOptions\xf2\xde\x1f\x12yaml:"httpOptions"'
    _SERVICEEXPOSE.fields_by_name['ip']._options = None
    _SERVICEEXPOSE.fields_by_name['ip']._serialized_options = b'\xe2\xde\x1f\x02IP\xea\xde\x1f\x02ip\xf2\xde\x1f\tyaml:"ip"'
    _SERVICEEXPOSE.fields_by_name['endpoint_sequence_number']._options = None
    _SERVICEEXPOSE.fields_by_name['endpoint_sequence_number']._serialized_options = b'\xea\xde\x1f\x16endpointSequenceNumber\xf2\xde\x1f\x1dyaml:"endpointSequenceNumber"'
    _globals['_SERVICEEXPOSE']._serialized_start = 135
    _globals['_SERVICEEXPOSE']._serialized_end = 714