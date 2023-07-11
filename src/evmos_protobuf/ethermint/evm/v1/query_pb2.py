"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....ethermint.evm.v1 import evm_pb2 as ethermint_dot_evm_dot_v1_dot_evm__pb2
from ....ethermint.evm.v1 import tx_pb2 as ethermint_dot_evm_dot_v1_dot_tx__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cethermint/evm/v1/query.proto\x12\x10ethermint.evm.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1aethermint/evm/v1/evm.proto\x1a\x19ethermint/evm/v1/tx.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"0\n\x13QueryAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"I\n\x14QueryAccountResponse\x12\x0f\n\x07balance\x18\x01 \x01(\t\x12\x11\n\tcode_hash\x18\x02 \x01(\t\x12\r\n\x05nonce\x18\x03 \x01(\x04"6\n\x19QueryCosmosAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"^\n\x1aQueryCosmosAccountResponse\x12\x16\n\x0ecosmos_address\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x16\n\x0eaccount_number\x18\x03 \x01(\x04">\n\x1cQueryValidatorAccountRequest\x12\x14\n\x0ccons_address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"b\n\x1dQueryValidatorAccountResponse\x12\x17\n\x0faccount_address\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x16\n\x0eaccount_number\x18\x03 \x01(\x04"0\n\x13QueryBalanceRequest\x12\x0f\n\x07address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\'\n\x14QueryBalanceResponse\x12\x0f\n\x07balance\x18\x01 \x01(\t"=\n\x13QueryStorageRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"%\n\x14QueryStorageResponse\x12\r\n\x05value\x18\x01 \x01(\t"-\n\x10QueryCodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"!\n\x11QueryCodeResponse\x12\x0c\n\x04code\x18\x01 \x01(\x0c"h\n\x12QueryTxLogsRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"w\n\x13QueryTxLogsResponse\x12#\n\x04logs\x18\x01 \x03(\x0b2\x15.ethermint.evm.v1.Log\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x14\n\x12QueryParamsRequest"E\n\x13QueryParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b2\x18.ethermint.evm.v1.ParamsB\x04\xc8\xde\x1f\x00"\x8f\x01\n\x0eEthCallRequest\x12\x0c\n\x04args\x18\x01 \x01(\x0c\x12\x0f\n\x07gas_cap\x18\x02 \x01(\x04\x12L\n\x10proposer_address\x18\x03 \x01(\x0cB2\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress\x12\x10\n\x08chain_id\x18\x04 \x01(\x03""\n\x13EstimateGasResponse\x12\x0b\n\x03gas\x18\x01 \x01(\x04"\x83\x03\n\x13QueryTraceTxRequest\x12,\n\x03msg\x18\x01 \x01(\x0b2\x1f.ethermint.evm.v1.MsgEthereumTx\x123\n\x0ctrace_config\x18\x03 \x01(\x0b2\x1d.ethermint.evm.v1.TraceConfig\x125\n\x0cpredecessors\x18\x04 \x03(\x0b2\x1f.ethermint.evm.v1.MsgEthereumTx\x12\x14\n\x0cblock_number\x18\x05 \x01(\x03\x12\x12\n\nblock_hash\x18\x06 \x01(\t\x128\n\nblock_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12L\n\x10proposer_address\x18\x08 \x01(\x0cB2\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress\x12\x10\n\x08chain_id\x18\t \x01(\x03J\x04\x08\x02\x10\x03R\x08tx_index"$\n\x14QueryTraceTxResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c"\xbf\x02\n\x16QueryTraceBlockRequest\x12,\n\x03txs\x18\x01 \x03(\x0b2\x1f.ethermint.evm.v1.MsgEthereumTx\x123\n\x0ctrace_config\x18\x03 \x01(\x0b2\x1d.ethermint.evm.v1.TraceConfig\x12\x14\n\x0cblock_number\x18\x05 \x01(\x03\x12\x12\n\nblock_hash\x18\x06 \x01(\t\x128\n\nblock_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12L\n\x10proposer_address\x18\x08 \x01(\x0cB2\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress\x12\x10\n\x08chain_id\x18\t \x01(\x03"\'\n\x17QueryTraceBlockResponse\x12\x0c\n\x04data\x18\x01 \x01(\x0c"\x15\n\x13QueryBaseFeeRequest"T\n\x14QueryBaseFeeResponse\x12<\n\x08base_fee\x18\x01 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int2\xbf\x0c\n\x05Query\x12\x81\x01\n\x07Account\x12%.ethermint.evm.v1.QueryAccountRequest\x1a&.ethermint.evm.v1.QueryAccountResponse"\'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/evm/v1/account/{address}\x12\x9a\x01\n\rCosmosAccount\x12+.ethermint.evm.v1.QueryCosmosAccountRequest\x1a,.ethermint.evm.v1.QueryCosmosAccountResponse".\x82\xd3\xe4\x93\x02(\x12&/evmos/evm/v1/cosmos_account/{address}\x12\xab\x01\n\x10ValidatorAccount\x12..ethermint.evm.v1.QueryValidatorAccountRequest\x1a/.ethermint.evm.v1.QueryValidatorAccountResponse"6\x82\xd3\xe4\x93\x020\x12./evmos/evm/v1/validator_account/{cons_address}\x12\x82\x01\n\x07Balance\x12%.ethermint.evm.v1.QueryBalanceRequest\x1a&.ethermint.evm.v1.QueryBalanceResponse"(\x82\xd3\xe4\x93\x02"\x12 /evmos/evm/v1/balances/{address}\x12\x87\x01\n\x07Storage\x12%.ethermint.evm.v1.QueryStorageRequest\x1a&.ethermint.evm.v1.QueryStorageResponse"-\x82\xd3\xe4\x93\x02\'\x12%/evmos/evm/v1/storage/{address}/{key}\x12v\n\x04Code\x12".ethermint.evm.v1.QueryCodeRequest\x1a#.ethermint.evm.v1.QueryCodeResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/evmos/evm/v1/codes/{address}\x12s\n\x06Params\x12$.ethermint.evm.v1.QueryParamsRequest\x1a%.ethermint.evm.v1.QueryParamsResponse"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/evmos/evm/v1/params\x12t\n\x07EthCall\x12 .ethermint.evm.v1.EthCallRequest\x1a\'.ethermint.evm.v1.MsgEthereumTxResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/eth_call\x12z\n\x0bEstimateGas\x12 .ethermint.evm.v1.EthCallRequest\x1a%.ethermint.evm.v1.EstimateGasResponse""\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/evm/v1/estimate_gas\x12x\n\x07TraceTx\x12%.ethermint.evm.v1.QueryTraceTxRequest\x1a&.ethermint.evm.v1.QueryTraceTxResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/trace_tx\x12\x84\x01\n\nTraceBlock\x12(.ethermint.evm.v1.QueryTraceBlockRequest\x1a).ethermint.evm.v1.QueryTraceBlockResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/evmos/evm/v1/trace_block\x12x\n\x07BaseFee\x12%.ethermint.evm.v1.QueryBaseFeeRequest\x1a&.ethermint.evm.v1.QueryBaseFeeResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/base_feeB(Z&github.com/evmos/evmos/v13/x/evm/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/evmos/evmos/v13/x/evm/types'
    _QUERYACCOUNTREQUEST._options = None
    _QUERYACCOUNTREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYCOSMOSACCOUNTREQUEST._options = None
    _QUERYCOSMOSACCOUNTREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYVALIDATORACCOUNTREQUEST._options = None
    _QUERYVALIDATORACCOUNTREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYBALANCEREQUEST._options = None
    _QUERYBALANCEREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYSTORAGEREQUEST._options = None
    _QUERYSTORAGEREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYCODEREQUEST._options = None
    _QUERYCODEREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYTXLOGSREQUEST._options = None
    _QUERYTXLOGSREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _ETHCALLREQUEST.fields_by_name['proposer_address']._options = None
    _ETHCALLREQUEST.fields_by_name['proposer_address']._serialized_options = b'\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress'
    _QUERYTRACETXREQUEST.fields_by_name['block_time']._options = None
    _QUERYTRACETXREQUEST.fields_by_name['block_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _QUERYTRACETXREQUEST.fields_by_name['proposer_address']._options = None
    _QUERYTRACETXREQUEST.fields_by_name['proposer_address']._serialized_options = b'\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress'
    _QUERYTRACEBLOCKREQUEST.fields_by_name['block_time']._options = None
    _QUERYTRACEBLOCKREQUEST.fields_by_name['block_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _QUERYTRACEBLOCKREQUEST.fields_by_name['proposer_address']._options = None
    _QUERYTRACEBLOCKREQUEST.fields_by_name['proposer_address']._serialized_options = b'\xfa\xde\x1f.github.com/cosmos/cosmos-sdk/types.ConsAddress'
    _QUERYBASEFEERESPONSE.fields_by_name['base_fee']._options = None
    _QUERYBASEFEERESPONSE.fields_by_name['base_fee']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _QUERY.methods_by_name['Account']._options = None
    _QUERY.methods_by_name['Account']._serialized_options = b'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/evm/v1/account/{address}'
    _QUERY.methods_by_name['CosmosAccount']._options = None
    _QUERY.methods_by_name['CosmosAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/evmos/evm/v1/cosmos_account/{address}'
    _QUERY.methods_by_name['ValidatorAccount']._options = None
    _QUERY.methods_by_name['ValidatorAccount']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./evmos/evm/v1/validator_account/{cons_address}'
    _QUERY.methods_by_name['Balance']._options = None
    _QUERY.methods_by_name['Balance']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /evmos/evm/v1/balances/{address}'
    _QUERY.methods_by_name['Storage']._options = None
    _QUERY.methods_by_name['Storage']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/evmos/evm/v1/storage/{address}/{key}"
    _QUERY.methods_by_name['Code']._options = None
    _QUERY.methods_by_name['Code']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/evmos/evm/v1/codes/{address}'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16\x12\x14/evmos/evm/v1/params'
    _QUERY.methods_by_name['EthCall']._options = None
    _QUERY.methods_by_name['EthCall']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/eth_call'
    _QUERY.methods_by_name['EstimateGas']._options = None
    _QUERY.methods_by_name['EstimateGas']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/evm/v1/estimate_gas'
    _QUERY.methods_by_name['TraceTx']._options = None
    _QUERY.methods_by_name['TraceTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/trace_tx'
    _QUERY.methods_by_name['TraceBlock']._options = None
    _QUERY.methods_by_name['TraceBlock']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/evmos/evm/v1/trace_block'
    _QUERY.methods_by_name['BaseFee']._options = None
    _QUERY.methods_by_name['BaseFee']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/evmos/evm/v1/base_fee'
    _globals['_QUERYACCOUNTREQUEST']._serialized_start = 234
    _globals['_QUERYACCOUNTREQUEST']._serialized_end = 282
    _globals['_QUERYACCOUNTRESPONSE']._serialized_start = 284
    _globals['_QUERYACCOUNTRESPONSE']._serialized_end = 357
    _globals['_QUERYCOSMOSACCOUNTREQUEST']._serialized_start = 359
    _globals['_QUERYCOSMOSACCOUNTREQUEST']._serialized_end = 413
    _globals['_QUERYCOSMOSACCOUNTRESPONSE']._serialized_start = 415
    _globals['_QUERYCOSMOSACCOUNTRESPONSE']._serialized_end = 509
    _globals['_QUERYVALIDATORACCOUNTREQUEST']._serialized_start = 511
    _globals['_QUERYVALIDATORACCOUNTREQUEST']._serialized_end = 573
    _globals['_QUERYVALIDATORACCOUNTRESPONSE']._serialized_start = 575
    _globals['_QUERYVALIDATORACCOUNTRESPONSE']._serialized_end = 673
    _globals['_QUERYBALANCEREQUEST']._serialized_start = 675
    _globals['_QUERYBALANCEREQUEST']._serialized_end = 723
    _globals['_QUERYBALANCERESPONSE']._serialized_start = 725
    _globals['_QUERYBALANCERESPONSE']._serialized_end = 764
    _globals['_QUERYSTORAGEREQUEST']._serialized_start = 766
    _globals['_QUERYSTORAGEREQUEST']._serialized_end = 827
    _globals['_QUERYSTORAGERESPONSE']._serialized_start = 829
    _globals['_QUERYSTORAGERESPONSE']._serialized_end = 866
    _globals['_QUERYCODEREQUEST']._serialized_start = 868
    _globals['_QUERYCODEREQUEST']._serialized_end = 913
    _globals['_QUERYCODERESPONSE']._serialized_start = 915
    _globals['_QUERYCODERESPONSE']._serialized_end = 948
    _globals['_QUERYTXLOGSREQUEST']._serialized_start = 950
    _globals['_QUERYTXLOGSREQUEST']._serialized_end = 1054
    _globals['_QUERYTXLOGSRESPONSE']._serialized_start = 1056
    _globals['_QUERYTXLOGSRESPONSE']._serialized_end = 1175
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1177
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1197
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1199
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1268
    _globals['_ETHCALLREQUEST']._serialized_start = 1271
    _globals['_ETHCALLREQUEST']._serialized_end = 1414
    _globals['_ESTIMATEGASRESPONSE']._serialized_start = 1416
    _globals['_ESTIMATEGASRESPONSE']._serialized_end = 1450
    _globals['_QUERYTRACETXREQUEST']._serialized_start = 1453
    _globals['_QUERYTRACETXREQUEST']._serialized_end = 1840
    _globals['_QUERYTRACETXRESPONSE']._serialized_start = 1842
    _globals['_QUERYTRACETXRESPONSE']._serialized_end = 1878
    _globals['_QUERYTRACEBLOCKREQUEST']._serialized_start = 1881
    _globals['_QUERYTRACEBLOCKREQUEST']._serialized_end = 2200
    _globals['_QUERYTRACEBLOCKRESPONSE']._serialized_start = 2202
    _globals['_QUERYTRACEBLOCKRESPONSE']._serialized_end = 2241
    _globals['_QUERYBASEFEEREQUEST']._serialized_start = 2243
    _globals['_QUERYBASEFEEREQUEST']._serialized_end = 2264
    _globals['_QUERYBASEFEERESPONSE']._serialized_start = 2266
    _globals['_QUERYBASEFEERESPONSE']._serialized_end = 2350
    _globals['_QUERY']._serialized_start = 2353
    _globals['_QUERY']._serialized_end = 3952