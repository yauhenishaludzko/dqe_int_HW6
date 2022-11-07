import pytest
import connections


cursor = connections.connect_db()


def test_row_count():
    cursor.execute('SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address]')
    for i in cursor:
        assert i[0] == 19614


def test_uniq_values():
    cursor.execute('SELECT COUNT(DISTINCT StateProvinceID) FROM [AdventureWorks2012].[Person].[Address]')
    for i in cursor:
        assert i[0] == 74


def test_null_values_count():
    cursor.execute('SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE AddressLine2 is not null')
    for i in cursor:
        assert i[0] == 362


def test_future_date():
    cursor.execute('SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE ModifiedDate > GETDATE()')
    for i in cursor:
        assert i[0] == 0


def test_flag_range():
    cursor.execute('SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE FolderFlag NOT IN (0,1)')
    for i in cursor:
        assert i[0] == 0


def test_owner_code():
    cursor.execute('SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE len(Owner) <> 3')
    for i in cursor:
        assert i[0] == 0


def test_duplicates():
    cursor.execute('SELECT [UnitMeasureCode],[Name],[ModifiedDate],COUNT(*) FROM [AdventureWorks2012].[Production].['
                   'UnitMeasure] GROUP BY [UnitMeasureCode],[Name],[ModifiedDate] HAVING COUNT(*) > 1')
    for i in cursor:
        assert i[0] == 0


def test_column_counts():
    cursor.execute('SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_catalog = \'AdventureWorks2012\' AND '
                   'table_name = \'UnitMeasure\'')
    for i in cursor:
        assert i[0] == 3


