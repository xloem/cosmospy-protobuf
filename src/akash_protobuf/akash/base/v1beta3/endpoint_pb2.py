"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!akash/base/v1beta3/endpoint.proto\x12\x12akash.base.v1beta3\x1a\x14gogoproto/gogo.proto"\xd4\x01\n\x08Endpoint\x12/\n\x04kind\x18\x01 \x01(\x0e2!.akash.base.v1beta3.Endpoint.Kind\x12X\n\x0fsequence_number\x18\x02 \x01(\rB?\xe2\xde\x1f\x0eSequenceNumber\xea\xde\x1f\x0fsequence_number\xf2\xde\x1f\x16yaml:"sequence_number""7\n\x04Kind\x12\x0f\n\x0bSHARED_HTTP\x10\x00\x12\x0f\n\x0bRANDOM_PORT\x10\x01\x12\r\n\tLEASED_IP\x10\x02:\x04\xe8\xa0\x1f\x01B:Z8github.com/akash-network/akash-api/go/node/types/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.base.v1beta3.endpoint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/akash-network/akash-api/go/node/types/v1beta3'
    _ENDPOINT.fields_by_name['sequence_number']._options = None
    _ENDPOINT.fields_by_name['sequence_number']._serialized_options = b'\xe2\xde\x1f\x0eSequenceNumber\xea\xde\x1f\x0fsequence_number\xf2\xde\x1f\x16yaml:"sequence_number"'
    _ENDPOINT._options = None
    _ENDPOINT._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_ENDPOINT']._serialized_start = 80
    _globals['_ENDPOINT']._serialized_end = 292
    _globals['_ENDPOINT_KIND']._serialized_start = 231
    _globals['_ENDPOINT_KIND']._serialized_end = 286