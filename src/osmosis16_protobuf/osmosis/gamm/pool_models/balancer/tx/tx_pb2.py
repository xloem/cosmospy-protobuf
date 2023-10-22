"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......amino import amino_pb2 as amino_dot_amino__pb2
from ......osmosis.gamm.pool_models.balancer import balancerPool_pb2 as osmosis_dot_gamm_dot_pool__models_dot_balancer_dot_balancerPool__pb2
from ......cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-osmosis/gamm/pool-models/balancer/tx/tx.proto\x12(osmosis.gamm.poolmodels.balancer.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x11amino/amino.proto\x1a4osmosis/gamm/pool-models/balancer/balancerPool.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xac\x02\n\x15MsgCreateBalancerPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12M\n\x0bpool_params\x18\x02 \x01(\x0b2 .osmosis.gamm.v1beta1.PoolParamsB\x16\xf2\xde\x1f\x12yaml:"pool_params"\x12:\n\x0bpool_assets\x18\x03 \x03(\x0b2\x1f.osmosis.gamm.v1beta1.PoolAssetB\x04\xc8\xde\x1f\x00\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor":&\x8a\xe7\xb0*!osmosis/gamm/create-balancer-pool"<\n\x1dMsgCreateBalancerPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID2\xa6\x01\n\x03Msg\x12\x9e\x01\n\x12CreateBalancerPool\x12?.osmosis.gamm.poolmodels.balancer.v1beta1.MsgCreateBalancerPool\x1aG.osmosis.gamm.poolmodels.balancer.v1beta1.MsgCreateBalancerPoolResponseBAZ?github.com/osmosis-labs/osmosis/v16/x/gamm/pool-models/balancerb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.pool_models.balancer.tx.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z?github.com/osmosis-labs/osmosis/v16/x/gamm/pool-models/balancer'
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_params']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_params']._serialized_options = b'\xf2\xde\x1f\x12yaml:"pool_params"'
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_assets']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['pool_assets']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._options = None
    _MSGCREATEBALANCERPOOL.fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _MSGCREATEBALANCERPOOL._options = None
    _MSGCREATEBALANCERPOOL._serialized_options = b'\x8a\xe7\xb0*!osmosis/gamm/create-balancer-pool'
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._options = None
    _MSGCREATEBALANCERPOOLRESPONSE.fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _globals['_MSGCREATEBALANCERPOOL']._serialized_start = 252
    _globals['_MSGCREATEBALANCERPOOL']._serialized_end = 552
    _globals['_MSGCREATEBALANCERPOOLRESPONSE']._serialized_start = 554
    _globals['_MSGCREATEBALANCERPOOLRESPONSE']._serialized_end = 614
    _globals['_MSG']._serialized_start = 617
    _globals['_MSG']._serialized_end = 783