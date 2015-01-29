# coding: utf8

from fatores_primos import prime_factors


def test_3():
    assert {3: 1} == prime_factors(3)


def test_5():
    assert {5: 1} == prime_factors(5)


def test_6():
    assert {2: 1, 3: 1} == prime_factors(6)


def test_8():
    assert {2: 3} == prime_factors(8)


def test_100():
    assert {2: 2, 5: 2} == prime_factors(100)


def test_198():
    assert {2: 1, 3: 2, 11: 1} == prime_factors(198)


def test_276():
    assert {2: 2, 3: 1, 23: 1} == prime_factors(276)
