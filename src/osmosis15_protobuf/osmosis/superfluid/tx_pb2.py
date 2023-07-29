"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bosmosis/superfluid/tx.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a#osmosis/superfluid/superfluid.proto"]\n\x15MsgSuperfluidDelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\x12\x10\n\x08val_addr\x18\x03 \x01(\t"\x1f\n\x1dMsgSuperfluidDelegateResponse"M\n\x17MsgSuperfluidUndelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04"!\n\x1fMsgSuperfluidUndelegateResponse"M\n\x17MsgSuperfluidUnbondLock\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04"!\n\x1fMsgSuperfluidUnbondLockResponse"\x98\x01\n$MsgSuperfluidUndelegateAndUnbondLock\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\x12<\n\x04coin\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x13\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:"coin"".\n,MsgSuperfluidUndelegateAndUnbondLockResponse"\xaf\x01\n\x1cMsgLockAndSuperfluidDelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08val_addr\x18\x03 \x01(\t"2\n$MsgLockAndSuperfluidDelegateResponse\x12\n\n\x02ID\x18\x01 \x01(\x04"b\n\x18MsgUnPoolWhitelistedPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12#\n\x07pool_id\x18\x02 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"";\n MsgUnPoolWhitelistedPoolResponse\x12\x17\n\x0fexited_lock_ids\x18\x01 \x03(\x042\x96\x06\n\x03Msg\x12r\n\x12SuperfluidDelegate\x12).osmosis.superfluid.MsgSuperfluidDelegate\x1a1.osmosis.superfluid.MsgSuperfluidDelegateResponse\x12x\n\x14SuperfluidUndelegate\x12+.osmosis.superfluid.MsgSuperfluidUndelegate\x1a3.osmosis.superfluid.MsgSuperfluidUndelegateResponse\x12x\n\x14SuperfluidUnbondLock\x12+.osmosis.superfluid.MsgSuperfluidUnbondLock\x1a3.osmosis.superfluid.MsgSuperfluidUnbondLockResponse\x12\x9f\x01\n!SuperfluidUndelegateAndUnbondLock\x128.osmosis.superfluid.MsgSuperfluidUndelegateAndUnbondLock\x1a@.osmosis.superfluid.MsgSuperfluidUndelegateAndUnbondLockResponse\x12\x87\x01\n\x19LockAndSuperfluidDelegate\x120.osmosis.superfluid.MsgLockAndSuperfluidDelegate\x1a8.osmosis.superfluid.MsgLockAndSuperfluidDelegateResponse\x12{\n\x15UnPoolWhitelistedPool\x12,.osmosis.superfluid.MsgUnPoolWhitelistedPool\x1a4.osmosis.superfluid.MsgUnPoolWhitelistedPoolResponseB8Z6github.com/osmosis-labs/osmosis/v15/x/superfluid/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.superfluid.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v15/x/superfluid/types'
    _MSGSUPERFLUIDDELEGATE.fields_by_name['sender']._options = None
    _MSGSUPERFLUIDDELEGATE.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSUPERFLUIDUNDELEGATE.fields_by_name['sender']._options = None
    _MSGSUPERFLUIDUNDELEGATE.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSUPERFLUIDUNBONDLOCK.fields_by_name['sender']._options = None
    _MSGSUPERFLUIDUNBONDLOCK.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK.fields_by_name['sender']._options = None
    _MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK.fields_by_name['coin']._options = None
    _MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK.fields_by_name['coin']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:"coin"'
    _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['sender']._options = None
    _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['coins']._options = None
    _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['sender']._options = None
    _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['pool_id']._options = None
    _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_MSGSUPERFLUIDDELEGATE']._serialized_start = 174
    _globals['_MSGSUPERFLUIDDELEGATE']._serialized_end = 267
    _globals['_MSGSUPERFLUIDDELEGATERESPONSE']._serialized_start = 269
    _globals['_MSGSUPERFLUIDDELEGATERESPONSE']._serialized_end = 300
    _globals['_MSGSUPERFLUIDUNDELEGATE']._serialized_start = 302
    _globals['_MSGSUPERFLUIDUNDELEGATE']._serialized_end = 379
    _globals['_MSGSUPERFLUIDUNDELEGATERESPONSE']._serialized_start = 381
    _globals['_MSGSUPERFLUIDUNDELEGATERESPONSE']._serialized_end = 414
    _globals['_MSGSUPERFLUIDUNBONDLOCK']._serialized_start = 416
    _globals['_MSGSUPERFLUIDUNBONDLOCK']._serialized_end = 493
    _globals['_MSGSUPERFLUIDUNBONDLOCKRESPONSE']._serialized_start = 495
    _globals['_MSGSUPERFLUIDUNBONDLOCKRESPONSE']._serialized_end = 528
    _globals['_MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK']._serialized_start = 531
    _globals['_MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCK']._serialized_end = 683
    _globals['_MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCKRESPONSE']._serialized_start = 685
    _globals['_MSGSUPERFLUIDUNDELEGATEANDUNBONDLOCKRESPONSE']._serialized_end = 731
    _globals['_MSGLOCKANDSUPERFLUIDDELEGATE']._serialized_start = 734
    _globals['_MSGLOCKANDSUPERFLUIDDELEGATE']._serialized_end = 909
    _globals['_MSGLOCKANDSUPERFLUIDDELEGATERESPONSE']._serialized_start = 911
    _globals['_MSGLOCKANDSUPERFLUIDDELEGATERESPONSE']._serialized_end = 961
    _globals['_MSGUNPOOLWHITELISTEDPOOL']._serialized_start = 963
    _globals['_MSGUNPOOLWHITELISTEDPOOL']._serialized_end = 1061
    _globals['_MSGUNPOOLWHITELISTEDPOOLRESPONSE']._serialized_start = 1063
    _globals['_MSGUNPOOLWHITELISTEDPOOLRESPONSE']._serialized_end = 1122
    _globals['_MSG']._serialized_start = 1125
    _globals['_MSG']._serialized_end = 1915