"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.gov.v1beta1 import gov_pb2 as cosmos_dot_gov_dot_v1beta1_dot_gov__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/gov/v1beta1/tx.proto\x12\x12cosmos.gov.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1ccosmos/gov/v1beta1/gov.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x17cosmos/msg/v1/msg.proto"\xf8\x01\n\x11MsgSubmitProposal\x122\n\x07content\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07Content\x12d\n\x0finitial_deposit\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12*\n\x08proposer\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x1d\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x08proposer"A\n\x19MsgSubmitProposalResponse\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id"\x93\x01\n\x07MsgVote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12.\n\x06option\x18\x03 \x01(\x0e2\x1e.cosmos.gov.v1beta1.VoteOption:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter"\x11\n\x0fMsgVoteResponse"\xbb\x01\n\x0fMsgVoteWeighted\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12=\n\x07options\x18\x03 \x03(\x0b2&.cosmos.gov.v1beta1.WeightedVoteOptionB\x04\xc8\xde\x1f\x00:\x1a\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter"\x19\n\x17MsgVoteWeightedResponse"\xdc\x01\n\nMsgDeposit\x12$\n\x0bproposal_id\x18\x01 \x01(\x04B\x0f\xea\xde\x1f\x0bproposal_id\x12+\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x1e\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\tdepositor"\x14\n\x12MsgDepositResponse2\xec\x02\n\x03Msg\x12f\n\x0eSubmitProposal\x12%.cosmos.gov.v1beta1.MsgSubmitProposal\x1a-.cosmos.gov.v1beta1.MsgSubmitProposalResponse\x12H\n\x04Vote\x12\x1b.cosmos.gov.v1beta1.MsgVote\x1a#.cosmos.gov.v1beta1.MsgVoteResponse\x12`\n\x0cVoteWeighted\x12#.cosmos.gov.v1beta1.MsgVoteWeighted\x1a+.cosmos.gov.v1beta1.MsgVoteWeightedResponse\x12Q\n\x07Deposit\x12\x1e.cosmos.gov.v1beta1.MsgDeposit\x1a&.cosmos.gov.v1beta1.MsgDepositResponseB2Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z0github.com/cosmos/cosmos-sdk/x/gov/types/v1beta1'
    _MSGSUBMITPROPOSAL.fields_by_name['content']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['content']._serialized_options = b'\xca\xb4-\x07Content'
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['initial_deposit']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGSUBMITPROPOSAL.fields_by_name['proposer']._options = None
    _MSGSUBMITPROPOSAL.fields_by_name['proposer']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGSUBMITPROPOSAL._options = None
    _MSGSUBMITPROPOSAL._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x08proposer'
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name['proposal_id']._options = None
    _MSGSUBMITPROPOSALRESPONSE.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGVOTE.fields_by_name['voter']._options = None
    _MSGVOTE.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGVOTE._options = None
    _MSGVOTE._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter'
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGVOTEWEIGHTED.fields_by_name['voter']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGVOTEWEIGHTED.fields_by_name['options']._options = None
    _MSGVOTEWEIGHTED.fields_by_name['options']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGVOTEWEIGHTED._options = None
    _MSGVOTEWEIGHTED._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\x05voter'
    _MSGDEPOSIT.fields_by_name['proposal_id']._options = None
    _MSGDEPOSIT.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x0bproposal_id'
    _MSGDEPOSIT.fields_by_name['depositor']._options = None
    _MSGDEPOSIT.fields_by_name['depositor']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDEPOSIT.fields_by_name['amount']._options = None
    _MSGDEPOSIT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _MSGDEPOSIT._options = None
    _MSGDEPOSIT._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x00\x80\xdc \x00\x82\xe7\xb0*\tdepositor'
    _globals['_MSGSUBMITPROPOSAL']._serialized_start = 215
    _globals['_MSGSUBMITPROPOSAL']._serialized_end = 463
    _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_start = 465
    _globals['_MSGSUBMITPROPOSALRESPONSE']._serialized_end = 530
    _globals['_MSGVOTE']._serialized_start = 533
    _globals['_MSGVOTE']._serialized_end = 680
    _globals['_MSGVOTERESPONSE']._serialized_start = 682
    _globals['_MSGVOTERESPONSE']._serialized_end = 699
    _globals['_MSGVOTEWEIGHTED']._serialized_start = 702
    _globals['_MSGVOTEWEIGHTED']._serialized_end = 889
    _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_start = 891
    _globals['_MSGVOTEWEIGHTEDRESPONSE']._serialized_end = 916
    _globals['_MSGDEPOSIT']._serialized_start = 919
    _globals['_MSGDEPOSIT']._serialized_end = 1139
    _globals['_MSGDEPOSITRESPONSE']._serialized_start = 1141
    _globals['_MSGDEPOSITRESPONSE']._serialized_end = 1161
    _globals['_MSG']._serialized_start = 1164
    _globals['_MSG']._serialized_end = 1528