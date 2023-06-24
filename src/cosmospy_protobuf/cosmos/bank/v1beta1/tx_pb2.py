"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/bank/v1beta1/tx.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto"\xca\x01\n\x07MsgSend\x12-\n\x0cfrom_address\x18\x01 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"from_address"\x12)\n\nto_address\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"to_address"\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x11\n\x0fMsgSendResponse"z\n\x0cMsgMultiSend\x120\n\x06inputs\x18\x01 \x03(\x0b2\x1a.cosmos.bank.v1beta1.InputB\x04\xc8\xde\x1f\x00\x122\n\x07outputs\x18\x02 \x03(\x0b2\x1b.cosmos.bank.v1beta1.OutputB\x04\xc8\xde\x1f\x00:\x04\xe8\xa0\x1f\x00"\x16\n\x14MsgMultiSendResponse2\xac\x01\n\x03Msg\x12J\n\x04Send\x12\x1c.cosmos.bank.v1beta1.MsgSend\x1a$.cosmos.bank.v1beta1.MsgSendResponse\x12Y\n\tMultiSend\x12!.cosmos.bank.v1beta1.MsgMultiSend\x1a).cosmos.bank.v1beta1.MsgMultiSendResponseB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _MSGSEND.fields_by_name['from_address']._options = None
    _MSGSEND.fields_by_name['from_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"from_address"'
    _MSGSEND.fields_by_name['to_address']._options = None
    _MSGSEND.fields_by_name['to_address']._serialized_options = b'\xf2\xde\x1f\x11yaml:"to_address"'
    _MSGSEND.fields_by_name['amount']._options = None
    _MSGSEND.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGSEND._options = None
    _MSGSEND._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGMULTISEND.fields_by_name['inputs']._options = None
    _MSGMULTISEND.fields_by_name['inputs']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGMULTISEND.fields_by_name['outputs']._options = None
    _MSGMULTISEND.fields_by_name['outputs']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGMULTISEND._options = None
    _MSGMULTISEND._serialized_options = b'\xe8\xa0\x1f\x00'
    _globals['_MSGSEND']._serialized_start = 140
    _globals['_MSGSEND']._serialized_end = 342
    _globals['_MSGSENDRESPONSE']._serialized_start = 344
    _globals['_MSGSENDRESPONSE']._serialized_end = 361
    _globals['_MSGMULTISEND']._serialized_start = 363
    _globals['_MSGMULTISEND']._serialized_end = 485
    _globals['_MSGMULTISENDRESPONSE']._serialized_start = 487
    _globals['_MSGMULTISENDRESPONSE']._serialized_end = 509
    _globals['_MSG']._serialized_start = 512
    _globals['_MSG']._serialized_end = 684