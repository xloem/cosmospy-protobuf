"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....ethermint.evm.v1 import evm_pb2 as ethermint_dot_evm_dot_v1_dot_evm__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19ethermint/evm/v1/tx.proto\x12\x10ethermint.evm.v1\x1a\x17cosmos/msg/v1/msg.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1aethermint/evm/v1/evm.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto"w\n\rMsgEthereumTx\x12"\n\x04data\x18\x01 \x01(\x0b2\x14.google.protobuf.Any\x12\x13\n\x04size\x18\x02 \x01(\x01B\x05\xea\xde\x1f\x01-\x12\x19\n\x04hash\x18\x03 \x01(\tB\x0b\xf2\xde\x1f\x07rlp:"-"\x12\x0c\n\x04from\x18\x04 \x01(\t:\x04\x88\xa0\x1f\x00"\x83\x02\n\x08LegacyTx\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12=\n\tgas_price\x18\x02 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x03 \x01(\x04B\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x04 \x01(\t\x12C\n\x05value\x18\x05 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount\x12\x0c\n\x04data\x18\x06 \x01(\x0c\x12\t\n\x01v\x18\x07 \x01(\x0c\x12\t\n\x01r\x18\x08 \x01(\x0c\x12\t\n\x01s\x18\t \x01(\x0c:\x0e\x88\xa0\x1f\x00\xca\xb4-\x06TxData"\xae\x03\n\x0cAccessListTx\x12R\n\x08chain_id\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07ChainID\xea\xde\x1f\x07chainID\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12=\n\tgas_price\x18\x03 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x04 \x01(\x04B\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x05 \x01(\t\x12C\n\x05value\x18\x06 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount\x12\x0c\n\x04data\x18\x07 \x01(\x0c\x12Q\n\x08accesses\x18\x08 \x03(\x0b2\x1d.ethermint.evm.v1.AccessTupleB \xc8\xde\x1f\x00\xea\xde\x1f\naccessList\xaa\xdf\x1f\nAccessList\x12\t\n\x01v\x18\t \x01(\x0c\x12\t\n\x01r\x18\n \x01(\x0c\x12\t\n\x01s\x18\x0b \x01(\x0c:\x0e\x88\xa0\x1f\x00\xca\xb4-\x06TxData"\xf1\x03\n\x0cDynamicFeeTx\x12R\n\x08chain_id\x18\x01 \x01(\tB@\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07ChainID\xea\xde\x1f\x07chainID\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12?\n\x0bgas_tip_cap\x18\x03 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12?\n\x0bgas_fee_cap\x18\x04 \x01(\tB*\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x19\n\x03gas\x18\x05 \x01(\x04B\x0c\xe2\xde\x1f\x08GasLimit\x12\n\n\x02to\x18\x06 \x01(\t\x12C\n\x05value\x18\x07 \x01(\tB4\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount\x12\x0c\n\x04data\x18\x08 \x01(\x0c\x12Q\n\x08accesses\x18\t \x03(\x0b2\x1d.ethermint.evm.v1.AccessTupleB \xc8\xde\x1f\x00\xea\xde\x1f\naccessList\xaa\xdf\x1f\nAccessList\x12\t\n\x01v\x18\n \x01(\x0c\x12\t\n\x01r\x18\x0b \x01(\x0c\x12\t\n\x01s\x18\x0c \x01(\x0c:\x0e\x88\xa0\x1f\x00\xca\xb4-\x06TxData""\n\x1aExtensionOptionsEthereumTx:\x04\x88\xa0\x1f\x00"\x81\x01\n\x15MsgEthereumTxResponse\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12#\n\x04logs\x18\x02 \x03(\x0b2\x15.ethermint.evm.v1.Log\x12\x0b\n\x03ret\x18\x03 \x01(\x0c\x12\x10\n\x08vm_error\x18\x04 \x01(\t\x12\x10\n\x08gas_used\x18\x05 \x01(\x04:\x04\x88\xa0\x1f\x00"~\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12.\n\x06params\x18\x02 \x01(\x0b2\x18.ethermint.evm.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority"\x19\n\x17MsgUpdateParamsResponse2\xde\x01\n\x03Msg\x12y\n\nEthereumTx\x12\x1f.ethermint.evm.v1.MsgEthereumTx\x1a\'.ethermint.evm.v1.MsgEthereumTxResponse"!\x82\xd3\xe4\x93\x02\x1b"\x19/evmos/evm/v1/ethereum_tx\x12\\\n\x0cUpdateParams\x12!.ethermint.evm.v1.MsgUpdateParams\x1a).ethermint.evm.v1.MsgUpdateParamsResponseB(Z&github.com/evmos/evmos/v13/x/evm/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.evm.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z&github.com/evmos/evmos/v13/x/evm/types'
    _MSGETHEREUMTX.fields_by_name['size']._options = None
    _MSGETHEREUMTX.fields_by_name['size']._serialized_options = b'\xea\xde\x1f\x01-'
    _MSGETHEREUMTX.fields_by_name['hash']._options = None
    _MSGETHEREUMTX.fields_by_name['hash']._serialized_options = b'\xf2\xde\x1f\x07rlp:"-"'
    _MSGETHEREUMTX._options = None
    _MSGETHEREUMTX._serialized_options = b'\x88\xa0\x1f\x00'
    _LEGACYTX.fields_by_name['gas_price']._options = None
    _LEGACYTX.fields_by_name['gas_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _LEGACYTX.fields_by_name['gas']._options = None
    _LEGACYTX.fields_by_name['gas']._serialized_options = b'\xe2\xde\x1f\x08GasLimit'
    _LEGACYTX.fields_by_name['value']._options = None
    _LEGACYTX.fields_by_name['value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount'
    _LEGACYTX._options = None
    _LEGACYTX._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-\x06TxData'
    _ACCESSLISTTX.fields_by_name['chain_id']._options = None
    _ACCESSLISTTX.fields_by_name['chain_id']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07ChainID\xea\xde\x1f\x07chainID'
    _ACCESSLISTTX.fields_by_name['gas_price']._options = None
    _ACCESSLISTTX.fields_by_name['gas_price']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _ACCESSLISTTX.fields_by_name['gas']._options = None
    _ACCESSLISTTX.fields_by_name['gas']._serialized_options = b'\xe2\xde\x1f\x08GasLimit'
    _ACCESSLISTTX.fields_by_name['value']._options = None
    _ACCESSLISTTX.fields_by_name['value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount'
    _ACCESSLISTTX.fields_by_name['accesses']._options = None
    _ACCESSLISTTX.fields_by_name['accesses']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\naccessList\xaa\xdf\x1f\nAccessList'
    _ACCESSLISTTX._options = None
    _ACCESSLISTTX._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-\x06TxData'
    _DYNAMICFEETX.fields_by_name['chain_id']._options = None
    _DYNAMICFEETX.fields_by_name['chain_id']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x07ChainID\xea\xde\x1f\x07chainID'
    _DYNAMICFEETX.fields_by_name['gas_tip_cap']._options = None
    _DYNAMICFEETX.fields_by_name['gas_tip_cap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _DYNAMICFEETX.fields_by_name['gas_fee_cap']._options = None
    _DYNAMICFEETX.fields_by_name['gas_fee_cap']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _DYNAMICFEETX.fields_by_name['gas']._options = None
    _DYNAMICFEETX.fields_by_name['gas']._serialized_options = b'\xe2\xde\x1f\x08GasLimit'
    _DYNAMICFEETX.fields_by_name['value']._options = None
    _DYNAMICFEETX.fields_by_name['value']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xe2\xde\x1f\x06Amount'
    _DYNAMICFEETX.fields_by_name['accesses']._options = None
    _DYNAMICFEETX.fields_by_name['accesses']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\naccessList\xaa\xdf\x1f\nAccessList'
    _DYNAMICFEETX._options = None
    _DYNAMICFEETX._serialized_options = b'\x88\xa0\x1f\x00\xca\xb4-\x06TxData'
    _EXTENSIONOPTIONSETHEREUMTX._options = None
    _EXTENSIONOPTIONSETHEREUMTX._serialized_options = b'\x88\xa0\x1f\x00'
    _MSGETHEREUMTXRESPONSE._options = None
    _MSGETHEREUMTXRESPONSE._serialized_options = b'\x88\xa0\x1f\x00'
    _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
    _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEPARAMS.fields_by_name['params']._options = None
    _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGUPDATEPARAMS._options = None
    _MSGUPDATEPARAMS._serialized_options = b'\x82\xe7\xb0*\tauthority'
    _MSG.methods_by_name['EthereumTx']._options = None
    _MSG.methods_by_name['EthereumTx']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b"\x19/evmos/evm/v1/ethereum_tx'
    _globals['_MSGETHEREUMTX']._serialized_start = 206
    _globals['_MSGETHEREUMTX']._serialized_end = 325
    _globals['_LEGACYTX']._serialized_start = 328
    _globals['_LEGACYTX']._serialized_end = 587
    _globals['_ACCESSLISTTX']._serialized_start = 590
    _globals['_ACCESSLISTTX']._serialized_end = 1020
    _globals['_DYNAMICFEETX']._serialized_start = 1023
    _globals['_DYNAMICFEETX']._serialized_end = 1520
    _globals['_EXTENSIONOPTIONSETHEREUMTX']._serialized_start = 1522
    _globals['_EXTENSIONOPTIONSETHEREUMTX']._serialized_end = 1556
    _globals['_MSGETHEREUMTXRESPONSE']._serialized_start = 1559
    _globals['_MSGETHEREUMTXRESPONSE']._serialized_end = 1688
    _globals['_MSGUPDATEPARAMS']._serialized_start = 1690
    _globals['_MSGUPDATEPARAMS']._serialized_end = 1816
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 1818
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 1843
    _globals['_MSG']._serialized_start = 1846
    _globals['_MSG']._serialized_end = 2068