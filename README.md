The simplest Bitcoin Core RPC library for when you just want to talk to Bitcoin Core.

## Usage

If you started Bitcoin Core like this:

```bash
bitcoind -regtest -rpcuser=user -rpcpassword=pass
```

Instantiate the `bitcoin_requests` RPC client like this:

```python
from bitcoin_requests import BitcoinRPC

rpc = BitcoinRPC('http://127.0.0.1:18443', 'user', 'pass')
blocks = rpc.generate(101)
tx = rpc.sendtoaddress(address, 20)
```

## Installation

```
pip install bitcoin-requests
```
