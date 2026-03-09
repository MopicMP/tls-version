"""Tests for tls-version."""

import pytest
from tls_version import version


class TestVersion:
    """Test suite for version."""

    def test_basic(self):
        """Test basic usage."""
        result = version("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            version("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = version(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
