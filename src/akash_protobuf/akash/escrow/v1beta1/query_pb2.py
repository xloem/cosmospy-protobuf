"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....akash.escrow.v1beta1 import types_pb2 as akash_dot_escrow_dot_v1beta1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n akash/escrow/v1beta1/query.proto\x12\x14akash.escrow.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a akash/escrow/v1beta1/types.proto"\x8c\x01\n\x14QueryAccountsRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0b\n\x03xid\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12:\n\npagination\x18\x05 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8b\x01\n\x15QueryAccountsResponse\x125\n\x08accounts\x18\x01 \x03(\x0b2\x1d.akash.escrow.v1beta1.AccountB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x98\x01\n\x14QueryPaymentsRequest\x12\r\n\x05scope\x18\x01 \x01(\t\x12\x0b\n\x03xid\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05owner\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12:\n\npagination\x18\x06 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8b\x01\n\x15QueryPaymentsResponse\x125\n\x08payments\x18\x01 \x03(\x0b2\x1d.akash.escrow.v1beta1.PaymentB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xb9\x02\n\x05Query\x12\x96\x01\n\x08Accounts\x12*.akash.escrow.v1beta1.QueryAccountsRequest\x1a+.akash.escrow.v1beta1.QueryAccountsResponse"1\x82\xd3\xe4\x93\x02+\x12)/akash/escrow/v1beta1/types/accounts/list\x12\x96\x01\n\x08Payments\x12*.akash.escrow.v1beta1.QueryPaymentsRequest\x1a+.akash.escrow.v1beta1.QueryPaymentsResponse"1\x82\xd3\xe4\x93\x02+\x12)/akash/escrow/v1beta1/types/payments/listB;Z9github.com/akash-network/akash-api/go/node/escrow/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'akash.escrow.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/akash-network/akash-api/go/node/escrow/v1beta1'
    _QUERYACCOUNTSRESPONSE.fields_by_name['accounts']._options = None
    _QUERYACCOUNTSRESPONSE.fields_by_name['accounts']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPAYMENTSRESPONSE.fields_by_name['payments']._options = None
    _QUERYPAYMENTSRESPONSE.fields_by_name['payments']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Accounts']._options = None
    _QUERY.methods_by_name['Accounts']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/akash/escrow/v1beta1/types/accounts/list'
    _QUERY.methods_by_name['Payments']._options = None
    _QUERY.methods_by_name['Payments']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/akash/escrow/v1beta1/types/payments/list'
    _globals['_QUERYACCOUNTSREQUEST']._serialized_start = 189
    _globals['_QUERYACCOUNTSREQUEST']._serialized_end = 329
    _globals['_QUERYACCOUNTSRESPONSE']._serialized_start = 332
    _globals['_QUERYACCOUNTSRESPONSE']._serialized_end = 471
    _globals['_QUERYPAYMENTSREQUEST']._serialized_start = 474
    _globals['_QUERYPAYMENTSREQUEST']._serialized_end = 626
    _globals['_QUERYPAYMENTSRESPONSE']._serialized_start = 629
    _globals['_QUERYPAYMENTSRESPONSE']._serialized_end = 768
    _globals['_QUERY']._serialized_start = 771
    _globals['_QUERY']._serialized_end = 1084