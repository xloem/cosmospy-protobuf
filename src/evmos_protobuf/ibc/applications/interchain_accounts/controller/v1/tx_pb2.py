"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......ibc.applications.interchain_accounts.v1 import packet_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_v1_dot_packet__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;ibc/applications/interchain_accounts/controller/v1/tx.proto\x122ibc.applications.interchain_accounts.controller.v1\x1a\x14gogoproto/gogo.proto\x1a4ibc/applications/interchain_accounts/v1/packet.proto"y\n\x1cMsgRegisterInterchainAccount\x12\r\n\x05owner\x18\x01 \x01(\t\x12/\n\rconnection_id\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12\x0f\n\x07version\x18\x03 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"Q\n$MsgRegisterInterchainAccountResponse\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""\x83\x02\n\tMsgSendTx\x12\r\n\x05owner\x18\x01 \x01(\t\x12/\n\rconnection_id\x18\x02 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"connection_id"\x12u\n\x0bpacket_data\x18\x03 \x01(\x0b2D.ibc.applications.interchain_accounts.v1.InterchainAccountPacketDataB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_data"\x125\n\x10relative_timeout\x18\x04 \x01(\x04B\x1b\xf2\xde\x1f\x17yaml:"relative_timeout":\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"%\n\x11MsgSendTxResponse\x12\x10\n\x08sequence\x18\x01 \x01(\x042\xe0\x02\n\x03Msg\x12\xc7\x01\n\x19RegisterInterchainAccount\x12P.ibc.applications.interchain_accounts.controller.v1.MsgRegisterInterchainAccount\x1aX.ibc.applications.interchain_accounts.controller.v1.MsgRegisterInterchainAccountResponse\x12\x8e\x01\n\x06SendTx\x12=.ibc.applications.interchain_accounts.controller.v1.MsgSendTx\x1aE.ibc.applications.interchain_accounts.controller.v1.MsgSendTxResponseBRZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.controller.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZPgithub.com/cosmos/ibc-go/v6/modules/apps/27-interchain-accounts/controller/types'
    _MSGREGISTERINTERCHAINACCOUNT.fields_by_name['connection_id']._options = None
    _MSGREGISTERINTERCHAINACCOUNT.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _MSGREGISTERINTERCHAINACCOUNT._options = None
    _MSGREGISTERINTERCHAINACCOUNT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGREGISTERINTERCHAINACCOUNTRESPONSE.fields_by_name['channel_id']._options = None
    _MSGREGISTERINTERCHAINACCOUNTRESPONSE.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _MSGSENDTX.fields_by_name['connection_id']._options = None
    _MSGSENDTX.fields_by_name['connection_id']._serialized_options = b'\xf2\xde\x1f\x14yaml:"connection_id"'
    _MSGSENDTX.fields_by_name['packet_data']._options = None
    _MSGSENDTX.fields_by_name['packet_data']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_data"'
    _MSGSENDTX.fields_by_name['relative_timeout']._options = None
    _MSGSENDTX.fields_by_name['relative_timeout']._serialized_options = b'\xf2\xde\x1f\x17yaml:"relative_timeout"'
    _MSGSENDTX._options = None
    _MSGSENDTX._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_MSGREGISTERINTERCHAINACCOUNT']._serialized_start = 191
    _globals['_MSGREGISTERINTERCHAINACCOUNT']._serialized_end = 312
    _globals['_MSGREGISTERINTERCHAINACCOUNTRESPONSE']._serialized_start = 314
    _globals['_MSGREGISTERINTERCHAINACCOUNTRESPONSE']._serialized_end = 395
    _globals['_MSGSENDTX']._serialized_start = 398
    _globals['_MSGSENDTX']._serialized_end = 657
    _globals['_MSGSENDTXRESPONSE']._serialized_start = 659
    _globals['_MSGSENDTXRESPONSE']._serialized_end = 696
    _globals['_MSG']._serialized_start = 699
    _globals['_MSG']._serialized_end = 1051