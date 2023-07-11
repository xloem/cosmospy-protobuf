"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta3 import attribute_pb2 as akash_dot_base_dot_v1beta3_dot_attribute__pb2
from ....akash.base.v1beta3 import resourcevalue_pb2 as akash_dot_base_dot_v1beta3_dot_resourcevalue__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/base/v1beta3/storage.proto\x12\x12akash.base.v1beta3\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta3/attribute.proto\x1a&akash/base/v1beta3/resourcevalue.proto"\x86\x02\n\x07Storage\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12P\n\x08quantity\x18\x02 \x01(\x0b2!.akash.base.v1beta3.ResourceValueB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"\x12|\n\nattributes\x18\x03 \x03(\x0b2\x1d.akash.base.v1beta3.AttributeBI\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"\xaa\xdf\x1f\nAttributes:\x04\xe8\xa0\x1f\x01B:Z8github.com/akash-network/akash-api/go/node/types/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.base.v1beta3.storage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/types/v1beta3'
    _STORAGE.fields_by_name['name']._options = None
    _STORAGE.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _STORAGE.fields_by_name['quantity']._options = None
    _STORAGE.fields_by_name['quantity']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04size\xf2\xde\x1f\x0byaml:"size"'
    _STORAGE.fields_by_name['attributes']._options = None
    _STORAGE.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"\xaa\xdf\x1f\nAttributes'
    _STORAGE._options = None
    _STORAGE._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_STORAGE']._serialized_start = 155
    _globals['_STORAGE']._serialized_end = 417