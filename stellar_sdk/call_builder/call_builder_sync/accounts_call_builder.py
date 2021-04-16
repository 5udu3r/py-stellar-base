from ..base.accounts_call_builder import AccountsCallBuilder as BaseAccountsCallBuilder
from ..call_builder_sync.call_builder import CallBuilder
from ...client.base_sync_client import BaseSyncClient


class AccountsCallBuilder(CallBuilder, BaseAccountsCallBuilder):
    """Creates a new :class:`AccountsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.accounts`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(self, horizon_url, client: BaseSyncClient) -> None:
        super().__init__(horizon_url, client)