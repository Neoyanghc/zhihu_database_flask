import pymssql
import datetime



conn = pymssql.connect(host='127.0.0.1:1433', user='yhc', password='111111', database='ZhiHu', charset="UTF-8")
cur = conn.cursor()

def insertUser(cur,U_ID,user_name, mobile, Email,Passwd,SEX,SignDetail):
    sql_insert = '''
    INSERT INTO user_info
    VALUES (%s,%s,%s,%d,%s,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (U_ID, user_name,Passwd,mobile, Email,SEX, dt,SignDetail))

def insertQuestion(cur,Q_ID,user_ID, Q_text):
    sql_insert = '''
    INSERT INTO question_info
    VALUES (%s,%s,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (Q_ID, user_ID,Q_text, dt, 0))

def insertAnswer(cur,A_ID,Q_ID,user_ID,A_text):
    sql_insert = '''
    INSERT INTO Answer_info
    VALUES (%s,%s,%s,%s,%d);
    '''
    cur.execute(sql_insert, (A_ID,Q_ID,user_ID,A_text,0))
def insertComment(cur,C_ID,A_ID,user_ID, C_text):
    sql_insert = '''
    INSERT INTO Comment_info
    VALUES (%s,%s,%s,%s);
    '''
    cur.execute(sql_insert, (C_ID,A_ID,user_ID,C_text))
def insertCollection(cur,Q_ID,user_ID):
    sql_insert = '''
    INSERT INTO Collection_info
    VALUES (%s,%s);
    '''
    cur.execute(sql_insert, (Q_ID,user_ID))
def insertFocus(cur,Auser_ID,Buser_ID):
    sql_insert = '''
    INSERT INTO Focus_info
    VALUES (%s,%s);
    '''
    cur.execute(sql_insert, (Auser_ID,Buser_ID))
def insertAccount(cur,mobile,passwd):
    sql_insert = '''
    INSERT INTO Account_info
    VALUES (%d,%s);
    '''
    cur.execute(sql_insert, (mobile,passwd))
def selectAllUser(cur):
    SQL = 'select * from User_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectAllQuestion(cur):
    SQL = 'select * from Question_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectALLAnswer(cur):
    SQL = 'select * from Answer_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectALLComment(cur):
    SQL = 'select * from Comment_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectAnswerOfQuestion(cur,Q_ID):
    SQL = '''select A_text from Answer_info
             where Q_ID = (%s) '''
    cur.execute(SQL,(Q_ID))
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d

# insertAnswer(cur,'A008','Q005','u007','''看完了 @元吉
#  这篇乐理错漏百出，却假装专业客观的答案，不禁捧腹大笑，
#  这就是所谓的专业人士水准吗。本不想搭理，但是看到居然有这么多人将此捧为高赞，
#  也无奈只能站出来，秉着知乎精神反对一下了。
# ''')
# insertComment(cur,'c003','A002','u006','说的真好啊啊啊啊')
# insertCollection(cur,'Q001','u001')
# insertFocus(cur,'u003','u006')
# print('suecces')

def selectUserTologin(cur,telephone,passwd):
    sql = '''
    SELECT * FROM user_info
    WHERE email ='{}' and mobile = '{}'
    '''.format(passwd,telephone)
    cur.execute(sql)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return d

def questionAndfirstAuestion():
    questions = selectAllQuestion(cur)
    # print(questions)
    # print(answers)
    for i in range(len(questions)):
        data = selectAnswerOfQuestion(cur, questions[i][0])
        questions[i].append(data[0])
    return questions


print(selectUserTologin(cur,18801111888,'111111'))
cur.close()
conn.commit()
conn.close()