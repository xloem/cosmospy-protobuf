"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.deployment.v1beta3 import groupid_pb2 as akash_dot_deployment_dot_v1beta3_dot_groupid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'akash/deployment/v1beta3/groupmsg.proto\x12\x18akash.deployment.v1beta3\x1a\x14gogoproto/gogo.proto\x1a&akash/deployment/v1beta3/groupid.proto"c\n\rMsgCloseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta3.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgCloseGroupResponse"c\n\rMsgPauseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta3.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgPauseGroupResponse"c\n\rMsgStartGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta3.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgStartGroupResponseB?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta3.groupmsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta3'
    _MSGCLOSEGROUP.fields_by_name['id']._options = None
    _MSGCLOSEGROUP.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGCLOSEGROUP._options = None
    _MSGCLOSEGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGPAUSEGROUP.fields_by_name['id']._options = None
    _MSGPAUSEGROUP.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGPAUSEGROUP._options = None
    _MSGPAUSEGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _MSGSTARTGROUP.fields_by_name['id']._options = None
    _MSGSTARTGROUP.fields_by_name['id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _MSGSTARTGROUP._options = None
    _MSGSTARTGROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_MSGCLOSEGROUP']._serialized_start = 131
    _globals['_MSGCLOSEGROUP']._serialized_end = 230
    _globals['_MSGCLOSEGROUPRESPONSE']._serialized_start = 232
    _globals['_MSGCLOSEGROUPRESPONSE']._serialized_end = 255
    _globals['_MSGPAUSEGROUP']._serialized_start = 257
    _globals['_MSGPAUSEGROUP']._serialized_end = 356
    _globals['_MSGPAUSEGROUPRESPONSE']._serialized_start = 358
    _globals['_MSGPAUSEGROUPRESPONSE']._serialized_end = 381
    _globals['_MSGSTARTGROUP']._serialized_start = 383
    _globals['_MSGSTARTGROUP']._serialized_end = 482
    _globals['_MSGSTARTGROUPRESPONSE']._serialized_start = 484
    _globals['_MSGSTARTGROUPRESPONSE']._serialized_end = 507