"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17osmosis/lockup/tx.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19osmosis/lockup/lock.proto"\xec\x01\n\rMsgLockTokens\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12^\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\xea\xde\x1f\x12duration,omitempty\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01\x12Z\n\x05coins\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"#\n\x15MsgLockTokensResponse\x12\n\n\x02ID\x18\x01 \x01(\x04"7\n\x14MsgBeginUnlockingAll\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""K\n\x1cMsgBeginUnlockingAllResponse\x12+\n\x07unlocks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLock"\x9c\x01\n\x11MsgBeginUnlocking\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\n\n\x02ID\x18\x02 \x01(\x04\x12Z\n\x05coins\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"E\n\x19MsgBeginUnlockingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x17\n\x0funlockingLockID\x18\x02 \x01(\x04"\x9e\x01\n\x0fMsgExtendLockup\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\n\n\x02ID\x18\x02 \x01(\x04\x12^\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\xea\xde\x1f\x12duration,omitempty\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01"*\n\x17MsgExtendLockupResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"\x99\x01\n\x0eMsgForceUnlock\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\n\n\x02ID\x18\x02 \x01(\x04\x12Z\n\x05coins\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins")\n\x16MsgForceUnlockResponse\x12\x0f\n\x07success\x18\x01 \x01(\x082\xd3\x03\n\x03Msg\x12R\n\nLockTokens\x12\x1d.osmosis.lockup.MsgLockTokens\x1a%.osmosis.lockup.MsgLockTokensResponse\x12g\n\x11BeginUnlockingAll\x12$.osmosis.lockup.MsgBeginUnlockingAll\x1a,.osmosis.lockup.MsgBeginUnlockingAllResponse\x12^\n\x0eBeginUnlocking\x12!.osmosis.lockup.MsgBeginUnlocking\x1a).osmosis.lockup.MsgBeginUnlockingResponse\x12X\n\x0cExtendLockup\x12\x1f.osmosis.lockup.MsgExtendLockup\x1a\'.osmosis.lockup.MsgExtendLockupResponse\x12U\n\x0bForceUnlock\x12\x1e.osmosis.lockup.MsgForceUnlock\x1a&.osmosis.lockup.MsgForceUnlockResponseB4Z2github.com/osmosis-labs/osmosis/v15/x/lockup/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.lockup.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v15/x/lockup/types'
    _MSGLOCKTOKENS.fields_by_name['owner']._options = None
    _MSGLOCKTOKENS.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGLOCKTOKENS.fields_by_name['duration']._options = None
    _MSGLOCKTOKENS.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x12duration,omitempty\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _MSGLOCKTOKENS.fields_by_name['coins']._options = None
    _MSGLOCKTOKENS.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGBEGINUNLOCKINGALL.fields_by_name['owner']._options = None
    _MSGBEGINUNLOCKINGALL.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGBEGINUNLOCKING.fields_by_name['owner']._options = None
    _MSGBEGINUNLOCKING.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGBEGINUNLOCKING.fields_by_name['coins']._options = None
    _MSGBEGINUNLOCKING.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGEXTENDLOCKUP.fields_by_name['owner']._options = None
    _MSGEXTENDLOCKUP.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGEXTENDLOCKUP.fields_by_name['duration']._options = None
    _MSGEXTENDLOCKUP.fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x12duration,omitempty\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _MSGFORCEUNLOCK.fields_by_name['owner']._options = None
    _MSGFORCEUNLOCK.fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _MSGFORCEUNLOCK.fields_by_name['coins']._options = None
    _MSGFORCEUNLOCK.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGLOCKTOKENS']._serialized_start = 157
    _globals['_MSGLOCKTOKENS']._serialized_end = 393
    _globals['_MSGLOCKTOKENSRESPONSE']._serialized_start = 395
    _globals['_MSGLOCKTOKENSRESPONSE']._serialized_end = 430
    _globals['_MSGBEGINUNLOCKINGALL']._serialized_start = 432
    _globals['_MSGBEGINUNLOCKINGALL']._serialized_end = 487
    _globals['_MSGBEGINUNLOCKINGALLRESPONSE']._serialized_start = 489
    _globals['_MSGBEGINUNLOCKINGALLRESPONSE']._serialized_end = 564
    _globals['_MSGBEGINUNLOCKING']._serialized_start = 567
    _globals['_MSGBEGINUNLOCKING']._serialized_end = 723
    _globals['_MSGBEGINUNLOCKINGRESPONSE']._serialized_start = 725
    _globals['_MSGBEGINUNLOCKINGRESPONSE']._serialized_end = 794
    _globals['_MSGEXTENDLOCKUP']._serialized_start = 797
    _globals['_MSGEXTENDLOCKUP']._serialized_end = 955
    _globals['_MSGEXTENDLOCKUPRESPONSE']._serialized_start = 957
    _globals['_MSGEXTENDLOCKUPRESPONSE']._serialized_end = 999
    _globals['_MSGFORCEUNLOCK']._serialized_start = 1002
    _globals['_MSGFORCEUNLOCK']._serialized_end = 1155
    _globals['_MSGFORCEUNLOCKRESPONSE']._serialized_start = 1157
    _globals['_MSGFORCEUNLOCKRESPONSE']._serialized_end = 1198
    _globals['_MSG']._serialized_start = 1201
    _globals['_MSG']._serialized_end = 1668