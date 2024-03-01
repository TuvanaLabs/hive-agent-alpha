from typing import Dict

from solcx import install_solc, compile_source
from web3 import Web3

contracts = {}

web3_instance = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

def compile_solidity(src: str) -> Dict:
    install_solc("0.8.0")
    compiled_sol = compile_source(
        src,
        output_values=['abi', 'bin'],
        solc_version="0.8.0"
    )

    contract_id, contract_interface = compiled_sol.popitem()
    if contract_interface['bin'] == '':
        contract_id, contract_interface = compiled_sol.popitem()

    return contract_interface

def deploy_contract(source_code: str) -> str:
    """
    Is responsible for deploying a provided Solidity smart contract.
    """
    compiled = compile_solidity(src=source_code)

    UserContract = web3_instance.eth.contract(abi=compiled['abi'], bytecode=compiled['bin'])
    web3_instance.eth.default_account = web3_instance.eth.accounts[0]

    tx_hash = UserContract.constructor().transact()
    tx_receipt = web3_instance.eth.wait_for_transaction_receipt(tx_hash)
    address = tx_receipt.contractAddress

    contracts[address] = compiled['abi']

    return address


def load_contract(addr: str) -> any:
    abi = contracts[addr]
    contract = web3_instance.eth.contract(
        address=addr,
        abi=abi
    )

    return contract

def transfer(contract_address: str, recipient_address: str, amount: int) -> str:
    """
    Is responsible for transferring tokens to an address when provided the recipient address and amount.
    """

    UserContract = load_contract(contract_address)
    tx_hash = UserContract.functions.transfer(recipient_address, amount).transact()
    tx_receipt = web3_instance.eth.wait_for_transaction_receipt(tx_hash)

    return tx_hash

def get_account_balance(contract_address: str, account: str) -> any:
    """
    Is responsible for retrieving the token balance of an account.
    """

    UserContract = load_contract(contract_address)
    balance = UserContract.functions.balanceOf(account).call()
    
    return balance
