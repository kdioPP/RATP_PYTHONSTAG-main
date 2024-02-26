import sys
sys.path.append('src')
from calcul_tarif import calcul_tarif
import pytest
from unittest.mock import Mock


@pytest.fixture
def fix_setUpTearDown():
    print("before")
    yield
    print("after")

def test_enfant_parisien(fix_setUpTearDown):
    calcul = calcul_tarif()
    y=calcul.tarif(4,False)
    assert y == 0.75

def test_enfant_touriste():
    calcul = calcul_tarif()
    y=calcul.tarif(4,True)
    assert y == 1.5

def test_adulte_parisien():
    calcul = calcul_tarif()
    y=calcul.tarif(24,False)
    assert y == 1.5

def test_adulte_touriste(mocker):
    mocker.patch ('calcul_tarif.calcul_tarif.get', return_value = 1.4)
    calcul = calcul_tarif()
    y=calcul.tarif(24,True)
    calcul_tarif.get.assert_called_once_with()
    assert y == 3.0
