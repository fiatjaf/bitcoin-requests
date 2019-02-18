The simplest Bitcoin Core RPC library for when you're trying to test stuff.

```bash
bitcoind -regtest -rpcuser=user -rpcpassword=pass
```

```python
from bitcoin import BitcoinRPC

rpc = BitcoinRPC('http://127.0.0.1:18443', 'user', 'pass')
blocks = rpc.generate(101)
tx = rpc.sendtoaddress(address, 20)
```
