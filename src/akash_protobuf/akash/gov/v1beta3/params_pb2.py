"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eakash/gov/v1beta3/params.proto\x12\x11akash.gov.v1beta3\x1a\x14gogoproto/gogo.proto"\xbb\x01\n\rDepositParams\x12\xa9\x01\n\x18min_initial_deposit_rate\x18\x01 \x01(\x0cB\x86\x01\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x15MinInitialDepositRate\xea\xde\x1f\x18min_initial_deposit_rate\xf2\xde\x1f\x1fyaml:"min_initial_deposit_rate"B8Z6github.com/akash-network/akash-api/go/node/gov/v1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.gov.v1beta3.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z6github.com/akash-network/akash-api/go/node/gov/v1beta3'
    _DEPOSITPARAMS.fields_by_name['min_initial_deposit_rate']._options = None
    _DEPOSITPARAMS.fields_by_name['min_initial_deposit_rate']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xe2\xde\x1f\x15MinInitialDepositRate\xea\xde\x1f\x18min_initial_deposit_rate\xf2\xde\x1f\x1fyaml:"min_initial_deposit_rate"'
    _globals['_DEPOSITPARAMS']._serialized_start = 76
    _globals['_DEPOSITPARAMS']._serialized_end = 263