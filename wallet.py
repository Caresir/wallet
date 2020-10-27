import subprocess
import json
from constants import *
import os

def derive_wallets(mnemonic, coin, derive_count=10)

    mnemonic = os.getenv('MNEMONIC', 'pet panther clump shoulder express virtual lecture sport pink effort artefact balance bring jazz pilot')

    command = f'./derive -g --mnemonic= "{MNEMONIC}" --format=json --coin='{coin}' --numderive={derive_count}'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    print(keys)


def priv_key_to_account(coin, priv_key)
"""
convert the privkey string in a child key to an account object
that bit or web3.py can use to transact
"""

    if coin = "ETH":
        return Account.privateKeyToAccount(priv_key) 
    elif coin = "BTCTEST":
        return PrivateKeyTestnet(priv_key)
    return

