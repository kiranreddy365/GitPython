import pytest

#Grouping tests

@pytest.mark.one
def test01_login():
    print("This is Login test")

@pytest.mark.Two
def test02_regd():
    print("This is Registration test")

@pytest.mark.one
def test03_book():
    print("This is Booking test")

@pytest.mark.Two
def test03_Cancel():
    print("This is Cancelling test")