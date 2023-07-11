"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta2 import resource_pb2 as akash_dot_base_dot_v1beta2_dot_resource__pb2
from ....akash.base.v1beta2 import endpoint_pb2 as akash_dot_base_dot_v1beta2_dot_endpoint__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&akash/base/v1beta2/resourceunits.proto\x12\x12akash.base.v1beta2\x1a\x14gogoproto/gogo.proto\x1a!akash/base/v1beta2/resource.proto\x1a!akash/base/v1beta2/endpoint.proto"\xa7\x03\n\rResourceUnits\x12Z\n\x03cpu\x18\x01 \x01(\x0b2\x17.akash.base.v1beta2.CPUB4\xc8\xde\x1f\x01\xe2\xde\x1f\x03CPU\xea\xde\x1f\rcpu,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"\x12_\n\x06memory\x18\x02 \x01(\x0b2\x1a.akash.base.v1beta2.MemoryB3\xc8\xde\x1f\x01\xea\xde\x1f\x10memory,omitempty\xf2\xde\x1f\x17yaml:"memory,omitempty"\x12n\n\x07storage\x18\x03 \x03(\x0b2\x1b.akash.base.v1beta2.StorageB@\xc8\xde\x1f\x00\xea\xde\x1f\x11storage,omitempty\xf2\xde\x1f\x18yaml:"storage,omitempty"\xaa\xdf\x1f\x07Volumes\x12c\n\tendpoints\x18\x04 \x03(\x0b2\x1c.akash.base.v1beta2.EndpointB2\xc8\xde\x1f\x00\xea\xde\x1f\tendpoints\xf2\xde\x1f\x10yaml:"endpoints"\xaa\xdf\x1f\tEndpoints:\x04\xe8\xa0\x1f\x01B:Z8github.com/akash-network/akash-api/go/node/types/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.base.v1beta2.resourceunits_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/types/v1beta2'
    _RESOURCEUNITS.fields_by_name['cpu']._options = None
    _RESOURCEUNITS.fields_by_name['cpu']._serialized_options = b'\xc8\xde\x1f\x01\xe2\xde\x1f\x03CPU\xea\xde\x1f\rcpu,omitempty\xf2\xde\x1f\x14yaml:"cpu,omitempty"'
    _RESOURCEUNITS.fields_by_name['memory']._options = None
    _RESOURCEUNITS.fields_by_name['memory']._serialized_options = b'\xc8\xde\x1f\x01\xea\xde\x1f\x10memory,omitempty\xf2\xde\x1f\x17yaml:"memory,omitempty"'
    _RESOURCEUNITS.fields_by_name['storage']._options = None
    _RESOURCEUNITS.fields_by_name['storage']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x11storage,omitempty\xf2\xde\x1f\x18yaml:"storage,omitempty"\xaa\xdf\x1f\x07Volumes'
    _RESOURCEUNITS.fields_by_name['endpoints']._options = None
    _RESOURCEUNITS.fields_by_name['endpoints']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tendpoints\xf2\xde\x1f\x10yaml:"endpoints"\xaa\xdf\x1f\tEndpoints'
    _RESOURCEUNITS._options = None
    _RESOURCEUNITS._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_RESOURCEUNITS']._serialized_start = 155
    _globals['_RESOURCEUNITS']._serialized_end = 578