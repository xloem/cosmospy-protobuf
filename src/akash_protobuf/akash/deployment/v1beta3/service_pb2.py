"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....akash.deployment.v1beta3 import deploymentmsg_pb2 as akash_dot_deployment_dot_v1beta3_dot_deploymentmsg__pb2
from ....akash.deployment.v1beta3 import groupmsg_pb2 as akash_dot_deployment_dot_v1beta3_dot_groupmsg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b"\n&akash/deployment/v1beta3/service.proto\x12\x18akash.deployment.v1beta3\x1a,akash/deployment/v1beta3/deploymentmsg.proto\x1a'akash/deployment/v1beta3/groupmsg.proto2\xa5\x06\n\x03Msg\x12x\n\x10CreateDeployment\x12-.akash.deployment.v1beta3.MsgCreateDeployment\x1a5.akash.deployment.v1beta3.MsgCreateDeploymentResponse\x12{\n\x11DepositDeployment\x12..akash.deployment.v1beta3.MsgDepositDeployment\x1a6.akash.deployment.v1beta3.MsgDepositDeploymentResponse\x12x\n\x10UpdateDeployment\x12-.akash.deployment.v1beta3.MsgUpdateDeployment\x1a5.akash.deployment.v1beta3.MsgUpdateDeploymentResponse\x12u\n\x0fCloseDeployment\x12,.akash.deployment.v1beta3.MsgCloseDeployment\x1a4.akash.deployment.v1beta3.MsgCloseDeploymentResponse\x12f\n\nCloseGroup\x12'.akash.deployment.v1beta3.MsgCloseGroup\x1a/.akash.deployment.v1beta3.MsgCloseGroupResponse\x12f\n\nPauseGroup\x12'.akash.deployment.v1beta3.MsgPauseGroup\x1a/.akash.deployment.v1beta3.MsgPauseGroupResponse\x12f\n\nStartGroup\x12'.akash.deployment.v1beta3.MsgStartGroup\x1a/.akash.deployment.v1beta3.MsgStartGroupResponseB?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3")
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _globals['_MSG']._serialized_start = 156
    _globals['_MSG']._serialized_end = 961