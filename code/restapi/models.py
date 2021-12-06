import pymysql

def get_user(connection, id):
    with connection.cursor() as cursor:
            sql = "SELECT username FROM users WHERE id = " + str(id)
            cursor.execute(sql)
            result = cursor.fetchone()
            #print(result)
    connection.autocommit(True)
    return result['username']

def update_user(connection, id, username):
    with connection.cursor() as cursor:
            sql = "UPDATE users SET username = '" + username + "' WHERE id = " + str(id)
            cursor.execute(sql)
            connection.commit()
    if connection.commit():
        return 1
    return 0

def add_user(connection, username):
    sql = "INSERT INTO users (username) VALUES ('" + username + "')"
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
    except pymysql.err.IntegrityError:
        return "failed - user " + username + " already exist"

    cursor.execute('SELECT LAST_INSERT_ID() AS id')
    id = cursor.fetchone()['id']
    return "user - " + username + " added , id = " + str(id)

def add_token(connection, apitoken):
    sql = "INSERT INTO tokens (token, expired) values('" + apitoken + "',date_add(now(),interval 90 day))"
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
    except pymysql.err.IntegrityError:
        return "error"

    cursor.execute('SELECT LAST_INSERT_ID() AS id')
    id = cursor.fetchone()['id']
    return "added , token id - " + str(id)
