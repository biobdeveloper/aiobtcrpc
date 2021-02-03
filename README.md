# AioBtcRpc

Modern Python3 async [aiohttp](https://github.com/aio-libs/aiohttp )-based JSONRPC client 
for [Bitcoin Core](https://github.com/bitcoin/bitcoin ). 

Allow to use any [Bitcoin RPC method](https://developer.bitcoin.org/reference/rpc/)


![License]

# Install
```bash
pip install aiobtcrpc
```

# Usage
Pretty simple: 

`await BitcoinCoreClient.anybitcoinrpcmethodname(*args_in_order_like_in_the_docs)`
```python
import asyncio
from aiobtcrpc import BitcoinCoreClient, JSONRPCException


async def test():
    # Create client object by providing rpc-server url to BitcoinCoreClient class
    cli = BitcoinCoreClient(rpc_url="https://USER:PASSWROD@HOST:PORT")

    # Just execute cli.ANY_RPC_COMMAND(*args)
    balance = await cli.getbalance()

    # all float values returns as python decimal.Decimal object
    print(balance)
    # >>> 0.02587228

    # Unlock your wallet
    unlock = await cli.walletpassphrase("Your wallet.dat server bitcoin password", 10)

    # Donate me
    donate_tx = await cli.sendtoaddress("1EWGKaAdof35pdjBnQW9xh7dwRVJkA8vUR", 0.01)
    print(donate_tx)
    # >>> bd38d3e6c7ab8c25e183e818829e1f0e179af12ef418fa6f4f27c76ef77c924

    # Errors are raises as JSONRPCException with code and message
    try:
        await cli.walletpassphrase("BadPassword")
    except JSONRPCException as ex:
        print(ex.message)
        # >>> -14 Error: The wallet passphrase entered was incorrect.

asyncio.run(test())
```

[License]: https://img.shields.io/github/license/biobdeveloper/zverobot
[Python]: https://img.shields.io/pypi/pyversions/aiobtcrpc
