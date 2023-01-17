# -*- coding: utf-8 -*-
"""q2_3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kb4JfovLt-DPXuVw9AnJwAx1TXWGzOux
"""

#from google.colab import files
#uploaded = files.upload()

#!pip install python-bitcoinlib
#!pip install pycryptodome

import bitcoin.wallet
from bitcoin.core import COIN, b2lx, serialize, x, lx, b2x

from utils import *
from bitcoin.core.script import CScript, OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG, SignatureHash, SIGHASH_ALL,OP_TRUE,OP_RETURN
from q2_3_1 import primeNum1, primeNum2, add, sub

bitcoin.SelectParams("testnet")
my_private_key = bitcoin.wallet.CBitcoinSecret("92i3QHTdRhrUN8qhQ3vSuYqT55JrYvZuTUPwzYKMikAeVgGbXTZ")
print(my_private_key)
my_public_key = my_private_key.pub
my_address = bitcoin.wallet.P2PKHBitcoinAddress.from_pubkey(my_public_key)
print(my_address)
    
def P2PKH_scriptPubKey(address):
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]

def prime_P2PKH_scriptSig():
    return [primeNum1, primeNum2]

def prime_P2PKH_scriptPubkey():
    return [OP_2DUP, OP_ADD, add, OP_EQUALVERIFY, OP_SUB, sub, OP_EQUAL]

def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index,
                                txout_scriptPubKey):
    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = prime_P2PKH_scriptPubkey()
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = prime_P2PKH_scriptSig()

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx)

print(prime_P2PKH_scriptSig())

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.0005
    txid_to_spend = ('a659879239018a27d6d23e594f35a20bfb60b6e1c5c1319a5984e86d765eac2a') 
    utxo_index = 0
    ######################################################################

    print(my_address) 
    print(my_public_key.hex()) 
    print(my_private_key.hex()) 
    txout_scriptPubKey = P2PKH_scriptPubKey(my_address)
    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)