"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8osmosis/cosmwasmpool/v1beta1/model/module_sudo_msg.proto\x12\x1cosmosis.cosmwasmpool.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xff\x01\n\x11SwapExactAmountIn\x12\x0e\n\x06sender\x18\x01 \x01(\t\x121\n\x08token_in\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x17\n\x0ftoken_out_denom\x18\x03 \x01(\t\x12L\n\x14token_out_min_amount\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12@\n\x08swap_fee\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"o\n\x18SwapExactAmountInSudoMsg\x12S\n\x14swap_exact_amount_in\x18\x01 \x01(\x0b2/.osmosis.cosmwasmpool.v1beta1.SwapExactAmountInB\x04\xc8\xde\x1f\x00"l\n SwapExactAmountInSudoMsgResponse\x12H\n\x10token_out_amount\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"\xff\x01\n\x12SwapExactAmountOut\x12\x0e\n\x06sender\x18\x01 \x01(\t\x122\n\ttoken_out\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x16\n\x0etoken_in_denom\x18\x03 \x01(\t\x12K\n\x13token_in_max_amount\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12@\n\x08swap_fee\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"r\n\x19SwapExactAmountOutSudoMsg\x12U\n\x15swap_exact_amount_out\x18\x01 \x01(\x0b20.osmosis.cosmwasmpool.v1beta1.SwapExactAmountOutB\x04\xc8\xde\x1f\x00"l\n!SwapExactAmountOutSudoMsgResponse\x12G\n\x0ftoken_in_amount\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.IntBAZ?github.com/osmosis-labs/osmosis/v16/x/cosmwasmpool/cosmwasm/msgb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.cosmwasmpool.v1beta1.model.module_sudo_msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z?github.com/osmosis-labs/osmosis/v16/x/cosmwasmpool/cosmwasm/msg'
    _SWAPEXACTAMOUNTIN.fields_by_name['token_in']._options = None
    _SWAPEXACTAMOUNTIN.fields_by_name['token_in']._serialized_options = b'\xc8\xde\x1f\x00'
    _SWAPEXACTAMOUNTIN.fields_by_name['token_out_min_amount']._options = None
    _SWAPEXACTAMOUNTIN.fields_by_name['token_out_min_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _SWAPEXACTAMOUNTIN.fields_by_name['swap_fee']._options = None
    _SWAPEXACTAMOUNTIN.fields_by_name['swap_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _SWAPEXACTAMOUNTINSUDOMSG.fields_by_name['swap_exact_amount_in']._options = None
    _SWAPEXACTAMOUNTINSUDOMSG.fields_by_name['swap_exact_amount_in']._serialized_options = b'\xc8\xde\x1f\x00'
    _SWAPEXACTAMOUNTINSUDOMSGRESPONSE.fields_by_name['token_out_amount']._options = None
    _SWAPEXACTAMOUNTINSUDOMSGRESPONSE.fields_by_name['token_out_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _SWAPEXACTAMOUNTOUT.fields_by_name['token_out']._options = None
    _SWAPEXACTAMOUNTOUT.fields_by_name['token_out']._serialized_options = b'\xc8\xde\x1f\x00'
    _SWAPEXACTAMOUNTOUT.fields_by_name['token_in_max_amount']._options = None
    _SWAPEXACTAMOUNTOUT.fields_by_name['token_in_max_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _SWAPEXACTAMOUNTOUT.fields_by_name['swap_fee']._options = None
    _SWAPEXACTAMOUNTOUT.fields_by_name['swap_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _SWAPEXACTAMOUNTOUTSUDOMSG.fields_by_name['swap_exact_amount_out']._options = None
    _SWAPEXACTAMOUNTOUTSUDOMSG.fields_by_name['swap_exact_amount_out']._serialized_options = b'\xc8\xde\x1f\x00'
    _SWAPEXACTAMOUNTOUTSUDOMSGRESPONSE.fields_by_name['token_in_amount']._options = None
    _SWAPEXACTAMOUNTOUTSUDOMSGRESPONSE.fields_by_name['token_in_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _globals['_SWAPEXACTAMOUNTIN']._serialized_start = 145
    _globals['_SWAPEXACTAMOUNTIN']._serialized_end = 400
    _globals['_SWAPEXACTAMOUNTINSUDOMSG']._serialized_start = 402
    _globals['_SWAPEXACTAMOUNTINSUDOMSG']._serialized_end = 513
    _globals['_SWAPEXACTAMOUNTINSUDOMSGRESPONSE']._serialized_start = 515
    _globals['_SWAPEXACTAMOUNTINSUDOMSGRESPONSE']._serialized_end = 623
    _globals['_SWAPEXACTAMOUNTOUT']._serialized_start = 626
    _globals['_SWAPEXACTAMOUNTOUT']._serialized_end = 881
    _globals['_SWAPEXACTAMOUNTOUTSUDOMSG']._serialized_start = 883
    _globals['_SWAPEXACTAMOUNTOUTSUDOMSG']._serialized_end = 997
    _globals['_SWAPEXACTAMOUNTOUTSUDOMSGRESPONSE']._serialized_start = 999
    _globals['_SWAPEXACTAMOUNTOUTSUDOMSGRESPONSE']._serialized_end = 1107