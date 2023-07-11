"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta2 import deployment_pb2 as akash_dot_deployment_dot_v1beta2_dot_deployment__pb2
from ....akash.deployment.v1beta2 import group_pb2 as akash_dot_deployment_dot_v1beta2_dot_group__pb2
from ....akash.deployment.v1beta2 import params_pb2 as akash_dot_deployment_dot_v1beta2_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&akash/deployment/v1beta2/genesis.proto\x12\x18akash.deployment.v1beta2\x1a\x14gogoproto/gogo.proto\x1a)akash/deployment/v1beta2/deployment.proto\x1a$akash/deployment/v1beta2/group.proto\x1a%akash/deployment/v1beta2/params.proto"\xc8\x01\n\x11GenesisDeployment\x12a\n\ndeployment\x18\x01 \x01(\x0b2$.akash.deployment.v1beta2.DeploymentB\'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"\x12P\n\x06groups\x18\x02 \x03(\x0b2\x1f.akash.deployment.v1beta2.GroupB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups""\xce\x01\n\x0cGenesisState\x12k\n\x0bdeployments\x18\x01 \x03(\x0b2+.akash.deployment.v1beta2.GenesisDeploymentB)\xc8\xde\x1f\x00\xea\xde\x1f\x0bdeployments\xf2\xde\x1f\x12yaml:"deployments"\x12Q\n\x06params\x18\x02 \x01(\x0b2 .akash.deployment.v1beta2.ParamsB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta2.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta2'
    _GENESISDEPLOYMENT.fields_by_name['deployment']._options = None
    _GENESISDEPLOYMENT.fields_by_name['deployment']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"'
    _GENESISDEPLOYMENT.fields_by_name['groups']._options = None
    _GENESISDEPLOYMENT.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _GENESISSTATE.fields_by_name['deployments']._options = None
    _GENESISSTATE.fields_by_name['deployments']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0bdeployments\xf2\xde\x1f\x12yaml:"deployments"'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06params\xf2\xde\x1f\ryaml:"params"'
    _globals['_GENESISDEPLOYMENT']._serialized_start = 211
    _globals['_GENESISDEPLOYMENT']._serialized_end = 411
    _globals['_GENESISSTATE']._serialized_start = 414
    _globals['_GENESISSTATE']._serialized_end = 620