from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawalException, BalanceRetrievalException
import pytest

def test_view_balance_success():
    bank_account = BankAccount(username='name', balance=100)
    actual_balance = bank_account.view_balance()
    assert actual_balance == 100

def test_view_balance_unsuccessful():
    bank_account = BankAccount(username='name', balance=-100)
    with pytest.raises(BalanceRetrievalException):
        bank_account.view_balance()

def test_deposit_success():
    bank_account = BankAccount(username='name', balance=100)
    deposit_balance = bank_account.deposit(60)
    assert deposit_balance == 160
    
def test_deposit_unsuccess():
    bank_account = BankAccount(username='name', balance=100)
    deposit_balance = bank_account.view_balance('a')
    with pytest.raises(InternalDepositException):
        bank_account.view_balance()