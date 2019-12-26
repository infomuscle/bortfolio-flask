from flask          import Flask, render_template, request, jsonify, redirect, url_for
from flask_mail     import Mail, Message
import dao, logging, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/resume')
def resume():
    experience  = dao.getExperience()
    education   = dao.getEducation()
    language    = dao.getSkillLanguage()
    framework   = dao.getSkillFramework()
    database    = dao.getSkillDatabase()
    certification  = dao.getCert()
    award       = dao.getAward()
    return render_template('resume.html', experience = experience, education = education, language = language, framework = framework, database = database, certification = certification, award = award)

@app.route('/works')
def works():
    works = dao.getWork()
    return render_template("works.html", works=works)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/lotto')
def lotto():
    result = dao.getLotto()
    return render_template('lotto.html', result=result)

@app.route('/login')
def login():
    return render_template('login.html')


# Admin -----------------------------------------------
@app.route('/admin/loginValidation', methods=['POST'])
def loginValidation():
    data = request.get_json()

    adminId = data['adminId']
    adminPw = data['adminPw']

    # 아이디 체크
    adminIdObjList = dao.getAdminIdList()

    adminIdList = []

    for idObj in adminIdObjList:
        adminIdList.append(idObj['ADMIN_ID'])

    if adminId not in adminIdList:
        print("Wrong ID Error")
        return "E0001"

    # 패스워드 체크
    adminPwObjList = dao.getAdminPw(adminId)
    adminPwHashed = adminPwObjList[0]['ADMIN_PW']

    if adminPw == adminPwHashed:
        return "0000"
    else:
        print("Wrong Password Error")
        return "E0002"

@app.route('/admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/tables/<table>')
def tables(table):
    columns = dao.getColumns(table.upper())
    rows = dao.getTable(table)
    return render_template('admin/tables.html', table=table, columns=columns, rows=rows)

@app.route('/admin/addData', methods=['POST'])
def addData():
    data = request.get_json()

    table = data['table']
    columns = data['columns'].split(",")

    # INSERT VALUES 값 생성
    values = "("
    for i in range(len(columns)):
        temp = "input" + str(i+1)

        # 자료형 판별하는 함수 만들까 -> 알아서 해주긴 함
        d = data[temp]
        values += "'" + d + "'"
        if i != len(columns) - 1:
            values += ", "
    values += ")"
    print(values)

    dao.insertRecordToTable(table, values)

    return "0000"

@app.route('/admin/update', methods=['POST'])
def updateData():
    data = request.get_json()
    table = data['table']
    pkColumn = data['pkColumn']
    pkValue = data['pkValue']
    cols = data['columns']

    settings = []

    for c in cols:
        temp = ""
        for k in c.keys():
            if c[k] == 'None':
                c[k] = 'NULL'
                temp += (k + "=" + c[k])
            else:
                temp += (k + "='" + c[k] + "'")
            temp += ","
        setting = temp[:-1]
        settings.append(setting)

    resCd = dao.updateRecordInTable(table, pkColumn, pkValue, settings)

    return resCd

@app.route('/admin/delete', methods=['POST'])
def deleteData():
    data = request.get_json()
    table = data['table']
    pkColumn = data['pkColumn']
    pkValue = data['pkValue']

    dao.deleteRecordFromTable(table, pkColumn, pkValue)

    return "0000"
# ----------------------------------------------------


# Mail -----------------------------------------------
app.config.update(
    DEBUG = True,
    # Email Settings
    MAIL_SERVER = 'smtp.gmail.com'
  , MAIL_PORT = 465
  , MAIL_USE_SSL = True
  , MAIL_USERNAME = 'infomuscle10'
  , MAIL_PASSWORD = 'dkssudzz10!'
)

mail = Mail(app)

@app.route('/sendMail', methods=['POST'])
def sendMail():
    # TODO AJAX랑 데이터 파라미터 통일
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    title = "Mail from BxF - " + email

    msgBody = "name: " + name + "\n\n" + "email: " + email + "\n\n" + "phone: " + phone + "\n\n\n" + message

    try:
        msg = Message(title,
                      sender = email,
                      recipients=["infomuscle10@gmail.com"])
        msg.body = msgBody
        mail.send(msg)
        return 'success'
    except Exception as e:
        return (str(e))
# ----------------------------------------------------


if __name__ == '__main__':
    app.run()


# 테이블명 = WORK
# 컬럼: WORK_NO(INT) | TITLE(VARCHAR 20, PK) | SUB_TITLE(VARCHAR 20) | CTG(VARCHAR 20) | DESC(VARCHAR 500) | CLIENT(VARCHAR 20) | STRT_DT(DATE) | END_DT(DATE) | REP_IMG(VARCHAR 100) | URL (VARCHAR 100) | USE_YN(VARCHAR 1)
#
# 테이블명 = SKILL
# 1) 컬럼: TITLE(VARCHAR, PK) | SKILL1 | SKILL2 | SKILL3 | SKILL4 | SKILL5 | SKILL6 | SKILL7 |
# 2) 컬럼: SKILL_NO | SKILL_NAME | LEVEL | USE_PERIOD | LOGO_IMG
#
# 테이블명 = EXPERIENCE
# 컬럼: EXP_NO(INT) | COMPANY(VARCHAR 20, PK) | JOB(VARCHAR 20) | DESCRIPTION(VARCHAR 500) | STRT_DT(DATE) | END_DT(DATE) | USE_YN(VARCHAR 1)
#
# 테이블명 = AWARD_CERT
# 컬럼: AC_NO(INT) | AC_NM(VARCHAR 50, PK) | AC_TYPE(VARCHAR 20) | DESCRIPTION(VARCHAR 200) | ISSUE_DT(DATE) | USE_YN(VARCHAR 1)