from ..call_builder_sync.call_builder import CallBuilder
from ...client.base_sync_client import BaseSyncClient


class RootCallBuilder(CallBuilder):
    """Creates a new :class:`RootCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.root`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(self, horizon_url: str, client: BaseSyncClient) -> None:
        super().__init__(horizon_url, client)