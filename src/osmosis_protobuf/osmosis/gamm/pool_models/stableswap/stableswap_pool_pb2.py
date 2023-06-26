"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9osmosis/gamm/pool-models/stableswap/stableswap_pool.proto\x12*osmosis.gamm.poolmodels.stableswap.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xb4\x01\n\nPoolParams\x12R\n\x07swapFee\x18\x01 \x01(\tBA\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"\x12R\n\x07exitFee\x18\x02 \x01(\tBA\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"exit_fee""\xb4\x04\n\x04Pool\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\n\n\x02id\x18\x02 \x01(\x04\x12q\n\npoolParams\x18\x03 \x01(\x0b26.osmosis.gamm.poolmodels.stableswap.v1beta1.PoolParamsB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"stableswap_pool_params"\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor"\x12K\n\x0btotalShares\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"total_shares"\x12b\n\rpoolLiquidity\x18\x06 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12@\n\x0escaling_factor\x18\x07 \x03(\x04B(\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"stableswap_scaling_factor"\x12C\n\x17scaling_factor_governor\x18\x08 \x01(\tB"\xf2\xde\x1f\x1eyaml:"scaling_factor_governor":\x11\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolIBBZ@github.com/osmosis-labs/osmosis/v9/x/gamm/pool-models/stableswapb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.pool_models.stableswap.stableswap_pool_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z@github.com/osmosis-labs/osmosis/v9/x/gamm/pool-models/stableswap'
    _POOLPARAMS.fields_by_name['swapFee']._options = None
    _POOLPARAMS.fields_by_name['swapFee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"swap_fee"'
    _POOLPARAMS.fields_by_name['exitFee']._options = None
    _POOLPARAMS.fields_by_name['exitFee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\x0fyaml:"exit_fee"'
    _POOL.fields_by_name['address']._options = None
    _POOL.fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _POOL.fields_by_name['poolParams']._options = None
    _POOL.fields_by_name['poolParams']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"stableswap_pool_params"'
    _POOL.fields_by_name['future_pool_governor']._options = None
    _POOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _POOL.fields_by_name['totalShares']._options = None
    _POOL.fields_by_name['totalShares']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"total_shares"'
    _POOL.fields_by_name['poolLiquidity']._options = None
    _POOL.fields_by_name['poolLiquidity']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _POOL.fields_by_name['scaling_factor']._options = None
    _POOL.fields_by_name['scaling_factor']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f yaml:"stableswap_scaling_factor"'
    _POOL.fields_by_name['scaling_factor_governor']._options = None
    _POOL.fields_by_name['scaling_factor_governor']._serialized_options = b'\xf2\xde\x1f\x1eyaml:"scaling_factor_governor"'
    _POOL._options = None
    _POOL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolI'
    _globals['_POOLPARAMS']._serialized_start = 284
    _globals['_POOLPARAMS']._serialized_end = 464
    _globals['_POOL']._serialized_start = 467
    _globals['_POOL']._serialized_end = 1031