"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta3 import attribute_pb2 as akash_dot_base_dot_v1beta3_dot_attribute__pb2
from ....akash.base.v1beta3 import resourcevalue_pb2 as akash_dot_base_dot_v1beta3_dot_resourcevalue__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cakash/base/v1beta3/cpu.proto\x12\x12akash.base.v1beta3\x1a\x14gogoproto/gogo.proto\x1a"akash/base/v1beta3/attribute.proto\x1a&akash/base/v1beta3/resourcevalue.proto"\xc1\x01\n\x03CPU\x126\n\x05units\x18\x01 \x01(\x0b2!.akash.base.v1beta3.ResourceValueB\x04\xc8\xde\x1f\x00\x12|\n\nattributes\x18\x02 \x03(\x0b2\x1d.akash.base.v1beta3.AttributeBI\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"\xaa\xdf\x1f\nAttributes:\x04\xe8\xa0\x1f\x01B:Z8github.com/akash-network/akash-api/go/node/types/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.base.v1beta3.cpu_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/types/v1beta3'
    _CPU.fields_by_name['units']._options = None
    _CPU.fields_by_name['units']._serialized_options = b'\xc8\xde\x1f\x00'
    _CPU.fields_by_name['attributes']._options = None
    _CPU.fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x14attributes,omitempty\xf2\xde\x1f\x1byaml:"attributes,omitempty"\xaa\xdf\x1f\nAttributes'
    _CPU._options = None
    _CPU._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_CPU']._serialized_start = 151
    _globals['_CPU']._serialized_end = 344