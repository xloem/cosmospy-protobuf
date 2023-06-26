"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/upgrade/v1beta1/upgrade.proto\x12\x16cosmos.upgrade.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcb\x01\n\x04Plan\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x04time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\n\x18\x01\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\x0c\n\x04info\x18\x04 \x01(\t\x12W\n\x15upgraded_client_state\x18\x05 \x01(\x0b2\x14.google.protobuf.AnyB"\x18\x01\xf2\xde\x1f\x1cyaml:"upgraded_client_state":\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"y\n\x17SoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x120\n\x04plan\x18\x03 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.PlanB\x04\xc8\xde\x1f\x00:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"M\n\x1dCancelSoftwareUpgradeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"8\n\rModuleVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x04:\x08\x98\xa0\x1f\x01\xe8\xa0\x1f\x01B2Z,github.com/cosmos/cosmos-sdk/x/upgrade/types\xc8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.upgrade.v1beta1.upgrade_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types\xc8\xe1\x1e\x00'
    _PLAN.fields_by_name['time']._options = None
    _PLAN.fields_by_name['time']._serialized_options = b'\x18\x01\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _PLAN.fields_by_name['upgraded_client_state']._options = None
    _PLAN.fields_by_name['upgraded_client_state']._serialized_options = b'\x18\x01\xf2\xde\x1f\x1cyaml:"upgraded_client_state"'
    _PLAN._options = None
    _PLAN._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _SOFTWAREUPGRADEPROPOSAL.fields_by_name['plan']._options = None
    _SOFTWAREUPGRADEPROPOSAL.fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _SOFTWAREUPGRADEPROPOSAL._options = None
    _SOFTWAREUPGRADEPROPOSAL._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _CANCELSOFTWAREUPGRADEPROPOSAL._options = None
    _CANCELSOFTWAREUPGRADEPROPOSAL._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _MODULEVERSION._options = None
    _MODULEVERSION._serialized_options = b'\x98\xa0\x1f\x01\xe8\xa0\x1f\x01'
    _globals['_PLAN']._serialized_start = 147
    _globals['_PLAN']._serialized_end = 350
    _globals['_SOFTWAREUPGRADEPROPOSAL']._serialized_start = 352
    _globals['_SOFTWAREUPGRADEPROPOSAL']._serialized_end = 473
    _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._serialized_start = 475
    _globals['_CANCELSOFTWAREUPGRADEPROPOSAL']._serialized_end = 552
    _globals['_MODULEVERSION']._serialized_start = 554
    _globals['_MODULEVERSION']._serialized_end = 610