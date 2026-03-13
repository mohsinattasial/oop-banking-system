from datetime import date
from typing import List, Tuple

Txn = Tuple[str, str, float, float]


class Account:

    def __init__(self, account_id: str, owner: str):
        self.account_id = account_id
        self.owner = owner
        self.__balance: float = 0.0
        self._history: List[Txn] = []

    def _record(self, typ: str, amount: float) -> None:
        txn = (date.today().isoformat(), typ, amount, self.__balance)
        self._history.append(txn)

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount
        self._record("DEPOSIT", amount)

    def get_balance(self) -> float:
        return self.__balance

    def _set_balance(self, new_balance: float) -> None:
        self.__balance = new_balance

    def withdraw(self, amount: float) -> None:
        raise NotImplementedError

    def transfer(self, to: "Account", amount: float) -> None:

        if self.account_id == to.account_id:
            raise ValueError("Cannot transfer to same account")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.withdraw(amount)
        to.deposit(amount)

    def statement(self) -> List[Txn]:
        return list(self._history)


class SavingsAccount(Account):

    def withdraw(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        if self.get_balance() - amount < 0:
            raise ValueError("Insufficient balance")

        new_balance = self.get_balance() - amount
        self._set_balance(new_balance)

        self._record("WITHDRAW", amount)


class CurrentAccount(Account):

    def __init__(self, account_id: str, owner: str, overdraft_limit: float = 5000):

        super().__init__(account_id, owner)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:

        if amount <= 0:
            raise ValueError("Amount must be positive")

        new_balance = self.get_balance() - amount

        if new_balance < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

        self._set_balance(new_balance)
        self._record("WITHDRAW", amount)