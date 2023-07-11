"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....evmos.incentives.v1 import query_pb2 as evmos_dot_incentives_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Incentives = channel.unary_unary('/evmos.incentives.v1.Query/Incentives', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesResponse.FromString)
        self.Incentive = channel.unary_unary('/evmos.incentives.v1.Query/Incentive', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveResponse.FromString)
        self.GasMeters = channel.unary_unary('/evmos.incentives.v1.Query/GasMeters', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersResponse.FromString)
        self.GasMeter = channel.unary_unary('/evmos.incentives.v1.Query/GasMeter', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterResponse.FromString)
        self.AllocationMeters = channel.unary_unary('/evmos.incentives.v1.Query/AllocationMeters', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersResponse.FromString)
        self.AllocationMeter = channel.unary_unary('/evmos.incentives.v1.Query/AllocationMeter', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterResponse.FromString)
        self.Params = channel.unary_unary('/evmos.incentives.v1.Query/Params', request_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Incentives(self, request, context):
        """Incentives retrieves registered incentives
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Incentive(self, request, context):
        """Incentive retrieves a registered incentive
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GasMeters(self, request, context):
        """GasMeters retrieves active gas meters for a given contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GasMeter(self, request, context):
        """GasMeter retrieves a active gas meter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocationMeters(self, request, context):
        """AllocationMeters retrieves active allocation meters for a given
        denomination
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocationMeter(self, request, context):
        """AllocationMeter retrieves a active gas meter
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params retrieves the incentives module params
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Incentives': grpc.unary_unary_rpc_method_handler(servicer.Incentives, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesResponse.SerializeToString), 'Incentive': grpc.unary_unary_rpc_method_handler(servicer.Incentive, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveResponse.SerializeToString), 'GasMeters': grpc.unary_unary_rpc_method_handler(servicer.GasMeters, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersResponse.SerializeToString), 'GasMeter': grpc.unary_unary_rpc_method_handler(servicer.GasMeter, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterResponse.SerializeToString), 'AllocationMeters': grpc.unary_unary_rpc_method_handler(servicer.AllocationMeters, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersResponse.SerializeToString), 'AllocationMeter': grpc.unary_unary_rpc_method_handler(servicer.AllocationMeter, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('evmos.incentives.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Incentives(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/Incentives', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentivesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Incentive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/Incentive', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryIncentiveResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GasMeters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/GasMeters', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMetersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GasMeter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/GasMeter', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryGasMeterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocationMeters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/AllocationMeters', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMetersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocationMeter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/AllocationMeter', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryAllocationMeterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.incentives.v1.Query/Params', evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString, evmos_dot_incentives_dot_v1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)