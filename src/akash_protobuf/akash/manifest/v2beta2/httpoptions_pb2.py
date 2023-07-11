"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(akash/manifest/v2beta2/httpoptions.proto\x12\x16akash.manifest.v2beta2\x1a\x14gogoproto/gogo.proto"\xfd\x02\n\x18ServiceExposeHTTPOptions\x12<\n\rmax_body_size\x18\x01 \x01(\rB%\xea\xde\x1f\x0bmaxBodySize\xf2\xde\x1f\x12yaml:"maxBodySize"\x12;\n\x0cread_timeout\x18\x02 \x01(\rB%\xea\xde\x1f\x0breadTimeout\xf2\xde\x1f\x12yaml:"readTimeout"\x12;\n\x0csend_timeout\x18\x03 \x01(\rB%\xea\xde\x1f\x0bsendTimeout\xf2\xde\x1f\x12yaml:"sendTimeout"\x125\n\nnext_tries\x18\x04 \x01(\rB!\xea\xde\x1f\tnextTries\xf2\xde\x1f\x10yaml:"nextTries"\x12;\n\x0cnext_timeout\x18\x05 \x01(\rB%\xea\xde\x1f\x0bnextTimeout\xf2\xde\x1f\x12yaml:"nextTimeout"\x125\n\nnext_cases\x18\x06 \x03(\tB!\xea\xde\x1f\tnextCases\xf2\xde\x1f\x10yaml:"nextCases"B@Z6github.com/akash-network/akash-api/go/manifest/v2beta2\xd8\xe1\x1e\x00\x80\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.manifest.v2beta2.httpoptions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/manifest/v2beta2\xd8\xe1\x1e\x00\x80\xe2\x1e\x01'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['max_body_size']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['max_body_size']._serialized_options = b'\xea\xde\x1f\x0bmaxBodySize\xf2\xde\x1f\x12yaml:"maxBodySize"'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['read_timeout']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['read_timeout']._serialized_options = b'\xea\xde\x1f\x0breadTimeout\xf2\xde\x1f\x12yaml:"readTimeout"'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['send_timeout']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['send_timeout']._serialized_options = b'\xea\xde\x1f\x0bsendTimeout\xf2\xde\x1f\x12yaml:"sendTimeout"'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_tries']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_tries']._serialized_options = b'\xea\xde\x1f\tnextTries\xf2\xde\x1f\x10yaml:"nextTries"'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_timeout']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_timeout']._serialized_options = b'\xea\xde\x1f\x0bnextTimeout\xf2\xde\x1f\x12yaml:"nextTimeout"'
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_cases']._options = None
    _SERVICEEXPOSEHTTPOPTIONS.fields_by_name['next_cases']._serialized_options = b'\xea\xde\x1f\tnextCases\xf2\xde\x1f\x10yaml:"nextCases"'
    _globals['_SERVICEEXPOSEHTTPOPTIONS']._serialized_start = 91
    _globals['_SERVICEEXPOSEHTTPOPTIONS']._serialized_end = 472