import pymysql


def db_insert_task(text, urgent):

    # prepare the query text
    sql = """INSERT INTO task(description, urgent) VALUES (%s, %s)"""

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, urgent))
        # commit all pending queries
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result


def get_sorted_tasks_list():

    sql = "SELECT * FROM task order by description ASC"  # here we order data using "order by"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")

    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    conn.close()
    tasks = []
    for row in results:
        tasks.append({"id": row[0], "description": row[1], "urgent": row[2]})
    return tasks


def db_contains(task):

    # prepare the query text
    sql = "select description from task where description = %s"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    results = cursor.fetchall()
    conn.close()

    if len(results) == 0:
        return False
    else:
        return True


def db_remove_task(task_id):

    # prepare the query text
    sql = "delete from task where id_task = %s"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (task_id,))
        # commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result


def db_remove_multiple_tasks(text):

    # prepare the query text
    sql = "delete from task where description LIKE %s"

    # add percent sign (%) wildcard to select all the strings that contain specified text
    # <<the multiple character percent sign (%) wildcard can be used to represent
    # any number of characters in a value match>>
    text = "%" + text + "%"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()

    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (text, ))
        # commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result


def get_task(task_id):
    sql = "SELECT * FROM task WHERE id_task=%s"
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")

    cursor = conn.cursor()
    cursor.execute(sql, (task_id,))

    results = cursor.fetchone()
    conn.close()

    if len(results) == 0:
        return {}
    else:
        return {"id": results[0], "description": results[1], "urgent": results[2]}


def update_task(task_id, description, urgent):

    # prepare the query text
    sql = "UPDATE task SET description=%s, urgent=%s WHERE id_task=%s"

    # connect to the db
    conn = pymysql.connect(user="root", password="root", host="localhost", database="todolist")
    cursor = conn.cursor()
    result = False
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (description,urgent, task_id))
        # commit all pending executed queries in the connection
        conn.commit()
        result = True
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result
