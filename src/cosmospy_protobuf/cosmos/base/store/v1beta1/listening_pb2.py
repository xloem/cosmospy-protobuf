"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)cosmos/base/store/v1beta1/listening.proto\x12\x19cosmos.base.store.v1beta1\x1a\x1btendermint/abci/types.proto"L\n\x0bStoreKVPair\x12\x11\n\tstore_key\x18\x01 \x01(\t\x12\x0e\n\x06delete\x18\x02 \x01(\x08\x12\x0b\n\x03key\x18\x03 \x01(\x0c\x12\r\n\x05value\x18\x04 \x01(\x0c"\x89\x04\n\rBlockMetadata\x12?\n\x13request_begin_block\x18\x01 \x01(\x0b2".tendermint.abci.RequestBeginBlock\x12A\n\x14response_begin_block\x18\x02 \x01(\x0b2#.tendermint.abci.ResponseBeginBlock\x12G\n\x0bdeliver_txs\x18\x03 \x03(\x0b22.cosmos.base.store.v1beta1.BlockMetadata.DeliverTx\x12;\n\x11request_end_block\x18\x04 \x01(\x0b2 .tendermint.abci.RequestEndBlock\x12=\n\x12response_end_block\x18\x05 \x01(\x0b2!.tendermint.abci.ResponseEndBlock\x128\n\x0fresponse_commit\x18\x06 \x01(\x0b2\x1f.tendermint.abci.ResponseCommit\x1au\n\tDeliverTx\x122\n\x07request\x18\x01 \x01(\x0b2!.tendermint.abci.RequestDeliverTx\x124\n\x08response\x18\x02 \x01(\x0b2".tendermint.abci.ResponseDeliverTxB*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.store.v1beta1.listening_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/store/types'
    _globals['_STOREKVPAIR']._serialized_start = 101
    _globals['_STOREKVPAIR']._serialized_end = 177
    _globals['_BLOCKMETADATA']._serialized_start = 180
    _globals['_BLOCKMETADATA']._serialized_end = 701
    _globals['_BLOCKMETADATA_DELIVERTX']._serialized_start = 584
    _globals['_BLOCKMETADATA_DELIVERTX']._serialized_end = 701