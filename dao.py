import pymysql, logging, random, query


########## dao 기본 함수 ##########
def getConnect():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='dkssudzz10!',
                         db='BORTFOLIO_FLASK',
                         charset='utf8')
    return db

def getCursor(db):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return cursor

def getResult(db, cursor, sql, mthdName):
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return result
    except:
        logging.error("error: " + mthdName)
    finally:
        db.close()

def mnplData(db, cursor, sql, mthdName):
    try:
        cursor.execute(sql)
        db.commit()
        return "0000"
    except:
        logging.error("error: " + mthdName)
    finally:
        db.close()

##################################

def getWork():
    sql = query.getWork
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getWork()")

def getExperience():
    sql = query.getExperience
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getExperience()")

def getEducation():
    sql = query.getEducation
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getEducation()")


def getSkillLanguage():
    sql = query.getSkillLanguage
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getSkillLanguage()")

def getSkillFramework():
    sql = query.getSkillFramework
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getSkillFramework()")

def getCert():
    sql = query.getCert
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getCert()")

def getLotto():
    lotto = []
    for i in range(6):
        while True:
            ball = random.randint(1,45)
            if ball not in lotto:
                lotto.append(ball)
                break
    lotto.sort()

    while True:
        bonus = random.randint(1,46)
        if bonus not in lotto:
            break

    result = {"LOTTO":lotto, "BONUS":bonus}
    print(result)
    return result



########## ADMIN 테이블 조회 ##########
def getColumns(table):
    sql = query.getColumns.format(table=table)
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getColumns()")

def getTable(table):
    orders = {"work":"WORK_NO", "skill":"SKILL_NO", "education":"EDU_NO", "experience":"EXP_NO", "award":"AWARD_NO", "certification":"CERT_NO", "admin":"ADMIN_NO"}

    sql = query.getTable.format(table=table.upper(), order=orders[table])
    db = getConnect()
    cursor = getCursor(db)
    return getResult(db, cursor, sql, "getTable()")

def insertRecordToTable(table, values):
    sql = query.insertData.format(table=table.upper(), values=values)
    db = getConnect()
    cursor = getCursor(db)
    return mnplData(db, cursor, sql, "insertRecordToTable()")

def updateRecordInTable(table, pkColumn, pkValue, settings):

    try:
        for i in range(len(settings)):
            sql = query.updateData.format(table=table.upper(), pkColumn=pkColumn.upper(), pkValue=pkValue[i], setting=settings[i])
            print(sql)
            db = getConnect()
            cursor = getCursor(db)
            mnplData(db, cursor, sql, "updateRecordInTable()")

        return "0000"
    except:
        return "0001"

def deleteRecordFromTable(table, pkColumn, pkValue):
    sql = query.deleteData.format(table=table.upper(), pkColumn=pkColumn.upper(), pkValue=pkValue)
    db = getConnect()
    cursor = getCursor(db)
    return mnplData(db, cursor, sql, "deleteRecordFromTable()")
##################################