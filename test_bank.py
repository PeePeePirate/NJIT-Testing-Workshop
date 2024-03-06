from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawalException, BalanceRetrievalException
import pytest

def test_view_balance_success():
    """
    This is a generic test for the happy path
    It is testing view_balance with a good value (100)
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username='name', balance=100)
    # Act - do the action that we are testing
    actual_balance = bank_account.view_balance()
    # Assert - Assert that our expected outcome happened. could be assert something equals a value, assert something is true, assert an exception is raised
    assert actual_balance == 100

def test_view_balance_unsuccessful():
    """
    This is a generic test for the unhappy path (error)
    It is testing that view_balance with a bad value (-100) raises an exception
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username='name', balance=-100)
    # Assert - Assert that an exception is raised
    with pytest.raises(BalanceRetrievalException):
        # Act - do the action that we are testing
        bank_account.view_balance()

def test_deposit_function():
    bank_account = BankAccount(username='name', balance=100)

    bank_account.deposit(10)

    assert bank_account.view_balance() == 110