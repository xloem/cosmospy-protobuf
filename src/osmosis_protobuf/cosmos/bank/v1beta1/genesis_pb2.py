"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!cosmos/bank/v1beta1/genesis.proto\x12\x13cosmos.bank.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto"\xaa\x02\n\x0cGenesisState\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x124\n\x08balances\x18\x02 \x03(\x0b2\x1c.cosmos.bank.v1beta1.BalanceB\x04\xc8\xde\x1f\x00\x12[\n\x06supply\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12T\n\x0edenom_metadata\x18\x04 \x03(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"denom_metadata""\x80\x01\n\x07Balance\x12\x0f\n\x07address\x18\x01 \x01(\t\x12Z\n\x05coins\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00B+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['balances']._options = None
    _GENESISSTATE.fields_by_name['balances']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['supply']._options = None
    _GENESISSTATE.fields_by_name['supply']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _GENESISSTATE.fields_by_name['denom_metadata']._options = None
    _GENESISSTATE.fields_by_name['denom_metadata']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"denom_metadata"'
    _BALANCE.fields_by_name['coins']._options = None
    _BALANCE.fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _BALANCE._options = None
    _BALANCE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 145
    _globals['_GENESISSTATE']._serialized_end = 443
    _globals['_BALANCE']._serialized_start = 446
    _globals['_BALANCE']._serialized_end = 574