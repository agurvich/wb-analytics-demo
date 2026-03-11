"""Shared pytest fixtures."""
import pytest


@pytest.fixture
def sample_incomes():
    return [1.0, 1.5, 2.0, 3.0, 5.0, 10.0]
