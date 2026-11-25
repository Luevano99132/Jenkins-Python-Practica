import pytest
import Conversion as con

def test_celsius_a_fahrenheit():
    # 0 grados Celsius son 32 Fahrenheit
    assert con.celsius_a_fahrenheit(0) == 32
    # 100 grados Celsius son 212 Fahrenheit
    assert con.celsius_a_fahrenheit(100) == 212

def test_fahrenheit_a_celsius():
    # 32 Fahrenheit son 0 Celsius
    assert con.fahrenheit_a_celsius(32) == 0
    # 212 Fahrenheit son 100 Celsius
    assert con.fahrenheit_a_celsius(212) == 100
