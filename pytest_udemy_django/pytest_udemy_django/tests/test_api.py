"""Starting point for testing my API"""

import os
import json
from unittest import TestCase

import pytest
from django.test import Client
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytest_udemy_django.settings")

DJANGO_SETTINGS_MODULE = "/home/steve/repositories/RuerupRechnerWebApplication/pytest_udemy_django/pytest_udemy_django/pytest_udemy_django/settings.py"


class TestGetContracts(TestCase):
    """Class containint my GET Contracts tests"""

    @pytest.mark.django_db
    def test_zero_contracts_should_return_empty_list(self) -> None:
        """No contracts - GET should return empty list"""
        client = Client()
        contracts_url = reverse(viewname="contracts-list")
        response = client.get(contracts_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])
