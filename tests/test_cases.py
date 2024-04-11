def test_row_count(cursor):
    """Check on row count in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address]'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 19614


def test_uniq_values(cursor):
    """Check on unique values count in particular table"""
    query ='SELECT COUNT(DISTINCT StateProvinceID) FROM [AdventureWorks2012].[Person].[Address]'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 74


def test_null_values_count(cursor):
    """Check on not null values count of values in particular column of table"""
    query ='SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE AddressLine2 is not null'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 362


def test_future_date(cursor):
    """Check on date validity in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE ModifiedDate > GETDATE()'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 0


def test_flag_range(cursor):
    """Check on validity by list of values in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE FolderFlag NOT IN (0,1)'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 0


def test_owner_code(cursor):
    """Check on value length in particular column of table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE len(Owner) <> 3'
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    assert result == 0


def test_duplicates(cursor):
    """Check on duplicates by key columns"""
    query = 'SELECT [UnitMeasureCode], [Name], [ModifiedDate], COUNT(*) FROM [AdventureWorks2012].[Production].[UnitMeasure] GROUP BY [UnitMeasureCode], [Name], [ModifiedDate] HAVING COUNT(*) > 1'
    cursor.execute(query)
    result = cursor.fetchall()
    assert result == []


def test_column_counts(cursor):
    """Check on column counts in table"""
    cursor.execute('SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_catalog = \'AdventureWorks2012\' AND '
                   'table_name = \'UnitMeasure\'')
    result = cursor.fetchall()[0][0]
    assert result == 3


