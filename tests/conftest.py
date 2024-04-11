import pytest
import pymssql


@pytest.fixture(scope='module')
def cnxn():
    """Pytest fixture to establish connection to DB"""
    cnxn = pymssql.connect(
        host='192.168.0.104',
        user='shell84',
        password='zQ692U3d!',
        database='AdventureWorks2012',
        port=1433)

    yield cnxn


@pytest.fixture
def cursor(cnxn):
    """Pytest fixture for creating cursor"""
    cursor = cnxn.cursor()
    yield cursor
    cnxn.rollback()