# this function just tranfers X amt of funds from my acc1 to acc2

import json
from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import PaymentTxn

data = json.load(open('Algorand Testing Github/variables.json') ) # I made this private

print(data['account1_mnemonic'])

def transfer_funds(amt):
    print("--------------------------------------------")
    print("Getting Accounts...")

    accounts = {}

    accounts[0] = {}
    accounts[0]['pk'] = mnemonic.to_public_key(data['account1_mnemonic'])
    accounts[0]['sk'] = mnemonic.to_private_key(data['account1_mnemonic'])

    accounts[1] = {}
    accounts[1]['pk'] = mnemonic.to_public_key(data['account2_mnemonic'])
    accounts[1]['sk'] = mnemonic.to_private_key(data['account2_mnemonic'])

    algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
    headers = {
        "X-API-Key": data['algod_token'],
    }
    algod_client = algod.AlgodClient(data['algod_token'], algod_address, headers)

    params = algod_client.suggested_params()
    params.flat_fee = True
    params.fee = amt
    receiver =  accounts[1]['pk'] #Account 2 Public Key
    note = "Test Fee".encode()

    unsigned_txn = PaymentTxn(accounts[0]['pk'], params, receiver, 1000000, None, note)

    signed_txn = unsigned_txn.sign( accounts[0]['sk'] )
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))



transfer_funds(1000)




