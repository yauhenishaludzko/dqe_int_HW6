import pymssql

conn = pymssql.connect(
        server='EPBYVITW0125\SQLEXPRESS',
        user='test_user',
        password="123456",
        database='AdventureWorks2012',
        )


def connect_db():
    conn_db = pymssql.connect(
        server='EPBYVITW0125\SQLEXPRESS',
        user='test_user',
        password="123456",
        database='AdventureWorks2012',
        )
    return conn_db.cursor()


def connection_table_rows(table_name: str):
    cursor = connect_db()
    cursor.execute(f'select * from {table_name}')
    rows = []
    for row in cursor:
        rows.append(row)
    return rows


def table_columns(table_name: str):
    columns = ''
    columns_list = []
    cursor = connect_db()
    cursor.execute(f'select column_name FROM INFORMATION_SCHEMA.COLUMNS where table_name =\'{table_name}\'')
    for row in cursor:
        columns_list.append(row[0])
    return ', '.join(columns_list)
