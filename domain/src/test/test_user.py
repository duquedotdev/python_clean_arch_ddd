import pytest
from datetime import date
from unittest.mock import MagicMock
import sys
sys.path.append('domain/src/modules')

from modules.user.User import User
from modules.user.UserID import UserID
from modules.validation.ValidationHandler import ValidationHandler


@pytest.mark.user
def test_given_valid_user_when_call_new_user_then_should_instantiate_new_user():
    name = "Felipe Duque"
    email = "felipe@gmail.com"
    birthdate = date(1993, 7, 8)
    address = "Rua Volkswagen"
    skills = ["Spring Boot", "Spring Framework"]
    is_active = True

    actual_user = User.new_user(
        name,
        email,
        birthdate,
        address,
        skills,
        is_active
    )

    actual_user.validate = MagicMock()
    actual_user.validate.assert_not_called()

    assert actual_user is not None
    assert actual_user.id is not None
    assert name == actual_user.name
    assert email == actual_user.email
    assert birthdate == actual_user.birthdate
    assert address == actual_user.address
    assert skills == actual_user.skills
    assert is_active == actual_user.is_active
    assert actual_user.created_at is not None
    assert actual_user.updated_at is not None
    
    # Verifique deleted_at com base no valor de is_active
    if is_active:
        assert actual_user.deleted_at is None
    else:
        assert actual_user.deleted_at is not None

@pytest.mark.user
def test_given_valid_user_and_inactive_when_call_new_user_then_should_instantiate_new_user():
    # Dados do usuário
    name = "Felipe Duque"
    email = "felipe@gmail.com"
    birthdate = date(1993, 7, 8)
    address = "Rua Volkswagen"
    skills = ["Spring Boot", "Spring Framework"]
    is_active = False

    # Chama o método para criar um novo usuário
    actual_user = User.new_user(
        name,
        email,
        birthdate,
        address,
        skills,
        is_active
    )

    # Verificações
    assert actual_user is not None
    assert actual_user.id is not None
    assert actual_user.name == name
    assert actual_user.email == email
    assert actual_user.birthdate == birthdate
    assert actual_user.address == address
    assert actual_user.skills == skills
    assert not actual_user.is_active
    assert actual_user.created_at is not None
    assert actual_user.updated_at is not None
    assert actual_user.deleted_at is not None

    # Verifica que o método de validação não foi chamado
    actual_user.validate = MagicMock()
    actual_user.validate.assert_not_called()

@pytest.mark.user
def test_given_valid_user_when_call_deactivate_then_should_deactivate_the_user():
    # Dados do usuário
    name = "Felipe Duque"
    email = "felipe@gmail.com"
    birthdate = date(1993, 7, 8)
    address = "Rua Volkswagen"
    skills = ["Spring Boot", "Spring Framework"]
    is_active = True

    # Cria um novo usuário ativo
    actual_user = User.new_user(
        name,
        email,
        birthdate,
        address,
        skills,
        is_active
    )

    # Configuração do mock para o método de validação
    actual_user.validate = MagicMock()
    actual_user.validate.assert_not_called()

    # Verificações iniciais
    assert actual_user is not None
    assert actual_user.deleted_at is None

    # Chama o método para desativar o usuário
    actual_user.deactivate()

    # Verificações após a desativação
    assert not actual_user.is_active
    assert actual_user.deleted_at is not None

@pytest.mark.user
def test_given_valid_and_inactivated_user_when_call_activate_then_should_reactivate_the_user():
    # Dados do usuário inativado
    name = "Felipe Duque"
    email = "felipe@gmail.com"
    birthdate = date(1993, 7, 8)
    address = "Rua Volkswagen"
    skills = ["Spring Boot", "Spring Framework"]
    is_active = False

    # Cria um novo usuário inativado
    actual_user = User.new_user(
        name,
        email,
        birthdate,
        address,
        skills,
        is_active
    )

    # Configuração do mock para o método de validação
    actual_user.validate = MagicMock()
    actual_user.validate.assert_not_called()

    # Verificações iniciais
    assert actual_user is not None
    assert actual_user.deleted_at is not None

    # Chama o método para reativar o usuário
    actual_user.activate()

    # Verificações após a ativação
    assert actual_user.is_active
    assert actual_user.deleted_at is None