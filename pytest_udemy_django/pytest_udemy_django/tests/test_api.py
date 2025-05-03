"""Starting point for testing my API"""

import os
import json

import pytest
from django.urls import reverse
from rueruprechner.models import Contract

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytest_udemy_django.settings")

DJANGO_SETTINGS_MODULE = "/home/steve/repositories/RuerupRechnerWebApplication/pytest_udemy_django/pytest_udemy_django/pytest_udemy_django/settings.py"
CONTRACTS_URL = reverse(viewname="contracts-list")


@pytest.mark.django_db
def test_contract_magic_stringify_works() -> None:
    contract_object = Contract(name="Test Contract")
    assert str(contract_object) == "Test Contract"


@pytest.mark.django_db
def test_zero_contracts_should_return_empty_list(client) -> None:
    response = client.get(CONTRACTS_URL)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.django_db
def test_contract_creation_and_retrieval(client) -> None:
    test_contract = Contract.objects.create(
        name="Test Ruerup Contract",
        notes="Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
    )
    response = client.get(CONTRACTS_URL)
    response_content = json.loads(response.content)[0]
    assert response_content.get("name") == test_contract.name
    assert response_content.get("status") == "Draft"
    assert response_content.get("notes") == test_contract.notes
    test_contract.delete()


@pytest.mark.django_db
def test_post_empty_returns_error_and_info(client):
    response = client.post(CONTRACTS_URL)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


@pytest.mark.django_db
def test_post_company_already_exists(client):
    test_contract = Contract.objects.create(name="Unique Name")
    response = client.post(CONTRACTS_URL, data={"name": test_contract.name})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["contract with this name already exists."]
    }


@pytest.mark.django_db
def test_post_successful(client):
    test_company_name = "Test Company Name"
    response = client.post(CONTRACTS_URL, data={"name": test_company_name})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == test_company_name
    assert response_content.get("status") == "Draft"
    assert response_content.get("notes") == ""
    assert response_content.get("id") != ""
    assert response_content.get("last_update") != ""
