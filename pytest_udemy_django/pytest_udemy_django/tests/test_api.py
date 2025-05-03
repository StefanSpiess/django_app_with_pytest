"""Starting point for testing my API"""

import os
import json
from unittest import TestCase

import pytest
from django.test import Client
from django.urls import reverse
from rueruprechner.models import Contract

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytest_udemy_django.settings")

DJANGO_SETTINGS_MODULE = "/home/steve/repositories/RuerupRechnerWebApplication/pytest_udemy_django/pytest_udemy_django/pytest_udemy_django/settings.py"


@pytest.mark.django_db
class BasicInitialization(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.contracts_url = reverse(viewname="contracts-list")


class TestGetContracts(BasicInitialization):
    def test_contract_magic_stringify_works(self) -> None:
        contract_object = Contract(name="Test Contract")
        self.assertEqual(str(contract_object), "Test Contract")

    def test_zero_contracts_should_return_empty_list(self) -> None:
        response = self.client.get(self.contracts_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_contract_creation_and_retrieval(self) -> None:
        test_contract = Contract.objects.create(
            name="Test Ruerup Contract",
            notes="Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
        )
        response = self.client.get(self.contracts_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response_content.get("name"), test_contract.name)
        self.assertEqual(response_content.get("status"), "Draft")
        self.assertEqual(response_content.get("notes"), test_contract.notes)
        test_contract.delete()


class TestPostContracts(BasicInitialization):
    def test_post_empty_returns_error_and_info(self):
        response = self.client.post(self.contracts_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_post_company_already_exists(self):
        test_contract = Contract.objects.create(name="Unique Name")
        response = self.client.post(
            self.contracts_url, data={"name": test_contract.name}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"name": ["contract with this name already exists."]},
        )

    def test_post_successful(self):
        test_company_name = "Test Company Name"
        response = self.client.post(
            self.contracts_url, data={"name": test_company_name}
        )
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), test_company_name)
        self.assertEqual(response_content.get("status"), "Draft")
        self.assertEqual(response_content.get("notes"), "")
        self.assertIsNotNone(response_content.get("id"))
        self.assertIsNotNone(response_content.get("last_update"))

    @pytest.mark.xfail
    def test_should_fail(self):
        self.assertEqual(1, 2)
