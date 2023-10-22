"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.staking.v1beta1 import query_pb2 as cosmos_dot_staking_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Validators = channel.unary_unary('/cosmos.staking.v1beta1.Query/Validators', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.FromString)
        self.Validator = channel.unary_unary('/cosmos.staking.v1beta1.Query/Validator', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.FromString)
        self.ValidatorDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/ValidatorDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.FromString)
        self.ValidatorUnbondingDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.FromString)
        self.Delegation = channel.unary_unary('/cosmos.staking.v1beta1.Query/Delegation', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.FromString)
        self.UnbondingDelegation = channel.unary_unary('/cosmos.staking.v1beta1.Query/UnbondingDelegation', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.FromString)
        self.DelegatorDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.FromString)
        self.DelegatorUnbondingDelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.FromString)
        self.Redelegations = channel.unary_unary('/cosmos.staking.v1beta1.Query/Redelegations', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.FromString)
        self.DelegatorValidators = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorValidators', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString)
        self.DelegatorValidator = channel.unary_unary('/cosmos.staking.v1beta1.Query/DelegatorValidator', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.FromString)
        self.HistoricalInfo = channel.unary_unary('/cosmos.staking.v1beta1.Query/HistoricalInfo', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.FromString)
        self.Pool = channel.unary_unary('/cosmos.staking.v1beta1.Query/Pool', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString)
        self.Params = channel.unary_unary('/cosmos.staking.v1beta1.Query/Params', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.TokenizeShareRecordById = channel.unary_unary('/cosmos.staking.v1beta1.Query/TokenizeShareRecordById', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdResponse.FromString)
        self.TokenizeShareRecordByDenom = channel.unary_unary('/cosmos.staking.v1beta1.Query/TokenizeShareRecordByDenom', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomResponse.FromString)
        self.TokenizeShareRecordsOwned = channel.unary_unary('/cosmos.staking.v1beta1.Query/TokenizeShareRecordsOwned', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedResponse.FromString)
        self.AllTokenizeShareRecords = channel.unary_unary('/cosmos.staking.v1beta1.Query/AllTokenizeShareRecords', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsResponse.FromString)
        self.LastTokenizeShareRecordId = channel.unary_unary('/cosmos.staking.v1beta1.Query/LastTokenizeShareRecordId', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdResponse.FromString)
        self.TotalTokenizeSharedAssets = channel.unary_unary('/cosmos.staking.v1beta1.Query/TotalTokenizeSharedAssets', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsRequest.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsResponse.FromString)
        self.TotalLiquidStaked = channel.unary_unary('/cosmos.staking.v1beta1.Query/TotalLiquidStaked', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStaked.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStakedResponse.FromString)
        self.TokenizeShareLockInfo = channel.unary_unary('/cosmos.staking.v1beta1.Query/TokenizeShareLockInfo', request_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfo.SerializeToString, response_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfoResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Validators(self, request, context):
        """Validators queries all validators that match the given status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Validator(self, request, context):
        """Validator queries validator info for given validator address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorDelegations(self, request, context):
        """ValidatorDelegations queries delegate info for given validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidatorUnbondingDelegations(self, request, context):
        """ValidatorUnbondingDelegations queries unbonding delegations of a validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delegation(self, request, context):
        """Delegation queries delegate info for given validator delegator pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnbondingDelegation(self, request, context):
        """UnbondingDelegation queries unbonding info for given validator delegator
        pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorDelegations(self, request, context):
        """DelegatorDelegations queries all delegations of a given delegator address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorUnbondingDelegations(self, request, context):
        """DelegatorUnbondingDelegations queries all unbonding delegations of a given
        delegator address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Redelegations(self, request, context):
        """Redelegations queries redelegations of given address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorValidators(self, request, context):
        """DelegatorValidators queries all validators info for given delegator
        address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelegatorValidator(self, request, context):
        """DelegatorValidator queries validator info for given delegator validator
        pair.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HistoricalInfo(self, request, context):
        """HistoricalInfo queries the historical info for given height.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pool(self, request, context):
        """Pool queries the pool info.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Parameters queries the staking parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeShareRecordById(self, request, context):
        """Query for individual tokenize share record information by share by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeShareRecordByDenom(self, request, context):
        """Query for individual tokenize share record information by share denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeShareRecordsOwned(self, request, context):
        """Query tokenize share records by address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllTokenizeShareRecords(self, request, context):
        """Query for all tokenize share records
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LastTokenizeShareRecordId(self, request, context):
        """Query for last tokenize share record id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalTokenizeSharedAssets(self, request, context):
        """Query for total tokenized staked assets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalLiquidStaked(self, request, context):
        """Query for total liquid staked (including tokenized shares or owned by an liquid staking provider)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenizeShareLockInfo(self, request, context):
        """Query tokenize share locks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Validators': grpc.unary_unary_rpc_method_handler(servicer.Validators, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.SerializeToString), 'Validator': grpc.unary_unary_rpc_method_handler(servicer.Validator, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.SerializeToString), 'ValidatorDelegations': grpc.unary_unary_rpc_method_handler(servicer.ValidatorDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.SerializeToString), 'ValidatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(servicer.ValidatorUnbondingDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.SerializeToString), 'Delegation': grpc.unary_unary_rpc_method_handler(servicer.Delegation, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.SerializeToString), 'UnbondingDelegation': grpc.unary_unary_rpc_method_handler(servicer.UnbondingDelegation, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.SerializeToString), 'DelegatorDelegations': grpc.unary_unary_rpc_method_handler(servicer.DelegatorDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.SerializeToString), 'DelegatorUnbondingDelegations': grpc.unary_unary_rpc_method_handler(servicer.DelegatorUnbondingDelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.SerializeToString), 'Redelegations': grpc.unary_unary_rpc_method_handler(servicer.Redelegations, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.SerializeToString), 'DelegatorValidators': grpc.unary_unary_rpc_method_handler(servicer.DelegatorValidators, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.SerializeToString), 'DelegatorValidator': grpc.unary_unary_rpc_method_handler(servicer.DelegatorValidator, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.SerializeToString), 'HistoricalInfo': grpc.unary_unary_rpc_method_handler(servicer.HistoricalInfo, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.SerializeToString), 'Pool': grpc.unary_unary_rpc_method_handler(servicer.Pool, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'TokenizeShareRecordById': grpc.unary_unary_rpc_method_handler(servicer.TokenizeShareRecordById, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdResponse.SerializeToString), 'TokenizeShareRecordByDenom': grpc.unary_unary_rpc_method_handler(servicer.TokenizeShareRecordByDenom, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomResponse.SerializeToString), 'TokenizeShareRecordsOwned': grpc.unary_unary_rpc_method_handler(servicer.TokenizeShareRecordsOwned, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedResponse.SerializeToString), 'AllTokenizeShareRecords': grpc.unary_unary_rpc_method_handler(servicer.AllTokenizeShareRecords, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsResponse.SerializeToString), 'LastTokenizeShareRecordId': grpc.unary_unary_rpc_method_handler(servicer.LastTokenizeShareRecordId, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdResponse.SerializeToString), 'TotalTokenizeSharedAssets': grpc.unary_unary_rpc_method_handler(servicer.TotalTokenizeSharedAssets, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsRequest.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsResponse.SerializeToString), 'TotalLiquidStaked': grpc.unary_unary_rpc_method_handler(servicer.TotalLiquidStaked, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStaked.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStakedResponse.SerializeToString), 'TokenizeShareLockInfo': grpc.unary_unary_rpc_method_handler(servicer.TokenizeShareLockInfo, request_deserializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfo.FromString, response_serializer=cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfoResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.staking.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Validators(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Validators', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Validator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Validator', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/ValidatorDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidatorUnbondingDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryValidatorUnbondingDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delegation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Delegation', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnbondingDelegation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/UnbondingDelegation', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryUnbondingDelegationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorUnbondingDelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorUnbondingDelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Redelegations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Redelegations', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryRedelegationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorValidators(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorValidators', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelegatorValidator(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/DelegatorValidator', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryDelegatorValidatorResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HistoricalInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/HistoricalInfo', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryHistoricalInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Pool', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryPoolResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/Params', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenizeShareRecordById(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TokenizeShareRecordById', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByIdResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenizeShareRecordByDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TokenizeShareRecordByDenom', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordByDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenizeShareRecordsOwned(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TokenizeShareRecordsOwned', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareRecordsOwnedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllTokenizeShareRecords(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/AllTokenizeShareRecords', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryAllTokenizeShareRecordsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LastTokenizeShareRecordId(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/LastTokenizeShareRecordId', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryLastTokenizeShareRecordIdResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalTokenizeSharedAssets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TotalTokenizeSharedAssets', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsRequest.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalTokenizeSharedAssetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalLiquidStaked(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TotalLiquidStaked', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStaked.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTotalLiquidStakedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenizeShareLockInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.staking.v1beta1.Query/TokenizeShareLockInfo', cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfo.SerializeToString, cosmos_dot_staking_dot_v1beta1_dot_query__pb2.QueryTokenizeShareLockInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)