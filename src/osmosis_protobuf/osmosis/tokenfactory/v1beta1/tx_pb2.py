"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/tokenfactory/v1beta1/tx.proto\x12\x1cosmosis.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"Z\n\x0eMsgCreateDenom\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12%\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"subdenom""M\n\x16MsgCreateDenomResponse\x123\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"new_token_denom""n\n\x07MsgMint\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount""\x11\n\x0fMsgMintResponse"n\n\x07MsgBurn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12@\n\x06amount\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount""\x11\n\x0fMsgBurnResponse"|\n\x0eMsgChangeAdmin\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1f\n\x05denom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom"\x12&\n\x08newAdmin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"new_admin""\x18\n\x16MsgChangeAdminResponse2\xa7\x03\n\x03Msg\x12q\n\x0bCreateDenom\x12,.osmosis.tokenfactory.v1beta1.MsgCreateDenom\x1a4.osmosis.tokenfactory.v1beta1.MsgCreateDenomResponse\x12\\\n\x04Mint\x12%.osmosis.tokenfactory.v1beta1.MsgMint\x1a-.osmosis.tokenfactory.v1beta1.MsgMintResponse\x12\\\n\x04Burn\x12%.osmosis.tokenfactory.v1beta1.MsgBurn\x1a-.osmosis.tokenfactory.v1beta1.MsgBurnResponse\x12q\n\x0bChangeAdmin\x12,.osmosis.tokenfactory.v1beta1.MsgChangeAdmin\x1a4.osmosis.tokenfactory.v1beta1.MsgChangeAdminResponseB9Z7github.com/osmosis-labs/osmosis/v9/x/tokenfactory/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.tokenfactory.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v9/x/tokenfactory/types'
    _MSGCREATEDENOM.fields_by_name['sender']._options = None
    _MSGCREATEDENOM.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEDENOM.fields_by_name['subdenom']._options = None
    _MSGCREATEDENOM.fields_by_name['subdenom']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"subdenom"'
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._options = None
    _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"new_token_denom"'
    _MSGMINT.fields_by_name['sender']._options = None
    _MSGMINT.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGMINT.fields_by_name['amount']._options = None
    _MSGMINT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount"'
    _MSGBURN.fields_by_name['sender']._options = None
    _MSGBURN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGBURN.fields_by_name['amount']._options = None
    _MSGBURN.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"amount"'
    _MSGCHANGEADMIN.fields_by_name['sender']._options = None
    _MSGCHANGEADMIN.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCHANGEADMIN.fields_by_name['denom']._options = None
    _MSGCHANGEADMIN.fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _MSGCHANGEADMIN.fields_by_name['newAdmin']._options = None
    _MSGCHANGEADMIN.fields_by_name['newAdmin']._serialized_options = b'\xf2\xde\x1f\x10yaml:"new_admin"'
    _globals['_MSGCREATEDENOM']._serialized_start = 125
    _globals['_MSGCREATEDENOM']._serialized_end = 215
    _globals['_MSGCREATEDENOMRESPONSE']._serialized_start = 217
    _globals['_MSGCREATEDENOMRESPONSE']._serialized_end = 294
    _globals['_MSGMINT']._serialized_start = 296
    _globals['_MSGMINT']._serialized_end = 406
    _globals['_MSGMINTRESPONSE']._serialized_start = 408
    _globals['_MSGMINTRESPONSE']._serialized_end = 425
    _globals['_MSGBURN']._serialized_start = 427
    _globals['_MSGBURN']._serialized_end = 537
    _globals['_MSGBURNRESPONSE']._serialized_start = 539
    _globals['_MSGBURNRESPONSE']._serialized_end = 556
    _globals['_MSGCHANGEADMIN']._serialized_start = 558
    _globals['_MSGCHANGEADMIN']._serialized_end = 682
    _globals['_MSGCHANGEADMINRESPONSE']._serialized_start = 684
    _globals['_MSGCHANGEADMINRESPONSE']._serialized_end = 708
    _globals['_MSG']._serialized_start = 711
    _globals['_MSG']._serialized_end = 1134