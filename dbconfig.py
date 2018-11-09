mssql = {
    'server':'db-host',
    'user' : 'username',
    'password' : 'password',
    'DB' : 'db-name'
}

def getConn():
    conn_string = 'mssql+pymssql://{}:{}@{}/{}'.format(
        mssql['user'], 
        mssql['password'], 
        mssql['server'],
        mssql['DB']
    )
    return conn_string
