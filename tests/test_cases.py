def test_row_count():
    """Check on row count in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address]'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 19613


def test_uniq_values():
    """Check on unique values count in particular table"""
    query ='SELECT COUNT(DISTINCT StateProvinceID) FROM [AdventureWorks2012].[Person].[Address]'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 74


def test_null_values_count():
    """Check on not null values count of values in particular column of table"""
    query ='SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE AddressLine2 is not null'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 362


def test_future_date():
    """Check on date validity in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address] WHERE ModifiedDate > GETDATE()'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 0


def test_flag_range():
    """Check on validity by list of values in particular table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE FolderFlag NOT IN (0,1)'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 0


def test_owner_code():
    """Check on value length in particular column of table"""
    query = 'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE len(Owner) <> 3'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 0


def test_duplicates():
    """Check on duplicates by key columns"""
    query = 'SELECT [UnitMeasureCode],[Name],[ModifiedDate],COUNT(*) FROM [AdventureWorks2012].[Production].[UnitMeasure] GROUP BY [UnitMeasureCode],[Name],[ModifiedDate] HAVING COUNT(*) > 1'
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        assert i[0] == 0


def test_column_counts():
    """Check on colunmn counts in table"""
    cursor.execute('SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_catalog = \'AdventureWorks2012\' AND '
                   'table_name = \'UnitMeasure\'')
    for i in cursor:
        assert i[0] == 3


