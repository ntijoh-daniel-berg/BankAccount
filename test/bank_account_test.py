#encoding: utf-8

from nose.tools import *
from lib.bank_account import BankAccount


def test_bank_account_requires_an_account_number():
    assert_raises(TypeError, BankAccount)
    assert_raises(TypeError, BankAccount, amount=1300)


def test_bank_account_requires_an_amount():
    assert_raises(TypeError, BankAccount)
    assert_raises(TypeError, BankAccount, account_number=12)


def test_bank_account_has_an_account_number():
    b = BankAccount(account_number=12, amount=1300)
    assert_equal(b.account_number, 12)


def test_bank_account_has_a_balance():
    bank_account = BankAccount(account_number=12, amount=1300)
    assert_equal(bank_account.balance, 1300)


@raises(AttributeError)
def test_amount_can_not_be_accessed():
    bank_account = BankAccount(account_number=12, amount=1300)
    bank_account.amount
    bank_account.amount()

@raises(AttributeError)
def test_account_number_can_not_be_modified():
    bank_account = BankAccount(account_number=12, amount=1300)
    bank_account.account_number = 32


@raises(AttributeError)
def test_balance_can_not_be_modified():
    bank_account = BankAccount(account_number=12, amount=1300)
    bank_account.balance += 323


def test_deposit_increases_balance_correctly():
    bank_account = BankAccount(account_number=12, amount=1300)
    assert_equal(bank_account.balance, 1300)
    bank_account.deposit(amount=300)
    assert_equal(bank_account.balance, 1600)


def test_withdraw_decreeases_balance_correctly():
    bank_account = BankAccount(account_number=12, amount=1300)
    assert_equal(bank_account.balance, 1300)
    bank_account.withdraw(amount=250)
    assert_equal(bank_account.balance, 1050)
