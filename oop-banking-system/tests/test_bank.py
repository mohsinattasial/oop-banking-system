import unittest
from src.bank import Bank
from src.account import SavingsAccount, CurrentAccount


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

        self.acc1 = SavingsAccount("A1","Ali")
        self.acc2 = CurrentAccount("A2","Ahmed")

        self.bank.open_account(self.acc1)
        self.bank.open_account(self.acc2)

    def test_deposit(self):
        self.acc1.deposit(1000)
        self.assertEqual(self.acc1.get_balance(),1000)

    def test_savings_overdraft_not_allowed(self):
        with self.assertRaises(ValueError):
            self.acc1.withdraw(100)

    def test_current_overdraft_allowed(self):
        self.acc2.withdraw(1000)
        self.assertEqual(self.acc2.get_balance(),-1000)

    def test_overdraft_limit(self):
        with self.assertRaises(ValueError):
            self.acc2.withdraw(6000)

    def test_transfer(self):
        self.acc1.deposit(1000)
        self.bank.transfer("A1","A2",500)

        self.assertEqual(self.acc1.get_balance(),500)
        self.assertEqual(self.acc2.get_balance(),500)

    def test_transfer_same_account(self):
        with self.assertRaises(ValueError):
            self.acc1.transfer(self.acc1,100)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.acc1.deposit(-10)

    def test_negative_withdraw(self):
        with self.assertRaises(ValueError):
            self.acc1.withdraw(-10)

    def test_account_lookup(self):
        acc = self.bank.get_account("A1")
        self.assertEqual(acc.owner,"Ali")

    def test_invalid_account(self):
        with self.assertRaises(KeyError):
            self.bank.get_account("X")


if __name__ == "__main__":
    unittest.main()