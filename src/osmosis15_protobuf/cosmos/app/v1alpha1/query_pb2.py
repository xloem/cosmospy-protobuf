"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.app.v1alpha1 import config_pb2 as cosmos_dot_app_dot_v1alpha1_dot_config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/app/v1alpha1/query.proto\x12\x13cosmos.app.v1alpha1\x1a cosmos/app/v1alpha1/config.proto"\x14\n\x12QueryConfigRequest"B\n\x13QueryConfigResponse\x12+\n\x06config\x18\x01 \x01(\x0b2\x1b.cosmos.app.v1alpha1.Config2f\n\x05Query\x12]\n\x06Config\x12\'.cosmos.app.v1alpha1.QueryConfigRequest\x1a(.cosmos.app.v1alpha1.QueryConfigResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.v1alpha1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_QUERYCONFIGREQUEST']._serialized_start = 90
    _globals['_QUERYCONFIGREQUEST']._serialized_end = 110
    _globals['_QUERYCONFIGRESPONSE']._serialized_start = 112
    _globals['_QUERYCONFIGRESPONSE']._serialized_end = 178
    _globals['_QUERY']._serialized_start = 180
    _globals['_QUERY']._serialized_end = 282