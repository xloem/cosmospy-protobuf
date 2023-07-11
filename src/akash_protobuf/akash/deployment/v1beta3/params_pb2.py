"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/deployment/v1beta3/params.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto"\xc2\x01\n\x06Params\x12\x83\x01\n\x0cmin_deposits\x18\x01 \x03(\x0b21.akash.deployment.v1beta3.Params.MinDepositsEntryB:\xc8\xde\x1f\x00\xe2\xde\x1f\x0bMinDeposits\xea\xde\x1f\x0cmin_deposits\xf2\xde\x1f\x13yaml:"min_deposits"\x1a2\n\x10MinDepositsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x028\x01B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _PARAMS_MINDEPOSITSENTRY._options = None
    _PARAMS_MINDEPOSITSENTRY._serialized_options = b'8\x01'
    _PARAMS.fields_by_name['min_deposits']._options = None
    _PARAMS.fields_by_name['min_deposits']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0bMinDeposits\xea\xde\x1f\x0cmin_deposits\xf2\xde\x1f\x13yaml:"min_deposits"'
    _globals['_PARAMS']._serialized_start = 90
    _globals['_PARAMS']._serialized_end = 284
    _globals['_PARAMS_MINDEPOSITSENTRY']._serialized_start = 234
    _globals['_PARAMS_MINDEPOSITSENTRY']._serialized_end = 284