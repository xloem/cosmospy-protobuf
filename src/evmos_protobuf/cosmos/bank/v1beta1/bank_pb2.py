"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ecosmos/bank/v1beta1/bank.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x17cosmos/msg/v1/msg.proto"d\n\x06Params\x126\n\x0csend_enabled\x18\x01 \x03(\x0b2 .cosmos.bank.v1beta1.SendEnabled\x12\x1c\n\x14default_send_enabled\x18\x02 \x01(\x08:\x04\x98\xa0\x1f\x00"7\n\x0bSendEnabled\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x0f\n\x07enabled\x18\x02 \x01(\x08:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\xa4\x01\n\x05Input\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x14\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x07address"\x99\x01\n\x06Output\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb0\x01\n\x06Supply\x12Z\n\x05total\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:J\x18\x01\x88\xa0\x1f\x00\xe8\xa0\x1f\x01\xca\xb4-<*github.com/cosmos/cosmos-sdk/x/bank/migrations/v040.SupplyI"=\n\tDenomUnit\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08exponent\x18\x02 \x01(\r\x12\x0f\n\x07aliases\x18\x03 \x03(\t"\xc6\x01\n\x08Metadata\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x123\n\x0bdenom_units\x18\x02 \x03(\x0b2\x1e.cosmos.bank.v1beta1.DenomUnit\x12\x0c\n\x04base\x18\x03 \x01(\t\x12\x0f\n\x07display\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06symbol\x18\x06 \x01(\t\x12\x14\n\x03uri\x18\x07 \x01(\tB\x07\xe2\xde\x1f\x03URI\x12\x1d\n\x08uri_hash\x18\x08 \x01(\tB\x0b\xe2\xde\x1f\x07URIHashB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.bank_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _PARAMS._options = None
    _PARAMS._serialized_options = b'\x98\xa0\x1f\x00'
    _SENDENABLED._options = None
    _SENDENABLED._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _INPUT.fields_by_name['address']._options = None
    _INPUT.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _INPUT.fields_by_name['coins']._options = None
    _INPUT.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _INPUT._options = None
    _INPUT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x07address'
    _OUTPUT.fields_by_name['address']._options = None
    _OUTPUT.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _OUTPUT.fields_by_name['coins']._options = None
    _OUTPUT.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _OUTPUT._options = None
    _OUTPUT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _SUPPLY.fields_by_name['total']._options = None
    _SUPPLY.fields_by_name['total']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _SUPPLY._options = None
    _SUPPLY._serialized_options = b'\x18\x01\x88\xa0\x1f\x00\xe8\xa0\x1f\x01\xca\xb4-<*github.com/cosmos/cosmos-sdk/x/bank/migrations/v040.SupplyI'
    _METADATA.fields_by_name['uri']._options = None
    _METADATA.fields_by_name['uri']._serialized_options = b'\xe2\xde\x1f\x03URI'
    _METADATA.fields_by_name['uri_hash']._options = None
    _METADATA.fields_by_name['uri_hash']._serialized_options = b'\xe2\xde\x1f\x07URIHash'
    _globals['_PARAMS']._serialized_start = 161
    _globals['_PARAMS']._serialized_end = 261
    _globals['_SENDENABLED']._serialized_start = 263
    _globals['_SENDENABLED']._serialized_end = 318
    _globals['_INPUT']._serialized_start = 321
    _globals['_INPUT']._serialized_end = 485
    _globals['_OUTPUT']._serialized_start = 488
    _globals['_OUTPUT']._serialized_end = 641
    _globals['_SUPPLY']._serialized_start = 644
    _globals['_SUPPLY']._serialized_end = 820
    _globals['_DENOMUNIT']._serialized_start = 822
    _globals['_DENOMUNIT']._serialized_end = 883
    _globals['_METADATA']._serialized_start = 886
    _globals['_METADATA']._serialized_end = 1084