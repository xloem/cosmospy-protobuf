"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.consensus import types_pb2 as tendermint_dot_consensus_dot_types__pb2
from ...tendermint.types import events_pb2 as tendermint_dot_types_dot_events__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etendermint/consensus/wal.proto\x12\x14tendermint.consensus\x1a\x14gogoproto/gogo.proto\x1a tendermint/consensus/types.proto\x1a\x1dtendermint/types/events.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"X\n\x07MsgInfo\x120\n\x03msg\x18\x01 \x01(\x0b2\x1d.tendermint.consensus.MessageB\x04\xc8\xde\x1f\x00\x12\x1b\n\x07peer_id\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06PeerID"q\n\x0bTimeoutInfo\x125\n\x08duration\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\r\n\x05round\x18\x03 \x01(\x05\x12\x0c\n\x04step\x18\x04 \x01(\r"\x1b\n\tEndHeight\x12\x0e\n\x06height\x18\x01 \x01(\x03"\x81\x02\n\nWALMessage\x12G\n\x16event_data_round_state\x18\x01 \x01(\x0b2%.tendermint.types.EventDataRoundStateH\x00\x121\n\x08msg_info\x18\x02 \x01(\x0b2\x1d.tendermint.consensus.MsgInfoH\x00\x129\n\x0ctimeout_info\x18\x03 \x01(\x0b2!.tendermint.consensus.TimeoutInfoH\x00\x125\n\nend_height\x18\x04 \x01(\x0b2\x1f.tendermint.consensus.EndHeightH\x00B\x05\n\x03sum"t\n\x0fTimedWALMessage\x122\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12-\n\x03msg\x18\x02 \x01(\x0b2 .tendermint.consensus.WALMessageB=Z;github.com/tendermint/tendermint/proto/tendermint/consensusb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.consensus.wal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z;github.com/tendermint/tendermint/proto/tendermint/consensus'
    _MSGINFO.fields_by_name['msg']._options = None
    _MSGINFO.fields_by_name['msg']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGINFO.fields_by_name['peer_id']._options = None
    _MSGINFO.fields_by_name['peer_id']._serialized_options = b'\xe2\xde\x1f\x06PeerID'
    _TIMEOUTINFO.fields_by_name['duration']._options = None
    _TIMEOUTINFO.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _TIMEDWALMESSAGE.fields_by_name['time']._options = None
    _TIMEDWALMESSAGE.fields_by_name['time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_MSGINFO']._serialized_start = 208
    _globals['_MSGINFO']._serialized_end = 296
    _globals['_TIMEOUTINFO']._serialized_start = 298
    _globals['_TIMEOUTINFO']._serialized_end = 411
    _globals['_ENDHEIGHT']._serialized_start = 413
    _globals['_ENDHEIGHT']._serialized_end = 440
    _globals['_WALMESSAGE']._serialized_start = 443
    _globals['_WALMESSAGE']._serialized_end = 700
    _globals['_TIMEDWALMESSAGE']._serialized_start = 702
    _globals['_TIMEDWALMESSAGE']._serialized_end = 818