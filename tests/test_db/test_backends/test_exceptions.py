# -*- coding: utf-8 -*-

from django_test_migrations.db.backends import exceptions


def test_DatabaseConfigurationNotFound():  # noqa: N802
    """Ensure exception returns proper string representation."""
    vendor = 'ms_sql'
    exception = exceptions.DatabaseConfigurationNotFound(vendor)
    assert vendor in str(exception)


def test_DatabaseConfigurationSettingNotFound():  # noqa: N802
    """Ensure exception returns proper string representation."""
    vendor = 'ms_sql'
    setting_name = 'fake_setting'
    exception = exceptions.DatabaseConfigurationSettingNotFound(
        vendor,
        setting_name,
    )
    assert vendor in str(exception)
    assert setting_name in str(exception)
