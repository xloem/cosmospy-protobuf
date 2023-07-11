"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)akash/deployment/v1beta3/deployment.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto"q\n\x0cDeploymentID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\x90\x03\n\nDeployment\x12f\n\rdeployment_id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta3.DeploymentIDB\'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cDeploymentID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12T\n\x05state\x18\x02 \x01(\x0e2*.akash.deployment.v1beta3.Deployment.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12.\n\x07version\x18\x03 \x01(\x0cB\x1d\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"z\n\x05State\x12\'\n\x07invalid\x10\x00\x1a\x1a\x8a\x9d \x16DeploymentStateInvalid\x12 \n\x06active\x10\x01\x1a\x14\x8a\x9d \x10DeploymentActive\x12 \n\x06closed\x10\x02\x1a\x14\x8a\x9d \x10DeploymentClosed\x1a\x04\x88\xa3\x1e\x00:\x04\xe8\xa0\x1f\x00"\x9c\x01\n\x11DeploymentFilters\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12(\n\x05state\x18\x03 \x01(\tB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state":\x04\xe8\xa0\x1f\x00B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.deployment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _DEPLOYMENTID.fields_by_name['owner']._options = None
    _DEPLOYMENTID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _DEPLOYMENTID.fields_by_name['dseq']._options = None
    _DEPLOYMENTID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _DEPLOYMENTID._options = None
    _DEPLOYMENTID._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DEPLOYMENT_STATE._options = None
    _DEPLOYMENT_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _DEPLOYMENT_STATE.values_by_name['invalid']._options = None
    _DEPLOYMENT_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x16DeploymentStateInvalid'
    _DEPLOYMENT_STATE.values_by_name['active']._options = None
    _DEPLOYMENT_STATE.values_by_name['active']._serialized_options = b'\x8a\x9d \x10DeploymentActive'
    _DEPLOYMENT_STATE.values_by_name['closed']._options = None
    _DEPLOYMENT_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x10DeploymentClosed'
    _DEPLOYMENT.fields_by_name['deployment_id']._options = None
    _DEPLOYMENT.fields_by_name['deployment_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x0cDeploymentID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _DEPLOYMENT.fields_by_name['state']._options = None
    _DEPLOYMENT.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _DEPLOYMENT.fields_by_name['version']._options = None
    _DEPLOYMENT.fields_by_name['version']._serialized_options = b'\xea\xde\x1f\x07version\xf2\xde\x1f\x0eyaml:"version"'
    _DEPLOYMENT._options = None
    _DEPLOYMENT._serialized_options = b'\xe8\xa0\x1f\x00'
    _DEPLOYMENTFILTERS.fields_by_name['owner']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _DEPLOYMENTFILTERS.fields_by_name['dseq']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _DEPLOYMENTFILTERS.fields_by_name['state']._options = None
    _DEPLOYMENTFILTERS.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _DEPLOYMENTFILTERS._options = None
    _DEPLOYMENTFILTERS._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_DEPLOYMENTID']._serialized_start = 93
    _globals['_DEPLOYMENTID']._serialized_end = 206
    _globals['_DEPLOYMENT']._serialized_start = 209
    _globals['_DEPLOYMENT']._serialized_end = 609
    _globals['_DEPLOYMENT_STATE']._serialized_start = 481
    _globals['_DEPLOYMENT_STATE']._serialized_end = 603
    _globals['_DEPLOYMENTFILTERS']._serialized_start = 612
    _globals['_DEPLOYMENTFILTERS']._serialized_end = 768