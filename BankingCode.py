class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        else:
            return "Invalid deposit amount"


# Creating test cases using pytest

import pytest

@pytest.fixture
def new_account():
    return Account("123456", 1000)

def test_withdraw_sufficient_balance(new_account):
    withdrawn_amount = new_account.withdraw(500)
    assert withdrawn_amount == 500
    assert new_account.balance == 500

def test_withdraw_insufficient_balance(new_account):
    withdrawn_amount = new_account.withdraw(1500)
    assert withdrawn_amount == "Insufficient balance"
    assert new_account.balance == 1000

def test_deposit_valid_amount(new_account):
    deposited_amount = new_account.deposit(300)
    assert deposited_amount == 300
    assert new_account.balance == 1300

def test_deposit_invalid_amount(new_account):
    deposited_amount = new_account.deposit(-100)
    assert deposited_amount == "Invalid deposit amount"
    assert new_account.balance == 1000

if __name__ == "__main__":
    pytest.main()
