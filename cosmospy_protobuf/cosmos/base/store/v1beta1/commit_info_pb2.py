
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+cosmos/base/store/v1beta1/commit_info.proto\x12\x19cosmos.base.store.v1beta1\x1a\x14gogoproto/gogo.proto"^\n\nCommitInfo\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12?\n\x0bstore_infos\x18\x02 \x03(\x0b2$.cosmos.base.store.v1beta1.StoreInfoB\x04\xc8\xde\x1f\x00"W\n\tStoreInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\tcommit_id\x18\x02 \x01(\x0b2#.cosmos.base.store.v1beta1.CommitIDB\x04\xc8\xde\x1f\x00"/\n\x08CommitID\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x0c\n\x04hash\x18\x02 \x01(\x0c:\x04\x98\xa0\x1f\x00B*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3')
_COMMITINFO = DESCRIPTOR.message_types_by_name['CommitInfo']
_STOREINFO = DESCRIPTOR.message_types_by_name['StoreInfo']
_COMMITID = DESCRIPTOR.message_types_by_name['CommitID']
CommitInfo = _reflection.GeneratedProtocolMessageType('CommitInfo', (_message.Message,), {'DESCRIPTOR': _COMMITINFO, '__module__': 'cosmos.base.store.v1beta1.commit_info_pb2'})
_sym_db.RegisterMessage(CommitInfo)
StoreInfo = _reflection.GeneratedProtocolMessageType('StoreInfo', (_message.Message,), {'DESCRIPTOR': _STOREINFO, '__module__': 'cosmos.base.store.v1beta1.commit_info_pb2'})
_sym_db.RegisterMessage(StoreInfo)
CommitID = _reflection.GeneratedProtocolMessageType('CommitID', (_message.Message,), {'DESCRIPTOR': _COMMITID, '__module__': 'cosmos.base.store.v1beta1.commit_info_pb2'})
_sym_db.RegisterMessage(CommitID)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/store/types'
    _COMMITINFO.fields_by_name['store_infos']._options = None
    _COMMITINFO.fields_by_name['store_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _STOREINFO.fields_by_name['commit_id']._options = None
    _STOREINFO.fields_by_name['commit_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _COMMITID._options = None
    _COMMITID._serialized_options = b'\x98\xa0\x1f\x00'
    _COMMITINFO._serialized_start = 96
    _COMMITINFO._serialized_end = 190
    _STOREINFO._serialized_start = 192
    _STOREINFO._serialized_end = 279
    _COMMITID._serialized_start = 281
    _COMMITID._serialized_end = 328
