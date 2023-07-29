"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...osmosis.epochs import genesis_pb2 as osmosis_dot_epochs_dot_genesis__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aosmosis/epochs/query.proto\x12\x16osmosis.epochs.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cosmosis/epochs/genesis.proto"\x18\n\x16QueryEpochsInfoRequest"R\n\x17QueryEpochsInfoResponse\x127\n\x06epochs\x18\x01 \x03(\x0b2!.osmosis.epochs.v1beta1.EpochInfoB\x04\xc8\xde\x1f\x00".\n\x18QueryCurrentEpochRequest\x12\x12\n\nidentifier\x18\x01 \x01(\t"2\n\x19QueryCurrentEpochResponse\x12\x15\n\rcurrent_epoch\x18\x01 \x01(\x032\xc4\x02\n\x05Query\x12\x95\x01\n\nEpochInfos\x12..osmosis.epochs.v1beta1.QueryEpochsInfoRequest\x1a/.osmosis.epochs.v1beta1.QueryEpochsInfoResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/osmosis/epochs/v1beta1/epochs\x12\xa2\x01\n\x0cCurrentEpoch\x120.osmosis.epochs.v1beta1.QueryCurrentEpochRequest\x1a1.osmosis.epochs.v1beta1.QueryCurrentEpochResponse"-\x82\xd3\xe4\x93\x02\'\x12%/osmosis/epochs/v1beta1/current_epochB4Z2github.com/osmosis-labs/osmosis/v15/x/epochs/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.epochs.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v15/x/epochs/types'
    _QUERYEPOCHSINFORESPONSE.fields_by_name['epochs']._options = None
    _QUERYEPOCHSINFORESPONSE.fields_by_name['epochs']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['EpochInfos']._options = None
    _QUERY.methods_by_name['EpochInfos']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/osmosis/epochs/v1beta1/epochs'
    _QUERY.methods_by_name['CurrentEpoch']._options = None
    _QUERY.methods_by_name['CurrentEpoch']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/osmosis/epochs/v1beta1/current_epoch"
    _globals['_QUERYEPOCHSINFOREQUEST']._serialized_start = 180
    _globals['_QUERYEPOCHSINFOREQUEST']._serialized_end = 204
    _globals['_QUERYEPOCHSINFORESPONSE']._serialized_start = 206
    _globals['_QUERYEPOCHSINFORESPONSE']._serialized_end = 288
    _globals['_QUERYCURRENTEPOCHREQUEST']._serialized_start = 290
    _globals['_QUERYCURRENTEPOCHREQUEST']._serialized_end = 336
    _globals['_QUERYCURRENTEPOCHRESPONSE']._serialized_start = 338
    _globals['_QUERYCURRENTEPOCHRESPONSE']._serialized_end = 388
    _globals['_QUERY']._serialized_start = 391
    _globals['_QUERY']._serialized_end = 715