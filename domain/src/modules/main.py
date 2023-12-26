import unittest
from Identifier import Identifier
from Entity import Entity

class TestIdentifier(unittest.TestCase):
    def test_identifier_creation(self):
        # Criando uma instância de Identifier (ajuste conforme necessário)
        identifier = Identifier("example_id")

        # Criando uma instância de Entity
        entity = Entity(identifier)

        # Verificando se o ID da entidade é o esperado
        self.assertEqual(entity.get_id(), identifier)

class TestEntity(unittest.TestCase):
    def test_entity_creation(self):
        # Criando uma instância de Identifier (ajuste conforme necessário)
        identifier = Identifier("example_id")

        # Criando uma instância de Entity
        entity = Entity(identifier)

        # Verificando se o ID da entidade é o esperado
        self.assertEqual(entity.get_id(), identifier)

        # Verificando se a lista de eventos de domínio está vazia inicialmente
        self.assertEqual(entity.get_domain_events(), list())

        # Verificando se o método has_error retorna False inicialmente
        self.assertFalse(entity.has_error())

        # Verificando se o método first_error retorna None inicialmente
        self.assertIsNone(entity.first_error())

if __name__ == '__main__':
    unittest.main()
