"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n\x19cosmos_proto/cosmos.proto\x12\x0ccosmos_proto\x1a google/protobuf/descriptor.proto:9\n\x0einterface_type\x12\x1f.google.protobuf.MessageOptions\x18\xc9\xd6\x05 \x01(\t:?\n\x14implements_interface\x12\x1f.google.protobuf.MessageOptions\x18\xca\xd6\x05 \x01(\t::\n\x11accepts_interface\x12\x1d.google.protobuf.FieldOptions\x18\xc9\xd6\x05 \x01(\tB'Z%github.com/regen-network/cosmos-protob\x06proto3")
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos_proto.cosmos_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(interface_type)
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(implements_interface)
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(accepts_interface)
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/regen-network/cosmos-proto'