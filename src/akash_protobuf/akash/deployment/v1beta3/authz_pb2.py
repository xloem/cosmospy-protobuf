"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/deployment/v1beta3/authz.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"x\n\x1eDepositDeploymentAuthorization\x12C\n\x0bspend_limit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x13\xc8\xde\x1f\x00\xea\xde\x1f\x0bspend_limit:\x11\xca\xb4-\rAuthorizationB?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _DEPOSITDEPLOYMENTAUTHORIZATION.fields_by_name['spend_limit']._options = None
    _DEPOSITDEPLOYMENTAUTHORIZATION.fields_by_name['spend_limit']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0bspend_limit'
    _DEPOSITDEPLOYMENTAUTHORIZATION._options = None
    _DEPOSITDEPLOYMENTAUTHORIZATION._serialized_options = b'\xca\xb4-\rAuthorization'
    _globals['_DEPOSITDEPLOYMENTAUTHORIZATION']._serialized_start = 147
    _globals['_DEPOSITDEPLOYMENTAUTHORIZATION']._serialized_end = 267