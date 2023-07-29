"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from .....tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from .....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/query.proto\x12\x1ecosmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1atendermint/p2p/types.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto"l\n\x1eGetValidatorSetByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb3\x01\n\x1fGetValidatorSetByHeightResponse\x12\x14\n\x0cblock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b2).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Z\n\x1cGetLatestValidatorSetRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb1\x01\n\x1dGetLatestValidatorSetResponse\x12\x14\n\x0cblock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b2).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"t\n\tValidator\x12\x0f\n\x07address\x18\x01 \x01(\t\x12%\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x14\n\x0cvoting_power\x18\x03 \x01(\x03\x12\x19\n\x11proposer_priority\x18\x04 \x01(\x03")\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03"o\n\x18GetBlockByHeightResponse\x12+\n\x08block_id\x18\x01 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x02 \x01(\x0b2\x17.tendermint.types.Block"\x17\n\x15GetLatestBlockRequest"m\n\x16GetLatestBlockResponse\x12+\n\x08block_id\x18\x01 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x02 \x01(\x0b2\x17.tendermint.types.Block"\x13\n\x11GetSyncingRequest"%\n\x12GetSyncingResponse\x12\x0f\n\x07syncing\x18\x01 \x01(\x08"\x14\n\x12GetNodeInfoRequest"\x9b\x01\n\x13GetNodeInfoResponse\x12:\n\x11default_node_info\x18\x01 \x01(\x0b2\x1f.tendermint.p2p.DefaultNodeInfo\x12H\n\x13application_version\x18\x02 \x01(\x0b2+.cosmos.base.tendermint.v1beta1.VersionInfo"\xd2\x01\n\x0bVersionInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08app_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x12\n\ngit_commit\x18\x04 \x01(\t\x12\x12\n\nbuild_tags\x18\x05 \x01(\t\x12\x12\n\ngo_version\x18\x06 \x01(\t\x12:\n\nbuild_deps\x18\x07 \x03(\x0b2&.cosmos.base.tendermint.v1beta1.Module\x12\x1a\n\x12cosmos_sdk_version\x18\x08 \x01(\t"4\n\x06Module\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sum\x18\x03 \x01(\t2\x88\t\n\x07Service\x12\xa9\x01\n\x0bGetNodeInfo\x122.cosmos.base.tendermint.v1beta1.GetNodeInfoRequest\x1a3.cosmos.base.tendermint.v1beta1.GetNodeInfoResponse"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info\x12\xa4\x01\n\nGetSyncing\x121.cosmos.base.tendermint.v1beta1.GetSyncingRequest\x1a2.cosmos.base.tendermint.v1beta1.GetSyncingResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/base/tendermint/v1beta1/syncing\x12\xb6\x01\n\x0eGetLatestBlock\x125.cosmos.base.tendermint.v1beta1.GetLatestBlockRequest\x1a6.cosmos.base.tendermint.v1beta1.GetLatestBlockResponse"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest\x12\xbe\x01\n\x10GetBlockByHeight\x127.cosmos.base.tendermint.v1beta1.GetBlockByHeightRequest\x1a8.cosmos.base.tendermint.v1beta1.GetBlockByHeightResponse"7\x82\xd3\xe4\x93\x021\x12//cosmos/base/tendermint/v1beta1/blocks/{height}\x12\xd2\x01\n\x15GetLatestValidatorSet\x12<.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetRequest\x1a=.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/base/tendermint/v1beta1/validatorsets/latest\x12\xda\x01\n\x17GetValidatorSetByHeight\x12>.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightRequest\x1a?.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightResponse">\x82\xd3\xe4\x93\x028\x126/cosmos/base/tendermint/v1beta1/validatorsets/{height}B4Z2github.com/cosmos/cosmos-sdk/client/grpc/tmserviceb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.tendermint.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/client/grpc/tmservice'
    _SERVICE.methods_by_name['GetNodeInfo']._options = None
    _SERVICE.methods_by_name['GetNodeInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info'
    _SERVICE.methods_by_name['GetSyncing']._options = None
    _SERVICE.methods_by_name['GetSyncing']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/base/tendermint/v1beta1/syncing"
    _SERVICE.methods_by_name['GetLatestBlock']._options = None
    _SERVICE.methods_by_name['GetLatestBlock']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest'
    _SERVICE.methods_by_name['GetBlockByHeight']._options = None
    _SERVICE.methods_by_name['GetBlockByHeight']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//cosmos/base/tendermint/v1beta1/blocks/{height}'
    _SERVICE.methods_by_name['GetLatestValidatorSet']._options = None
    _SERVICE.methods_by_name['GetLatestValidatorSet']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/base/tendermint/v1beta1/validatorsets/latest'
    _SERVICE.methods_by_name['GetValidatorSetByHeight']._options = None
    _SERVICE.methods_by_name['GetValidatorSetByHeight']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/cosmos/base/tendermint/v1beta1/validatorsets/{height}'
    _globals['_GETVALIDATORSETBYHEIGHTREQUEST']._serialized_start = 289
    _globals['_GETVALIDATORSETBYHEIGHTREQUEST']._serialized_end = 397
    _globals['_GETVALIDATORSETBYHEIGHTRESPONSE']._serialized_start = 400
    _globals['_GETVALIDATORSETBYHEIGHTRESPONSE']._serialized_end = 579
    _globals['_GETLATESTVALIDATORSETREQUEST']._serialized_start = 581
    _globals['_GETLATESTVALIDATORSETREQUEST']._serialized_end = 671
    _globals['_GETLATESTVALIDATORSETRESPONSE']._serialized_start = 674
    _globals['_GETLATESTVALIDATORSETRESPONSE']._serialized_end = 851
    _globals['_VALIDATOR']._serialized_start = 853
    _globals['_VALIDATOR']._serialized_end = 969
    _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_start = 971
    _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_end = 1012
    _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_start = 1014
    _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_end = 1125
    _globals['_GETLATESTBLOCKREQUEST']._serialized_start = 1127
    _globals['_GETLATESTBLOCKREQUEST']._serialized_end = 1150
    _globals['_GETLATESTBLOCKRESPONSE']._serialized_start = 1152
    _globals['_GETLATESTBLOCKRESPONSE']._serialized_end = 1261
    _globals['_GETSYNCINGREQUEST']._serialized_start = 1263
    _globals['_GETSYNCINGREQUEST']._serialized_end = 1282
    _globals['_GETSYNCINGRESPONSE']._serialized_start = 1284
    _globals['_GETSYNCINGRESPONSE']._serialized_end = 1321
    _globals['_GETNODEINFOREQUEST']._serialized_start = 1323
    _globals['_GETNODEINFOREQUEST']._serialized_end = 1343
    _globals['_GETNODEINFORESPONSE']._serialized_start = 1346
    _globals['_GETNODEINFORESPONSE']._serialized_end = 1501
    _globals['_VERSIONINFO']._serialized_start = 1504
    _globals['_VERSIONINFO']._serialized_end = 1714
    _globals['_MODULE']._serialized_start = 1716
    _globals['_MODULE']._serialized_end = 1768
    _globals['_SERVICE']._serialized_start = 1771
    _globals['_SERVICE']._serialized_end = 2931