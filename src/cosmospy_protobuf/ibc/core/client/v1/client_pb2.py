"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/client/v1/client.proto\x12\x12ibc.core.client.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x19cosmos_proto/cosmos.proto"\x85\x01\n\x15IdentifiedClientState\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12C\n\x0cclient_state\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state""\x97\x01\n\x18ConsensusStateWithHeight\x120\n\x06height\x18\x01 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12I\n\x0fconsensus_state\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:"consensus_state""\xa9\x01\n\x15ClientConsensusStates\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12g\n\x10consensus_states\x18\x02 \x03(\x0b2,.ibc.core.client.v1.ConsensusStateWithHeightB\x1f\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"consensus_states""\xd6\x01\n\x14ClientUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x127\n\x11subject_client_id\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"subject_client_id"\x12=\n\x14substitute_client_id\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"substitute_client_id":"\x88\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content"\xea\x01\n\x0fUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x120\n\x04plan\x18\x03 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.PlanB\x04\xc8\xde\x1f\x00\x12U\n\x15upgraded_client_state\x18\x04 \x01(\x0b2\x14.google.protobuf.AnyB \xf2\xde\x1f\x1cyaml:"upgraded_client_state":*\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\xca\xb4-\x1acosmos.gov.v1beta1.Content"|\n\x06Height\x123\n\x0frevision_number\x18\x01 \x01(\x04B\x1a\xf2\xde\x1f\x16yaml:"revision_number"\x123\n\x0frevision_height\x18\x02 \x01(\x04B\x1a\xf2\xde\x1f\x16yaml:"revision_height":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00"=\n\x06Params\x123\n\x0fallowed_clients\x18\x01 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:"allowed_clients"B:Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.client_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/types'
    _IDENTIFIEDCLIENTSTATE.fields_by_name['client_id']._options = None
    _IDENTIFIEDCLIENTSTATE.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _IDENTIFIEDCLIENTSTATE.fields_by_name['client_state']._options = None
    _IDENTIFIEDCLIENTSTATE.fields_by_name['client_state']._serialized_options = b'\xf2\xde\x1f\x13yaml:"client_state"'
    _CONSENSUSSTATEWITHHEIGHT.fields_by_name['height']._options = None
    _CONSENSUSSTATEWITHHEIGHT.fields_by_name['height']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSENSUSSTATEWITHHEIGHT.fields_by_name['consensus_state']._options = None
    _CONSENSUSSTATEWITHHEIGHT.fields_by_name['consensus_state']._serialized_options = b'\xf2\xde\x1f\x16yaml:"consensus_state"'
    _CLIENTCONSENSUSSTATES.fields_by_name['client_id']._options = None
    _CLIENTCONSENSUSSTATES.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _CLIENTCONSENSUSSTATES.fields_by_name['consensus_states']._options = None
    _CLIENTCONSENSUSSTATES.fields_by_name['consensus_states']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"consensus_states"'
    _CLIENTUPDATEPROPOSAL.fields_by_name['subject_client_id']._options = None
    _CLIENTUPDATEPROPOSAL.fields_by_name['subject_client_id']._serialized_options = b'\xf2\xde\x1f\x18yaml:"subject_client_id"'
    _CLIENTUPDATEPROPOSAL.fields_by_name['substitute_client_id']._options = None
    _CLIENTUPDATEPROPOSAL.fields_by_name['substitute_client_id']._serialized_options = b'\xf2\xde\x1f\x1byaml:"substitute_client_id"'
    _CLIENTUPDATEPROPOSAL._options = None
    _CLIENTUPDATEPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _UPGRADEPROPOSAL.fields_by_name['plan']._options = None
    _UPGRADEPROPOSAL.fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _UPGRADEPROPOSAL.fields_by_name['upgraded_client_state']._options = None
    _UPGRADEPROPOSAL.fields_by_name['upgraded_client_state']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"upgraded_client_state"'
    _UPGRADEPROPOSAL._options = None
    _UPGRADEPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01\xca\xb4-\x1acosmos.gov.v1beta1.Content'
    _HEIGHT.fields_by_name['revision_number']._options = None
    _HEIGHT.fields_by_name['revision_number']._serialized_options = b'\xf2\xde\x1f\x16yaml:"revision_number"'
    _HEIGHT.fields_by_name['revision_height']._options = None
    _HEIGHT.fields_by_name['revision_height']._serialized_options = b'\xf2\xde\x1f\x16yaml:"revision_height"'
    _HEIGHT._options = None
    _HEIGHT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _PARAMS.fields_by_name['allowed_clients']._options = None
    _PARAMS.fields_by_name['allowed_clients']._serialized_options = b'\xf2\xde\x1f\x16yaml:"allowed_clients"'
    _globals['_IDENTIFIEDCLIENTSTATE']._serialized_start = 170
    _globals['_IDENTIFIEDCLIENTSTATE']._serialized_end = 303
    _globals['_CONSENSUSSTATEWITHHEIGHT']._serialized_start = 306
    _globals['_CONSENSUSSTATEWITHHEIGHT']._serialized_end = 457
    _globals['_CLIENTCONSENSUSSTATES']._serialized_start = 460
    _globals['_CLIENTCONSENSUSSTATES']._serialized_end = 629
    _globals['_CLIENTUPDATEPROPOSAL']._serialized_start = 632
    _globals['_CLIENTUPDATEPROPOSAL']._serialized_end = 846
    _globals['_UPGRADEPROPOSAL']._serialized_start = 849
    _globals['_UPGRADEPROPOSAL']._serialized_end = 1083
    _globals['_HEIGHT']._serialized_start = 1085
    _globals['_HEIGHT']._serialized_end = 1209
    _globals['_PARAMS']._serialized_start = 1211
    _globals['_PARAMS']._serialized_end = 1272