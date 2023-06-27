"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/bank/v1beta1/query.proto\x12\x13cosmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ecosmos/bank/v1beta1/bank.proto\x1a\x19cosmos_proto/cosmos.proto"Y\n\x13QueryBalanceRequest\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\r\n\x05denom\x18\x02 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"B\n\x14QueryBalanceResponse\x12*\n\x07balance\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.Coin"\x8a\x01\n\x17QueryAllBalancesRequest\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb6\x01\n\x18QueryAllBalancesResponse\x12]\n\x08balances\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x90\x01\n\x1dQuerySpendableBalancesRequest\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xbc\x01\n\x1eQuerySpendableBalancesResponse\x12]\n\x08balances\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"_\n\x17QueryTotalSupplyRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb4\x01\n\x18QueryTotalSupplyResponse\x12[\n\x06supply\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"%\n\x14QuerySupplyOfRequest\x12\r\n\x05denom\x18\x01 \x01(\t"H\n\x15QuerySupplyOfResponse\x12/\n\x06amount\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"X\n\x1aQueryDenomsMetadataRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x92\x01\n\x1bQueryDenomsMetadataResponse\x126\n\tmetadatas\x18\x01 \x03(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"*\n\x19QueryDenomMetadataRequest\x12\r\n\x05denom\x18\x01 \x01(\t"S\n\x1aQueryDenomMetadataResponse\x125\n\x08metadata\x18\x01 \x01(\x0b2\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00"d\n\x17QueryDenomOwnersRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"i\n\nDenomOwner\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x07balance\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00"\x8e\x01\n\x18QueryDenomOwnersResponse\x125\n\x0cdenom_owners\x18\x01 \x03(\x0b2\x1f.cosmos.bank.v1beta1.DenomOwner\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\x8e\x0b\n\x05Query\x12\x98\x01\n\x07Balance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse"8\x82\xd3\xe4\x93\x022\x120/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\x9b\x01\n\x0bAllBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\xb7\x01\n\x11SpendableBalances\x122.cosmos.bank.v1beta1.QuerySpendableBalancesRequest\x1a3.cosmos.bank.v1beta1.QuerySpendableBalancesResponse"9\x82\xd3\xe4\x93\x023\x121/cosmos/bank/v1beta1/spendable_balances/{address}\x12\x8f\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x8f\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse",\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/supply/by_denom\x12\x80\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xa6\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xa1\x01\n\x0eDenomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a0.cosmos.bank.v1beta1.QueryDenomsMetadataResponse",\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata\x12\x9d\x01\n\x0bDenomOwners\x12,.cosmos.bank.v1beta1.QueryDenomOwnersRequest\x1a-.cosmos.bank.v1beta1.QueryDenomOwnersResponse"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/bank/v1beta1/denom_owners/{denom}B+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
    _QUERYBALANCEREQUEST.fields_by_name['address']._options = None
    _QUERYBALANCEREQUEST.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYBALANCEREQUEST._options = None
    _QUERYBALANCEREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYALLBALANCESREQUEST.fields_by_name['address']._options = None
    _QUERYALLBALANCESREQUEST.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYALLBALANCESREQUEST._options = None
    _QUERYALLBALANCESREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
    _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYSPENDABLEBALANCESREQUEST.fields_by_name['address']._options = None
    _QUERYSPENDABLEBALANCESREQUEST.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _QUERYSPENDABLEBALANCESREQUEST._options = None
    _QUERYSPENDABLEBALANCESREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._options = None
    _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALSUPPLYREQUEST._options = None
    _QUERYTOTALSUPPLYREQUEST._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
    _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
    _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
    _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
    _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None
    _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._serialized_options = b'\xc8\xde\x1f\x00'
    _DENOMOWNER.fields_by_name['address']._options = None
    _DENOMOWNER.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _DENOMOWNER.fields_by_name['balance']._options = None
    _DENOMOWNER.fields_by_name['balance']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERY.methods_by_name['Balance']._options = None
    _QUERY.methods_by_name['Balance']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/cosmos/bank/v1beta1/balances/{address}/by_denom'
    _QUERY.methods_by_name['AllBalances']._options = None
    _QUERY.methods_by_name['AllBalances']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/bank/v1beta1/balances/{address}"
    _QUERY.methods_by_name['SpendableBalances']._options = None
    _QUERY.methods_by_name['SpendableBalances']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/cosmos/bank/v1beta1/spendable_balances/{address}'
    _QUERY.methods_by_name['TotalSupply']._options = None
    _QUERY.methods_by_name['TotalSupply']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply'
    _QUERY.methods_by_name['SupplyOf']._options = None
    _QUERY.methods_by_name['SupplyOf']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/supply/by_denom'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params'
    _QUERY.methods_by_name['DenomMetadata']._options = None
    _QUERY.methods_by_name['DenomMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
    _QUERY.methods_by_name['DenomsMetadata']._options = None
    _QUERY.methods_by_name['DenomsMetadata']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadata'
    _QUERY.methods_by_name['DenomOwners']._options = None
    _QUERY.methods_by_name['DenomOwners']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/cosmos/bank/v1beta1/denom_owners/{denom}'
    _globals['_QUERYBALANCEREQUEST']._serialized_start = 243
    _globals['_QUERYBALANCEREQUEST']._serialized_end = 332
    _globals['_QUERYBALANCERESPONSE']._serialized_start = 334
    _globals['_QUERYBALANCERESPONSE']._serialized_end = 400
    _globals['_QUERYALLBALANCESREQUEST']._serialized_start = 403
    _globals['_QUERYALLBALANCESREQUEST']._serialized_end = 541
    _globals['_QUERYALLBALANCESRESPONSE']._serialized_start = 544
    _globals['_QUERYALLBALANCESRESPONSE']._serialized_end = 726
    _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_start = 729
    _globals['_QUERYSPENDABLEBALANCESREQUEST']._serialized_end = 873
    _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_start = 876
    _globals['_QUERYSPENDABLEBALANCESRESPONSE']._serialized_end = 1064
    _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_start = 1066
    _globals['_QUERYTOTALSUPPLYREQUEST']._serialized_end = 1161
    _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_start = 1164
    _globals['_QUERYTOTALSUPPLYRESPONSE']._serialized_end = 1344
    _globals['_QUERYSUPPLYOFREQUEST']._serialized_start = 1346
    _globals['_QUERYSUPPLYOFREQUEST']._serialized_end = 1383
    _globals['_QUERYSUPPLYOFRESPONSE']._serialized_start = 1385
    _globals['_QUERYSUPPLYOFRESPONSE']._serialized_end = 1457
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 1459
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 1479
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1481
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1553
    _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_start = 1555
    _globals['_QUERYDENOMSMETADATAREQUEST']._serialized_end = 1643
    _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_start = 1646
    _globals['_QUERYDENOMSMETADATARESPONSE']._serialized_end = 1792
    _globals['_QUERYDENOMMETADATAREQUEST']._serialized_start = 1794
    _globals['_QUERYDENOMMETADATAREQUEST']._serialized_end = 1836
    _globals['_QUERYDENOMMETADATARESPONSE']._serialized_start = 1838
    _globals['_QUERYDENOMMETADATARESPONSE']._serialized_end = 1921
    _globals['_QUERYDENOMOWNERSREQUEST']._serialized_start = 1923
    _globals['_QUERYDENOMOWNERSREQUEST']._serialized_end = 2023
    _globals['_DENOMOWNER']._serialized_start = 2025
    _globals['_DENOMOWNER']._serialized_end = 2130
    _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_start = 2133
    _globals['_QUERYDENOMOWNERSRESPONSE']._serialized_end = 2275
    _globals['_QUERY']._serialized_start = 2278
    _globals['_QUERY']._serialized_end = 3700