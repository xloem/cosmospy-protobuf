"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.claims.v1 import query_pb2 as evmos_dot_claims_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TotalUnclaimed = channel.unary_unary('/evmos.claims.v1.Query/TotalUnclaimed', request_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedRequest.SerializeToString, response_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedResponse.FromString)
        self.Params = channel.unary_unary('/evmos.claims.v1.Query/Params', request_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)
        self.ClaimsRecords = channel.unary_unary('/evmos.claims.v1.Query/ClaimsRecords', request_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsRequest.SerializeToString, response_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsResponse.FromString)
        self.ClaimsRecord = channel.unary_unary('/evmos.claims.v1.Query/ClaimsRecord', request_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordRequest.SerializeToString, response_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def TotalUnclaimed(self, request, context):
        """TotalUnclaimed queries the total unclaimed tokens from the airdrop
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params returns the claims module parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClaimsRecords(self, request, context):
        """ClaimsRecords returns all claims records
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClaimsRecord(self, request, context):
        """ClaimsRecord returns the claims record for a given address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'TotalUnclaimed': grpc.unary_unary_rpc_method_handler(servicer.TotalUnclaimed, request_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedRequest.FromString, response_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'ClaimsRecords': grpc.unary_unary_rpc_method_handler(servicer.ClaimsRecords, request_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsRequest.FromString, response_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsResponse.SerializeToString), 'ClaimsRecord': grpc.unary_unary_rpc_method_handler(servicer.ClaimsRecord, request_deserializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordRequest.FromString, response_serializer=evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.claims.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def TotalUnclaimed(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.claims.v1.Query/TotalUnclaimed', evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedRequest.SerializeToString, evmos_dot_claims_dot_v1_dot_query__pb2.QueryTotalUnclaimedResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.claims.v1.Query/Params', evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, evmos_dot_claims_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClaimsRecords(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.claims.v1.Query/ClaimsRecords', evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsRequest.SerializeToString, evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClaimsRecord(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.claims.v1.Query/ClaimsRecord', evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordRequest.SerializeToString, evmos_dot_claims_dot_v1_dot_query__pb2.QueryClaimsRecordResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)