"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dethermint/types/v1/web3.proto\x12\x12ethermint.types.v1\x1a\x14gogoproto/gogo.proto"\xcc\x01\n\x16ExtensionOptionsWeb3Tx\x12O\n\x13typed_data_chain_id\x18\x01 \x01(\x04B2\xe2\xde\x1f\x10TypedDataChainID\xea\xde\x1f\x1atypedDataChainID,omitempty\x12)\n\tfee_payer\x18\x02 \x01(\tB\x16\xea\xde\x1f\x12feePayer,omitempty\x120\n\rfee_payer_sig\x18\x03 \x01(\x0cB\x19\xea\xde\x1f\x15feePayerSig,omitempty:\x04\x88\xa0\x1f\x00B"Z github.com/evmos/evmos/v13/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ethermint.types.v1.web3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z github.com/evmos/evmos/v13/types'
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['typed_data_chain_id']._options = None
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['typed_data_chain_id']._serialized_options = b'\xe2\xde\x1f\x10TypedDataChainID\xea\xde\x1f\x1atypedDataChainID,omitempty'
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer']._options = None
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer']._serialized_options = b'\xea\xde\x1f\x12feePayer,omitempty'
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer_sig']._options = None
    _EXTENSIONOPTIONSWEB3TX.fields_by_name['fee_payer_sig']._serialized_options = b'\xea\xde\x1f\x15feePayerSig,omitempty'
    _EXTENSIONOPTIONSWEB3TX._options = None
    _EXTENSIONOPTIONSWEB3TX._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_EXTENSIONOPTIONSWEB3TX']._serialized_start = 76
    _globals['_EXTENSIONOPTIONSWEB3TX']._serialized_end = 280