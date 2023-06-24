import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import google
from .... import cosmos
from .... import interchain_security

class QueryBase(abc.ABC):

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        pass