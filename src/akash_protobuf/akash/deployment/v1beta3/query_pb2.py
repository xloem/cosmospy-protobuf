"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.deployment.v1beta3 import deployment_pb2 as akash_dot_deployment_dot_v1beta3_dot_deployment__pb2
from ....akash.deployment.v1beta3 import group_pb2 as akash_dot_deployment_dot_v1beta3_dot_group__pb2
from ....akash.deployment.v1beta3 import groupid_pb2 as akash_dot_deployment_dot_v1beta3_dot_groupid__pb2
from ....akash.escrow.v1beta3 import types_pb2 as akash_dot_escrow_dot_v1beta3_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/deployment/v1beta3/query.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a)akash/deployment/v1beta3/deployment.proto\x1a$akash/deployment/v1beta3/group.proto\x1a&akash/deployment/v1beta3/groupid.proto\x1a akash/escrow/v1beta3/types.proto"\x99\x01\n\x17QueryDeploymentsRequest\x12B\n\x07filters\x18\x01 \x01(\x0b2+.akash.deployment.v1beta3.DeploymentFiltersB\x04\xc8\xde\x1f\x00\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xbc\x01\n\x18QueryDeploymentsResponse\x12c\n\x0bdeployments\x18\x01 \x03(\x0b21.akash.deployment.v1beta3.QueryDeploymentResponseB\x1b\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DeploymentResponses\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"X\n\x16QueryDeploymentRequest\x12>\n\x02id\x18\x01 \x01(\x0b2&.akash.deployment.v1beta3.DeploymentIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"\x91\x02\n\x17QueryDeploymentResponse\x12a\n\ndeployment\x18\x01 \x01(\x0b2$.akash.deployment.v1beta3.DeploymentB\'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"\x12P\n\x06groups\x18\x02 \x03(\x0b2\x1f.akash.deployment.v1beta3.GroupB\x1f\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"\x12;\n\x0eescrow_account\x18\x03 \x01(\x0b2\x1d.akash.escrow.v1beta3.AccountB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"N\n\x11QueryGroupRequest\x129\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta3.GroupIDB\n\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID"J\n\x12QueryGroupResponse\x124\n\x05group\x18\x01 \x01(\x0b2\x1f.akash.deployment.v1beta3.GroupB\x04\xc8\xde\x1f\x002\xee\x03\n\x05Query\x12\xa8\x01\n\x0bDeployments\x121.akash.deployment.v1beta3.QueryDeploymentsRequest\x1a2.akash.deployment.v1beta3.QueryDeploymentsResponse"2\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta3/deployments/list\x12\xa5\x01\n\nDeployment\x120.akash.deployment.v1beta3.QueryDeploymentRequest\x1a1.akash.deployment.v1beta3.QueryDeploymentResponse"2\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta3/deployments/info\x12\x91\x01\n\x05Group\x12+.akash.deployment.v1beta3.QueryGroupRequest\x1a,.akash.deployment.v1beta3.QueryGroupResponse"-\x82\xd3\xe4\x93\x02\'\x12%/akash/deployment/v1beta3/groups/infoB?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _QUERYDEPLOYMENTSREQUEST.fields_by_name['filters']._options = None
    _QUERYDEPLOYMENTSREQUEST.fields_by_name['filters']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDEPLOYMENTSRESPONSE.fields_by_name['deployments']._options = None
    _QUERYDEPLOYMENTSRESPONSE.fields_by_name['deployments']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DeploymentResponses'
    _QUERYDEPLOYMENTREQUEST.fields_by_name['id']._options = None
    _QUERYDEPLOYMENTREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['deployment']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['deployment']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\ndeployment\xf2\xde\x1f\x11yaml:"deployment"'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['groups']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x06groups\xf2\xde\x1f\ryaml:"groups"'
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['escrow_account']._options = None
    _QUERYDEPLOYMENTRESPONSE.fields_by_name['escrow_account']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDEPLOYMENTRESPONSE._options = None
    _QUERYDEPLOYMENTRESPONSE._serialized_options = b'\xe8\xa0\x1f\x00'
    _QUERYGROUPREQUEST.fields_by_name['id']._options = None
    _QUERYGROUPREQUEST.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID'
    _QUERYGROUPRESPONSE.fields_by_name['group']._options = None
    _QUERYGROUPRESPONSE.fields_by_name['group']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Deployments']._options = None
    _QUERY.methods_by_name['Deployments']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta3/deployments/list'
    _QUERY.methods_by_name['Deployment']._options = None
    _QUERY.methods_by_name['Deployment']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/akash/deployment/v1beta3/deployments/info'
    _QUERY.methods_by_name['Group']._options = None
    _QUERY.methods_by_name['Group']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/akash/deployment/v1beta3/groups/info"
    _globals['_QUERYDEPLOYMENTSREQUEST']._serialized_start = 318
    _globals['_QUERYDEPLOYMENTSREQUEST']._serialized_end = 471
    _globals['_QUERYDEPLOYMENTSRESPONSE']._serialized_start = 474
    _globals['_QUERYDEPLOYMENTSRESPONSE']._serialized_end = 662
    _globals['_QUERYDEPLOYMENTREQUEST']._serialized_start = 664
    _globals['_QUERYDEPLOYMENTREQUEST']._serialized_end = 752
    _globals['_QUERYDEPLOYMENTRESPONSE']._serialized_start = 755
    _globals['_QUERYDEPLOYMENTRESPONSE']._serialized_end = 1028
    _globals['_QUERYGROUPREQUEST']._serialized_start = 1030
    _globals['_QUERYGROUPREQUEST']._serialized_end = 1108
    _globals['_QUERYGROUPRESPONSE']._serialized_start = 1110
    _globals['_QUERYGROUPRESPONSE']._serialized_end = 1184
    _globals['_QUERY']._serialized_start = 1187
    _globals['_QUERY']._serialized_end = 1681