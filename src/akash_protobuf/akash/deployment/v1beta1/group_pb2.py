"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....akash.base.v1beta1 import resource_pb2 as akash_dot_base_dot_v1beta1_dot_resource__pb2
from ....akash.base.v1beta1 import attribute_pb2 as akash_dot_base_dot_v1beta1_dot_attribute__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$akash/deployment/v1beta1/group.proto\x12\x18akash.deployment.v1beta1\x1a\x14gogoproto/gogo.proto\x1a!akash/base/v1beta1/resource.proto\x1a"akash/base/v1beta1/attribute.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"c\n\rMsgCloseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta1.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgCloseGroupResponse"c\n\rMsgPauseGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta1.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgPauseGroupResponse"c\n\rMsgStartGroup\x12L\n\x02id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta1.GroupIDB\x1d\xc8\xde\x1f\x00\xe2\xde\x1f\x02ID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id":\x04\xe8\xa0\x1f\x00"\x17\n\x15MsgStartGroupResponse"\x9b\x01\n\x07GroupID\x12(\n\x05owner\x18\x01 \x01(\tB\x19\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"\x12-\n\x04dseq\x18\x02 \x01(\x04B\x1f\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"\x12-\n\x04gseq\x18\x03 \x01(\rB\x1f\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\x88\x02\n\tGroupSpec\x12%\n\x04name\x18\x01 \x01(\tB\x17\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"\x12l\n\x0crequirements\x18\x02 \x01(\x0b2).akash.base.v1beta1.PlacementRequirementsB+\xc8\xde\x1f\x00\xea\xde\x1f\x0crequirements\xf2\xde\x1f\x13yaml:"requirements"\x12\\\n\tresources\x18\x03 \x03(\x0b2".akash.deployment.v1beta1.ResourceB%\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xdc\x03\n\x05Group\x12W\n\x08group_id\x18\x01 \x01(\x0b2!.akash.deployment.v1beta1.GroupIDB"\xc8\xde\x1f\x00\xe2\xde\x1f\x07GroupID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x12O\n\x05state\x18\x02 \x01(\x0e2%.akash.deployment.v1beta1.Group.StateB\x19\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"\x12T\n\ngroup_spec\x18\x03 \x01(\x0b2#.akash.deployment.v1beta1.GroupSpecB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"\x12\x12\n\ncreated_at\x18\x04 \x01(\x03"\xb8\x01\n\x05State\x12"\n\x07invalid\x10\x00\x1a\x15\x8a\x9d \x11GroupStateInvalid\x12\x17\n\x04open\x10\x01\x1a\r\x8a\x9d \tGroupOpen\x12\x1b\n\x06paused\x10\x02\x1a\x0f\x8a\x9d \x0bGroupPaused\x122\n\x12insufficient_funds\x10\x03\x1a\x1a\x8a\x9d \x16GroupInsufficientFunds\x12\x1b\n\x06closed\x10\x04\x1a\x0f\x8a\x9d \x0bGroupClosed\x1a\x04\x88\xa3\x1e\x00:\x04\xe8\xa0\x1f\x00"\xd6\x01\n\x08Resource\x12Q\n\tresources\x18\x01 \x01(\x0b2!.akash.base.v1beta1.ResourceUnitsB\x1b\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"\x12(\n\x05count\x18\x02 \x01(\rB\x19\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"\x12G\n\x05price\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1d\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price":\x04\xe8\xa0\x1f\x00B?Z=github.com/akash-network/akash-api/go/node/deployment/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.deployment.v1beta1.group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z=github.com/akash-network/akash-api/go/node/deployment/v1beta1'
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
    _GROUPID.fields_by_name['owner']._options = None
    _GROUPID.fields_by_name['owner']._serialized_options = b'\xea\xde\x1f\x05owner\xf2\xde\x1f\x0cyaml:"owner"'
    _GROUPID.fields_by_name['dseq']._options = None
    _GROUPID.fields_by_name['dseq']._serialized_options = b'\xe2\xde\x1f\x04DSeq\xea\xde\x1f\x04dseq\xf2\xde\x1f\x0byaml:"dseq"'
    _GROUPID.fields_by_name['gseq']._options = None
    _GROUPID.fields_by_name['gseq']._serialized_options = b'\xe2\xde\x1f\x04GSeq\xea\xde\x1f\x04gseq\xf2\xde\x1f\x0byaml:"gseq"'
    _GROUPID._options = None
    _GROUPID._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _GROUPSPEC.fields_by_name['name']._options = None
    _GROUPSPEC.fields_by_name['name']._serialized_options = b'\xea\xde\x1f\x04name\xf2\xde\x1f\x0byaml:"name"'
    _GROUPSPEC.fields_by_name['requirements']._options = None
    _GROUPSPEC.fields_by_name['requirements']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x0crequirements\xf2\xde\x1f\x13yaml:"requirements"'
    _GROUPSPEC.fields_by_name['resources']._options = None
    _GROUPSPEC.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\tresources\xf2\xde\x1f\x10yaml:"resources"'
    _GROUPSPEC._options = None
    _GROUPSPEC._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _GROUP_STATE._options = None
    _GROUP_STATE._serialized_options = b'\x88\xa3\x1e\x00'
    _GROUP_STATE.values_by_name['invalid']._options = None
    _GROUP_STATE.values_by_name['invalid']._serialized_options = b'\x8a\x9d \x11GroupStateInvalid'
    _GROUP_STATE.values_by_name['open']._options = None
    _GROUP_STATE.values_by_name['open']._serialized_options = b'\x8a\x9d \tGroupOpen'
    _GROUP_STATE.values_by_name['paused']._options = None
    _GROUP_STATE.values_by_name['paused']._serialized_options = b'\x8a\x9d \x0bGroupPaused'
    _GROUP_STATE.values_by_name['insufficient_funds']._options = None
    _GROUP_STATE.values_by_name['insufficient_funds']._serialized_options = b'\x8a\x9d \x16GroupInsufficientFunds'
    _GROUP_STATE.values_by_name['closed']._options = None
    _GROUP_STATE.values_by_name['closed']._serialized_options = b'\x8a\x9d \x0bGroupClosed'
    _GROUP.fields_by_name['group_id']._options = None
    _GROUP.fields_by_name['group_id']._serialized_options = b'\xc8\xde\x1f\x00\xe2\xde\x1f\x07GroupID\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _GROUP.fields_by_name['state']._options = None
    _GROUP.fields_by_name['state']._serialized_options = b'\xea\xde\x1f\x05state\xf2\xde\x1f\x0cyaml:"state"'
    _GROUP.fields_by_name['group_spec']._options = None
    _GROUP.fields_by_name['group_spec']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04spec\xf2\xde\x1f\x0byaml:"spec"'
    _GROUP._options = None
    _GROUP._serialized_options = b'\xe8\xa0\x1f\x00'
    _RESOURCE.fields_by_name['resources']._options = None
    _RESOURCE.fields_by_name['resources']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x04unit\xf2\xde\x1f\x0byaml:"unit"'
    _RESOURCE.fields_by_name['count']._options = None
    _RESOURCE.fields_by_name['count']._serialized_options = b'\xea\xde\x1f\x05count\xf2\xde\x1f\x0cyaml:"count"'
    _RESOURCE.fields_by_name['price']._options = None
    _RESOURCE.fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x05price\xf2\xde\x1f\x0cyaml:"price"'
    _RESOURCE._options = None
    _RESOURCE._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_MSGCLOSEGROUP']._serialized_start = 191
    _globals['_MSGCLOSEGROUP']._serialized_end = 290
    _globals['_MSGCLOSEGROUPRESPONSE']._serialized_start = 292
    _globals['_MSGCLOSEGROUPRESPONSE']._serialized_end = 315
    _globals['_MSGPAUSEGROUP']._serialized_start = 317
    _globals['_MSGPAUSEGROUP']._serialized_end = 416
    _globals['_MSGPAUSEGROUPRESPONSE']._serialized_start = 418
    _globals['_MSGPAUSEGROUPRESPONSE']._serialized_end = 441
    _globals['_MSGSTARTGROUP']._serialized_start = 443
    _globals['_MSGSTARTGROUP']._serialized_end = 542
    _globals['_MSGSTARTGROUPRESPONSE']._serialized_start = 544
    _globals['_MSGSTARTGROUPRESPONSE']._serialized_end = 567
    _globals['_GROUPID']._serialized_start = 570
    _globals['_GROUPID']._serialized_end = 725
    _globals['_GROUPSPEC']._serialized_start = 728
    _globals['_GROUPSPEC']._serialized_end = 992
    _globals['_GROUP']._serialized_start = 995
    _globals['_GROUP']._serialized_end = 1471
    _globals['_GROUP_STATE']._serialized_start = 1281
    _globals['_GROUP_STATE']._serialized_end = 1465
    _globals['_RESOURCE']._serialized_start = 1474
    _globals['_RESOURCE']._serialized_end = 1688