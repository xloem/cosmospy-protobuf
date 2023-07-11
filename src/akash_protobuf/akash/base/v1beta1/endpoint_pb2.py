"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/base/v1beta1/endpoint.proto\x12\x12akash.base.v1beta1\x1a\x14gogoproto/gogo.proto"k\n\x08Endpoint\x12/\n\x04kind\x18\x01 \x01(\x0e2!.akash.base.v1beta1.Endpoint.Kind"(\n\x04Kind\x12\x0f\n\x0bSHARED_HTTP\x10\x00\x12\x0f\n\x0bRANDOM_PORT\x10\x01:\x04\xe8\xa0\x1f\x01B:Z8github.com/akash-network/akash-api/go/node/types/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.base.v1beta1.endpoint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/types/v1beta1'
    _ENDPOINT._options = None
    _ENDPOINT._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_ENDPOINT']._serialized_start = 79
    _globals['_ENDPOINT']._serialized_end = 186
    _globals['_ENDPOINT_KIND']._serialized_start = 140
    _globals['_ENDPOINT_KIND']._serialized_end = 180