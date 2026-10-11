"""
Fixtures compartilhadas para os testes
"""
import pytest
import sys
import os

# Adiciona o diretório raiz ao path para importar a aplicação
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def app_context():
    """Cria um contexto de aplicação para testes"""
    with app.app_context() as ctx:
        yield ctx
