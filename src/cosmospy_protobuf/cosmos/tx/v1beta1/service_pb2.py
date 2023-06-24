"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.abci.v1beta1 import abci_pb2 as cosmos_dot_base_dot_abci_dot_v1beta1_dot_abci__pb2
from ....cosmos.tx.v1beta1 import tx_pb2 as cosmos_dot_tx_dot_v1beta1_dot_tx__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from ....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/tx/v1beta1/service.proto\x12\x11cosmos.tx.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#cosmos/base/abci/v1beta1/abci.proto\x1a\x1acosmos/tx/v1beta1/tx.proto\x1a\x14gogoproto/gogo.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto"\x8e\x01\n\x12GetTxsEventRequest\x12\x0e\n\x06events\x18\x01 \x03(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12,\n\x08order_by\x18\x03 \x01(\x0e2\x1a.cosmos.tx.v1beta1.OrderBy"\xb2\x01\n\x13GetTxsEventResponse\x12"\n\x03txs\x18\x01 \x03(\x0b2\x15.cosmos.tx.v1beta1.Tx\x12:\n\x0ctx_responses\x18\x02 \x03(\x0b2$.cosmos.base.abci.v1beta1.TxResponse\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"V\n\x12BroadcastTxRequest\x12\x10\n\x08tx_bytes\x18\x01 \x01(\x0c\x12.\n\x04mode\x18\x02 \x01(\x0e2 .cosmos.tx.v1beta1.BroadcastMode"P\n\x13BroadcastTxResponse\x129\n\x0btx_response\x18\x01 \x01(\x0b2$.cosmos.base.abci.v1beta1.TxResponse"J\n\x0fSimulateRequest\x12%\n\x02tx\x18\x01 \x01(\x0b2\x15.cosmos.tx.v1beta1.TxB\x02\x18\x01\x12\x10\n\x08tx_bytes\x18\x02 \x01(\x0c"y\n\x10SimulateResponse\x123\n\x08gas_info\x18\x01 \x01(\x0b2!.cosmos.base.abci.v1beta1.GasInfo\x120\n\x06result\x18\x02 \x01(\x0b2 .cosmos.base.abci.v1beta1.Result"\x1c\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t"m\n\rGetTxResponse\x12!\n\x02tx\x18\x01 \x01(\x0b2\x15.cosmos.tx.v1beta1.Tx\x129\n\x0btx_response\x18\x02 \x01(\x0b2$.cosmos.base.abci.v1beta1.TxResponse"d\n\x16GetBlockWithTxsRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xcf\x01\n\x17GetBlockWithTxsResponse\x12"\n\x03txs\x18\x01 \x03(\x0b2\x15.cosmos.tx.v1beta1.Tx\x12+\n\x08block_id\x18\x02 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x03 \x01(\x0b2\x17.tendermint.types.Block\x12;\n\npagination\x18\x04 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse*H\n\x07OrderBy\x12\x18\n\x14ORDER_BY_UNSPECIFIED\x10\x00\x12\x10\n\x0cORDER_BY_ASC\x10\x01\x12\x11\n\rORDER_BY_DESC\x10\x02*|\n\rBroadcastMode\x12\x1e\n\x1aBROADCAST_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14BROADCAST_MODE_BLOCK\x10\x01\x12\x17\n\x13BROADCAST_MODE_SYNC\x10\x02\x12\x18\n\x14BROADCAST_MODE_ASYNC\x10\x032\x92\x05\n\x07Service\x12{\n\x08Simulate\x12".cosmos.tx.v1beta1.SimulateRequest\x1a#.cosmos.tx.v1beta1.SimulateResponse"&\x82\xd3\xe4\x93\x02 "\x1b/cosmos/tx/v1beta1/simulate:\x01*\x12q\n\x05GetTx\x12\x1f.cosmos.tx.v1beta1.GetTxRequest\x1a .cosmos.tx.v1beta1.GetTxResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}\x12\x7f\n\x0bBroadcastTx\x12%.cosmos.tx.v1beta1.BroadcastTxRequest\x1a&.cosmos.tx.v1beta1.BroadcastTxResponse"!\x82\xd3\xe4\x93\x02\x1b"\x16/cosmos/tx/v1beta1/txs:\x01*\x12|\n\x0bGetTxsEvent\x12%.cosmos.tx.v1beta1.GetTxsEventRequest\x1a&.cosmos.tx.v1beta1.GetTxsEventResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txs\x12\x97\x01\n\x0fGetBlockWithTxs\x12).cosmos.tx.v1beta1.GetBlockWithTxsRequest\x1a*.cosmos.tx.v1beta1.GetBlockWithTxsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/cosmos/tx/v1beta1/txs/block/{height}B+Z%github.com/cosmos/cosmos-sdk/types/tx\xc0\xe3\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.tx.v1beta1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z%github.com/cosmos/cosmos-sdk/types/tx\xc0\xe3\x1e\x01'
    _SIMULATEREQUEST.fields_by_name['tx']._options = None
    _SIMULATEREQUEST.fields_by_name['tx']._serialized_options = b'\x18\x01'
    _SERVICE.methods_by_name['Simulate']._options = None
    _SERVICE.methods_by_name['Simulate']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/cosmos/tx/v1beta1/simulate:\x01*'
    _SERVICE.methods_by_name['GetTx']._options = None
    _SERVICE.methods_by_name['GetTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/cosmos/tx/v1beta1/txs/{hash}'
    _SERVICE.methods_by_name['BroadcastTx']._options = None
    _SERVICE.methods_by_name['BroadcastTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x16/cosmos/tx/v1beta1/txs:\x01*'
    _SERVICE.methods_by_name['GetTxsEvent']._options = None
    _SERVICE.methods_by_name['GetTxsEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmos/tx/v1beta1/txs'
    _SERVICE.methods_by_name['GetBlockWithTxs']._options = None
    _SERVICE.methods_by_name['GetBlockWithTxs']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/cosmos/tx/v1beta1/txs/block/{height}"
    _globals['_ORDERBY']._serialized_start = 1423
    _globals['_ORDERBY']._serialized_end = 1495
    _globals['_BROADCASTMODE']._serialized_start = 1497
    _globals['_BROADCASTMODE']._serialized_end = 1621
    _globals['_GETTXSEVENTREQUEST']._serialized_start = 276
    _globals['_GETTXSEVENTREQUEST']._serialized_end = 418
    _globals['_GETTXSEVENTRESPONSE']._serialized_start = 421
    _globals['_GETTXSEVENTRESPONSE']._serialized_end = 599
    _globals['_BROADCASTTXREQUEST']._serialized_start = 601
    _globals['_BROADCASTTXREQUEST']._serialized_end = 687
    _globals['_BROADCASTTXRESPONSE']._serialized_start = 689
    _globals['_BROADCASTTXRESPONSE']._serialized_end = 769
    _globals['_SIMULATEREQUEST']._serialized_start = 771
    _globals['_SIMULATEREQUEST']._serialized_end = 845
    _globals['_SIMULATERESPONSE']._serialized_start = 847
    _globals['_SIMULATERESPONSE']._serialized_end = 968
    _globals['_GETTXREQUEST']._serialized_start = 970
    _globals['_GETTXREQUEST']._serialized_end = 998
    _globals['_GETTXRESPONSE']._serialized_start = 1000
    _globals['_GETTXRESPONSE']._serialized_end = 1109
    _globals['_GETBLOCKWITHTXSREQUEST']._serialized_start = 1111
    _globals['_GETBLOCKWITHTXSREQUEST']._serialized_end = 1211
    _globals['_GETBLOCKWITHTXSRESPONSE']._serialized_start = 1214
    _globals['_GETBLOCKWITHTXSRESPONSE']._serialized_end = 1421
    _globals['_SERVICE']._serialized_start = 1624
    _globals['_SERVICE']._serialized_end = 2282