import pytest

from aiobtcrpc import BitcoinCoreClient


def test_bad_config():
    with pytest.raises(TypeError):
        BitcoinCoreClient(rpc_url="")
