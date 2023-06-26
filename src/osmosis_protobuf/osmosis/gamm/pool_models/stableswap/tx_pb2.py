"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....osmosis.gamm.pool_models.stableswap import stableswap_pool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_stableswap_dot_stableswap__pool__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,osmosis/gamm/pool-models/stableswap/tx.proto\x12*osmosis.gamm.poolmodels.stableswap.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a9osmosis/gamm/pool-models/stableswap/stableswap_pool.proto"\xcc\x02\n\x17MsgCreateStableswapPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12b\n\npoolParams\x18\x02 \x01(\x0b26.osmosis.gamm.poolmodels.stableswap.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x12k\n\x16initial_pool_liquidity\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor"">\n\x1fMsgCreateStableswapPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID"\xa6\x01\n!MsgStableSwapAdjustScalingFactors\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12\x1b\n\x07pool_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PoolID\x12A\n\x0fscaling_factors\x18\x03 \x03(\x04B(\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"stableswap_scaling_factor""+\n)MsgStableSwapAdjustScalingFactorsResponse2\xf9\x02\n\x03Msg\x12\xa8\x01\n\x14CreateStableswapPool\x12C.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgCreateStableswapPool\x1aK.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgCreateStableswapPoolResponse\x12\xc6\x01\n\x1eStableSwapAdjustScalingFactors\x12M.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgStableSwapAdjustScalingFactors\x1aU.osmosis.gamm.poolmodels.stableswap.v1beta1.MsgStableSwapAdjustScalingFactorsResponseBBZ@github.com/osmosis-labs/osmosis/v9/x/gamm/pool-models/stableswapb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.pool_models.stableswap.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z@github.com/osmosis-labs/osmosis/v9/x/gamm/pool-models/stableswap'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['poolParams']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['poolParams']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['initial_pool_liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATESTABLESWAPPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATESTABLESWAPPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['sender']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['pool_id']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['scaling_factors']._options = None
    _MSGSTABLESWAPADJUSTSCALINGFACTORS.fields_by_name['scaling_factors']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"stableswap_scaling_factor"'
    _globals['_MSGCREATESTABLESWAPPOOL']._serialized_start = 206
    _globals['_MSGCREATESTABLESWAPPOOL']._serialized_end = 538
    _globals['_MSGCREATESTABLESWAPPOOLRESPONSE']._serialized_start = 540
    _globals['_MSGCREATESTABLESWAPPOOLRESPONSE']._serialized_end = 602
    _globals['_MSGSTABLESWAPADJUSTSCALINGFACTORS']._serialized_start = 605
    _globals['_MSGSTABLESWAPADJUSTSCALINGFACTORS']._serialized_end = 771
    _globals['_MSGSTABLESWAPADJUSTSCALINGFACTORSRESPONSE']._serialized_start = 773
    _globals['_MSGSTABLESWAPADJUSTSCALINGFACTORSRESPONSE']._serialized_end = 816
    _globals['_MSG']._serialized_start = 819
    _globals['_MSG']._serialized_end = 1196