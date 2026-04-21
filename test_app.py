import pytest

def calcular_imc(peso, altura):
    return round(peso / (altura * altura), 2)

# Teste 1: IMC padrão
def test_imc_padrao():
    assert calcular_imc(80, 1.80) == 24.69

# Teste 2: IMC baixo peso
def test_imc_baixo():
    assert calcular_imc(50, 1.70) == 17.3

# Teste 3: IMC sobrepeso
def test_imc_sobrepeso():
    assert calcular_imc(100, 1.75) == 32.65

# Teste 4: IMC valor exato
def test_imc_limite():
    assert calcular_imc(70, 1.67) == 25.1

# Teste 5: Pessoa muito alta
def test_imc_alto():
    assert calcular_imc(90, 2.00) == 22.5