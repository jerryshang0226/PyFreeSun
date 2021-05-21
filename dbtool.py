import pymysql
import logging
import globalvar


def dbOpen():
    logging.info("dbOpen, host = " + globalvar.db_host + "; user = " + globalvar.db_user + "; db = " + globalvar.db_name)
    db = pymysql.connect(host= globalvar.db_host, user=globalvar.db_user, password=globalvar.db_passwd, db=globalvar.db_name, charset=globalvar.db_charset)
    return db

def dbQueryFull(str_sql):
    db = dbOpen()
    cursor = db.cursor()
    cursor.execute(str_sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    logging.info("dbQueryFull："+ str_sql)
    return result

def dbQuery(str_sql,values):
    db = dbOpen()
    cursor = db.cursor()
    cursor.execute(str_sql,values)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    logging.info("dbQuery：" + str_sql)
    return result

def dbExec(str_sql,values):
    db = dbOpen()
    cursor = db.cursor()
    flg = 0
    logging.info("dbExec：" + str_sql + "; values = " + str(values))
    try:
        cursor.execute(str_sql,values)
        db.commit()
        flg = 1
    except:
        db.rollback()
        flg = 0
    finally:
        cursor.close()
        db.close()
        return flg

def dbCommit(str_sql):
    db = dbOpen()
    cursor = db.cursor()
    try:
        cursor.execute(str_sql)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()