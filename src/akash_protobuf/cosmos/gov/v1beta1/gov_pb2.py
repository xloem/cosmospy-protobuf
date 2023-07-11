"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ccosmos/gov/v1beta1/gov.proto\x12\x12cosmos.gov.v1beta1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto"\x95\x01\n\x12WeightedVoteOption\x12.\n\x06option\x18\x01 \x01(\x0e2\x1e.cosmos.gov.v1beta1.VoteOption\x12O\n\x06weight\x18\x02 \x01(\tB?\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\ryaml:"weight""C\n\x0cTextProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t:\x0f\xe8\xa0\x1f\x01\xca\xb4-\x07Content"\xb0\x01\n\x07Deposit\x12+\n\x0bproposal_id\x18\x01 \x01(\x04B\x16\xf2\xde\x1f\x12yaml:"proposal_id"\x12\x11\n\tdepositor\x18\x02 \x01(\t\x12[\n\x06amount\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xfc\x05\n\x08Proposal\x12(\n\x0bproposal_id\x18\x01 \x01(\x04B\x13\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"\x122\n\x07content\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x0b\xca\xb4-\x07Content\x12N\n\x06status\x18\x03 \x01(\x0e2".cosmos.gov.v1beta1.ProposalStatusB\x1a\xf2\xde\x1f\x16yaml:"proposal_status"\x12^\n\x12final_tally_result\x18\x04 \x01(\x0b2\x1f.cosmos.gov.v1beta1.TallyResultB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"final_tally_result"\x12O\n\x0bsubmit_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"submit_time"\x90\xdf\x1f\x01\x12Y\n\x10deposit_end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB#\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"deposit_end_time"\x90\xdf\x1f\x01\x12z\n\rtotal_deposit\x18\x07 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBH\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"total_deposit"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12[\n\x11voting_start_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB$\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"voting_start_time"\x90\xdf\x1f\x01\x12W\n\x0fvoting_end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB"\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"voting_end_time"\x90\xdf\x1f\x01:\x04\xe8\xa0\x1f\x01"\xaa\x02\n\x0bTallyResult\x12;\n\x03yes\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12?\n\x07abstain\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12:\n\x02no\x18\x03 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12[\n\x0cno_with_veto\x18\x04 \x01(\tBE\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:"no_with_veto":\x04\xe8\xa0\x1f\x01"\xbf\x01\n\x04Vote\x12+\n\x0bproposal_id\x18\x01 \x01(\x04B\x16\xf2\xde\x1f\x12yaml:"proposal_id"\x12\r\n\x05voter\x18\x02 \x01(\t\x122\n\x06option\x18\x03 \x01(\x0e2\x1e.cosmos.gov.v1beta1.VoteOptionB\x02\x18\x01\x12=\n\x07options\x18\x04 \x03(\x0b2&.cosmos.gov.v1beta1.WeightedVoteOptionB\x04\xc8\xde\x1f\x00:\x08\x98\xa0\x1f\x00\xe8\xa0\x1f\x00"\x9f\x02\n\rDepositParams\x12\x8f\x01\n\x0bmin_deposit\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB_\xc8\xde\x1f\x00\xea\xde\x1f\x15min_deposit,omitempty\xf2\xde\x1f\x12yaml:"min_deposit"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12|\n\x12max_deposit_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationBE\xc8\xde\x1f\x00\xea\xde\x1f\x1cmax_deposit_period,omitempty\xf2\xde\x1f\x19yaml:"max_deposit_period"\x98\xdf\x1f\x01"}\n\x0cVotingParams\x12m\n\rvoting_period\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB;\xc8\xde\x1f\x00\xea\xde\x1f\x17voting_period,omitempty\xf2\xde\x1f\x14yaml:"voting_period"\x98\xdf\x1f\x01"\xb8\x02\n\x0bTallyParams\x12R\n\x06quorum\x18\x01 \x01(\x0cBB\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x10quorum,omitempty\x12X\n\tthreshold\x18\x02 \x01(\x0cBE\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x13threshold,omitempty\x12{\n\x0eveto_threshold\x18\x03 \x01(\x0cBc\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x18veto_threshold,omitempty\xf2\xde\x1f\x15yaml:"veto_threshold"*\xe6\x01\n\nVoteOption\x12,\n\x17VOTE_OPTION_UNSPECIFIED\x10\x00\x1a\x0f\x8a\x9d \x0bOptionEmpty\x12"\n\x0fVOTE_OPTION_YES\x10\x01\x1a\r\x8a\x9d \tOptionYes\x12*\n\x13VOTE_OPTION_ABSTAIN\x10\x02\x1a\x11\x8a\x9d \rOptionAbstain\x12 \n\x0eVOTE_OPTION_NO\x10\x03\x1a\x0c\x8a\x9d \x08OptionNo\x122\n\x18VOTE_OPTION_NO_WITH_VETO\x10\x04\x1a\x14\x8a\x9d \x10OptionNoWithVeto\x1a\x04\x88\xa3\x1e\x00*\xcc\x02\n\x0eProposalStatus\x12.\n\x1bPROPOSAL_STATUS_UNSPECIFIED\x10\x00\x1a\r\x8a\x9d \tStatusNil\x12;\n\x1ePROPOSAL_STATUS_DEPOSIT_PERIOD\x10\x01\x1a\x17\x8a\x9d \x13StatusDepositPeriod\x129\n\x1dPROPOSAL_STATUS_VOTING_PERIOD\x10\x02\x1a\x16\x8a\x9d \x12StatusVotingPeriod\x12,\n\x16PROPOSAL_STATUS_PASSED\x10\x03\x1a\x10\x8a\x9d \x0cStatusPassed\x120\n\x18PROPOSAL_STATUS_REJECTED\x10\x04\x1a\x12\x8a\x9d \x0eStatusRejected\x12,\n\x16PROPOSAL_STATUS_FAILED\x10\x05\x1a\x10\x8a\x9d \x0cStatusFailed\x1a\x04\x88\xa3\x1e\x00B6Z(github.com/cosmos/cosmos-sdk/x/gov/types\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\x80\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.gov.v1beta1.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/x/gov/types\xc8\xe1\x1e\x00\xd8\xe1\x1e\x00\x80\xe2\x1e\x00'
    _VOTEOPTION._options = None
    _VOTEOPTION._serialized_options = b'\x88\xa3\x1e\x00'
    _VOTEOPTION.values_by_name['VOTE_OPTION_UNSPECIFIED']._options = None
    _VOTEOPTION.values_by_name['VOTE_OPTION_UNSPECIFIED']._serialized_options = b'\x8a\x9d \x0bOptionEmpty'
    _VOTEOPTION.values_by_name['VOTE_OPTION_YES']._options = None
    _VOTEOPTION.values_by_name['VOTE_OPTION_YES']._serialized_options = b'\x8a\x9d \tOptionYes'
    _VOTEOPTION.values_by_name['VOTE_OPTION_ABSTAIN']._options = None
    _VOTEOPTION.values_by_name['VOTE_OPTION_ABSTAIN']._serialized_options = b'\x8a\x9d \rOptionAbstain'
    _VOTEOPTION.values_by_name['VOTE_OPTION_NO']._options = None
    _VOTEOPTION.values_by_name['VOTE_OPTION_NO']._serialized_options = b'\x8a\x9d \x08OptionNo'
    _VOTEOPTION.values_by_name['VOTE_OPTION_NO_WITH_VETO']._options = None
    _VOTEOPTION.values_by_name['VOTE_OPTION_NO_WITH_VETO']._serialized_options = b'\x8a\x9d \x10OptionNoWithVeto'
    _PROPOSALSTATUS._options = None
    _PROPOSALSTATUS._serialized_options = b'\x88\xa3\x1e\x00'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_UNSPECIFIED']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_UNSPECIFIED']._serialized_options = b'\x8a\x9d \tStatusNil'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_DEPOSIT_PERIOD']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_DEPOSIT_PERIOD']._serialized_options = b'\x8a\x9d \x13StatusDepositPeriod'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_VOTING_PERIOD']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_VOTING_PERIOD']._serialized_options = b'\x8a\x9d \x12StatusVotingPeriod'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_PASSED']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_PASSED']._serialized_options = b'\x8a\x9d \x0cStatusPassed'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_REJECTED']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_REJECTED']._serialized_options = b'\x8a\x9d \x0eStatusRejected'
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_FAILED']._options = None
    _PROPOSALSTATUS.values_by_name['PROPOSAL_STATUS_FAILED']._serialized_options = b'\x8a\x9d \x0cStatusFailed'
    _WEIGHTEDVOTEOPTION.fields_by_name['weight']._options = None
    _WEIGHTEDVOTEOPTION.fields_by_name['weight']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xf2\xde\x1f\ryaml:"weight"'
    _TEXTPROPOSAL._options = None
    _TEXTPROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01\xca\xb4-\x07Content'
    _DEPOSIT.fields_by_name['proposal_id']._options = None
    _DEPOSIT.fields_by_name['proposal_id']._serialized_options = b'\xf2\xde\x1f\x12yaml:"proposal_id"'
    _DEPOSIT.fields_by_name['amount']._options = None
    _DEPOSIT.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _DEPOSIT._options = None
    _DEPOSIT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _PROPOSAL.fields_by_name['proposal_id']._options = None
    _PROPOSAL.fields_by_name['proposal_id']._serialized_options = b'\xea\xde\x1f\x02id\xf2\xde\x1f\tyaml:"id"'
    _PROPOSAL.fields_by_name['content']._options = None
    _PROPOSAL.fields_by_name['content']._serialized_options = b'\xca\xb4-\x07Content'
    _PROPOSAL.fields_by_name['status']._options = None
    _PROPOSAL.fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\x16yaml:"proposal_status"'
    _PROPOSAL.fields_by_name['final_tally_result']._options = None
    _PROPOSAL.fields_by_name['final_tally_result']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"final_tally_result"'
    _PROPOSAL.fields_by_name['submit_time']._options = None
    _PROPOSAL.fields_by_name['submit_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"submit_time"\x90\xdf\x1f\x01'
    _PROPOSAL.fields_by_name['deposit_end_time']._options = None
    _PROPOSAL.fields_by_name['deposit_end_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"deposit_end_time"\x90\xdf\x1f\x01'
    _PROPOSAL.fields_by_name['total_deposit']._options = None
    _PROPOSAL.fields_by_name['total_deposit']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"total_deposit"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _PROPOSAL.fields_by_name['voting_start_time']._options = None
    _PROPOSAL.fields_by_name['voting_start_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"voting_start_time"\x90\xdf\x1f\x01'
    _PROPOSAL.fields_by_name['voting_end_time']._options = None
    _PROPOSAL.fields_by_name['voting_end_time']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"voting_end_time"\x90\xdf\x1f\x01'
    _PROPOSAL._options = None
    _PROPOSAL._serialized_options = b'\xe8\xa0\x1f\x01'
    _TALLYRESULT.fields_by_name['yes']._options = None
    _TALLYRESULT.fields_by_name['yes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TALLYRESULT.fields_by_name['abstain']._options = None
    _TALLYRESULT.fields_by_name['abstain']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TALLYRESULT.fields_by_name['no']._options = None
    _TALLYRESULT.fields_by_name['no']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _TALLYRESULT.fields_by_name['no_with_veto']._options = None
    _TALLYRESULT.fields_by_name['no_with_veto']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xf2\xde\x1f\x13yaml:"no_with_veto"'
    _TALLYRESULT._options = None
    _TALLYRESULT._serialized_options = b'\xe8\xa0\x1f\x01'
    _VOTE.fields_by_name['proposal_id']._options = None
    _VOTE.fields_by_name['proposal_id']._serialized_options = b'\xf2\xde\x1f\x12yaml:"proposal_id"'
    _VOTE.fields_by_name['option']._options = None
    _VOTE.fields_by_name['option']._serialized_options = b'\x18\x01'
    _VOTE.fields_by_name['options']._options = None
    _VOTE.fields_by_name['options']._serialized_options = b'\xc8\xde\x1f\x00'
    _VOTE._options = None
    _VOTE._serialized_options = b'\x98\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _DEPOSITPARAMS.fields_by_name['min_deposit']._options = None
    _DEPOSITPARAMS.fields_by_name['min_deposit']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x15min_deposit,omitempty\xf2\xde\x1f\x12yaml:"min_deposit"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _DEPOSITPARAMS.fields_by_name['max_deposit_period']._options = None
    _DEPOSITPARAMS.fields_by_name['max_deposit_period']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x1cmax_deposit_period,omitempty\xf2\xde\x1f\x19yaml:"max_deposit_period"\x98\xdf\x1f\x01'
    _VOTINGPARAMS.fields_by_name['voting_period']._options = None
    _VOTINGPARAMS.fields_by_name['voting_period']._serialized_options = b'\xc8\xde\x1f\x00\xea\xde\x1f\x17voting_period,omitempty\xf2\xde\x1f\x14yaml:"voting_period"\x98\xdf\x1f\x01'
    _TALLYPARAMS.fields_by_name['quorum']._options = None
    _TALLYPARAMS.fields_by_name['quorum']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x10quorum,omitempty'
    _TALLYPARAMS.fields_by_name['threshold']._options = None
    _TALLYPARAMS.fields_by_name['threshold']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x13threshold,omitempty'
    _TALLYPARAMS.fields_by_name['veto_threshold']._options = None
    _TALLYPARAMS.fields_by_name['veto_threshold']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xea\xde\x1f\x18veto_threshold,omitempty\xf2\xde\x1f\x15yaml:"veto_threshold"'
    _globals['_VOTEOPTION']._serialized_start = 2620
    _globals['_VOTEOPTION']._serialized_end = 2850
    _globals['_PROPOSALSTATUS']._serialized_start = 2853
    _globals['_PROPOSALSTATUS']._serialized_end = 3185
    _globals['_WEIGHTEDVOTEOPTION']._serialized_start = 226
    _globals['_WEIGHTEDVOTEOPTION']._serialized_end = 375
    _globals['_TEXTPROPOSAL']._serialized_start = 377
    _globals['_TEXTPROPOSAL']._serialized_end = 444
    _globals['_DEPOSIT']._serialized_start = 447
    _globals['_DEPOSIT']._serialized_end = 623
    _globals['_PROPOSAL']._serialized_start = 626
    _globals['_PROPOSAL']._serialized_end = 1390
    _globals['_TALLYRESULT']._serialized_start = 1393
    _globals['_TALLYRESULT']._serialized_end = 1691
    _globals['_VOTE']._serialized_start = 1694
    _globals['_VOTE']._serialized_end = 1885
    _globals['_DEPOSITPARAMS']._serialized_start = 1888
    _globals['_DEPOSITPARAMS']._serialized_end = 2175
    _globals['_VOTINGPARAMS']._serialized_start = 2177
    _globals['_VOTINGPARAMS']._serialized_end = 2302
    _globals['_TALLYPARAMS']._serialized_start = 2305
    _globals['_TALLYPARAMS']._serialized_end = 2617