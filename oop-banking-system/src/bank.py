from typing import Dict
from .account import Account


class Bank:

    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def open_account(self, account: Account) -> None:

        if account.account_id in self.accounts:
            raise ValueError("Account ID already exists")

        self.accounts[account.account_id] = account

    def get_account(self, account_id: str) -> Account:

        if account_id not in self.accounts:
            raise KeyError("Account not found")

        return self.accounts[account_id]

    def transfer(self, from_id: str, to_id: str, amount: float) -> None:

        from_account = self.get_account(from_id)
        to_account = self.get_account(to_id)

        from_account.transfer(to_account, amount)