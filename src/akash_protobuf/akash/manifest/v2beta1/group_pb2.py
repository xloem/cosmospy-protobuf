"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.manifest.v2beta1 import service_pb2 as akash_dot_manifest_dot_v2beta1_dot_service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"akash/manifest/v2beta1/group.proto\x12\x16akash.manifest.v2beta1\x1a\x14gogoproto/gogo.proto\x1a$akash/manifest/v2beta1/service.proto"\x8c\x01\n\x05Group\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12V\n\x08services\x18\x02 \x03(\x0b2\x1f.akash.manifest.v2beta1.ServiceB#\xc8\xde\x1f\x00\xea\xde\x1f\x08services\xf2\xde\x1f\x0fyaml:"services":\x04\x88\xa0\x1f\x00B@Z6github.com/akash-network/akash-api/go/manifest/v2beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.manifest.v2beta1.group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/manifest/v2beta1\xd8\xe1\x1e\x00\x80\xe2\x1e\x01'
    _GROUP.fields_by_name['name']._options = None
    _GROUP.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _GROUP.fields_by_name['services']._options = None
    _GROUP.fields_by_name['services']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x08services\xf2\xde\x1f\x0fyaml:"services"'
    _GROUP._options = None
    _GROUP._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_GROUP']._serialized_start = 123
    _globals['_GROUP']._serialized_end = 263