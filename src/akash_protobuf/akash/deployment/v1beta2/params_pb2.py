"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%akash/deployment/v1beta2/params.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x9d\x01\n\x06Params\x12\x92\x01\n\x16deployment_min_deposit\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinBW\xc8\xde\x1f\x00\xe2\xde\x1f\x14DeploymentMinDeposit\xea\xde\x1f\x16deployment_min_deposit\xf2\xde\x1f\x1dyaml:"deployment_min_deposit"B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta2.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta2'
    _PARAMS.fields_by_name['deployment_min_deposit']._options = None
    _PARAMS.fields_by_name['deployment_min_deposit']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x14DeploymentMinDeposit\xea\xde\x1f\x16deployment_min_deposit\xf2\xde\x1f\x1dyaml:"deployment_min_deposit"'
    _globals['_PARAMS']._serialized_start = 122
    _globals['_PARAMS']._serialized_end = 279