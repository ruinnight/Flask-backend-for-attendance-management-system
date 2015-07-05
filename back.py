from flask import Flask, url_for
from flask import request
from flask import  jsonify
import MySQLdb as mdb
import datetime

    # http://127.0.0.1:5000/attendance?uid=001&authkey=qwerty&hour=h4&class=Class4&absentees=1,2,3,4

app = Flask(__name__)


@app.route('/')
def hello():
            success='{"Google ee appinde aishwaryam"}'
            list = []
            list.append(success)
            return success

@app.route('/login')
def login():
        return chek(request.args['name'],request.args['password'])

def chek(username,password):
        con = mdb.connect('mysql.server', 'arunpurushothama', 'qwertyuiop', 'arunpurushothama$api')
        try:
              token='{"authKey":"qwerty"}'
              token1='qwerty'
              error='{"failed"}'
              cur = con.cursor()
              cur.execute("select count(*) from staff where staffId=(%s) and password =(%s)",(username,password))
              row = cur.fetchone()
              if row[0] == 1:
                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token1,username))
                        con.commit()
                        con.close()
                        return token
              else:
                    con.close()
                    return error

        except mdb.Error, e:
              print "Error %d: %s" % (e.args[0],e.args[1])




@app.route('/attendance' )
def mark():
                    debug       = False
                    uid         = request.args['uid']
                    key         = request.args['authkey']
                    hourid      = request.args['hour']
                    classid     = request.args['class']
                    absentees   = request.args['absentees']
                    privilage   =""
                    privilage   = chek_privilages(uid,key,hourid,classid)
                    count=0
                    x=[]
                    if debug== True:
                                x.append(uid)
                                x.append(key)
                                x.append(hourid)
                                x.append(classid)
                                x.append(absentees)
                                x.append(privilage)
                                return jsonify(gamma=x)
                    priv = privilage
                    if priv == 'PG':
                                    con     = mdb.connect('mysql.server', 'arunpurushothama', 'qwertyuiop', 'arunpurushothama$api')
                                    cur     = con.cursor()
                                    try:
                                        cur.execute("INSERT INTO attendance VALUES ((%s),(%s),(%s),(%s))",(uid,classid,hourid,absentees))
                                        con.commit()
                                        con.close()
                                    except mdb.Error, e:

                                        con.close()
                                    x='{"authKey":"success"}'
                    elif priv == 'PR':
                                    x='{"authKey":"permissiondenied"}'

                    elif priv == 'IHC':
                                    x='{"authKey":"invalidhourocde"}'
                    return x


def chek_privilages(uId,key,hourId,classId):
        con     = mdb.connect('mysql.server', 'arunpurushothama', 'qwertyuiop', 'arunpurushothama$api')
        cur     = con.cursor()
        now     = datetime.datetime.now()
        day     = now.strftime("%A")
        status  = ""
        day="Monday"

        try:


              if day=='Monday':
                                if hourId=='h1':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h1=(%s)",(uId,classId))
                                elif hourId=='h2':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h2=(%s)",(uId,classId))
                                elif hourId=='h3':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h3=(%s)",(uId,classId))
                                elif hourId=='h4':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h4=(%s)",(uId,classId))
                                elif hourId=='h5':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h5=(%s)",(uId,classId))
                                elif hourId=='h6':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h6=(%s)",(uId,classId))
                                elif hourId=='h7':
                                        cur.execute("select count(*) from Monday where U_ID=(%s) and h7=(%s)",(uId,classId))
                                else:
                                     status='IHC'
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status='PG'
                                      con.close()
                                      return status

                                else:
                                      status='PR'
                                      con.close()
                                      return status

              elif day =='Tuesday':
                                if hourId=='h1':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h1=(%s)",(uId,classId))
                                elif hourId=='h2':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h2=(%s)",(uId,classId))
                                elif hourId=='h3':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h3=(%s)",(uId,classId))
                                elif hourId=='h4':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h4=(%s)",(uId,classId))
                                elif hourId=='h5':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h5=(%s)",(uId,classId))
                                elif hourId=='h6':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h6=(%s)",(uId,classId))
                                elif hourId=='h7':
                                        cur.execute("select count(*) from Tuesday where U_ID=(%s) and h7=(%s)",(uId,classId))
                                else:
                                     status='IHC'
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status='PG'
                                      con.close()
                                      return status

                                else:
                                      status='PR'
                                      con.close()
                                      return status


              elif day =='Wednesday':
                                if hourId=='h1':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h1=(%s)",(uId,classId))
                                elif hourId=='h2':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h2=(%s)",(uId,classId))
                                elif hourId=='h3':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h3=(%s)",(uId,classId))
                                elif hourId=='h4':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h4=(%s)",(uId,classId))
                                elif hourId=='h5':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h5=(%s)",(uId,classId))
                                elif hourId=='h6':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h6=(%s)",(uId,classId))
                                elif hourId=='h7':
                                        cur.execute("select count(*) from Wednesday where U_ID=(%s) and h7=(%s)",(uId,classId))
                                else:
                                     status='IHC'
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status='PG'
                                      con.close()
                                      return status

                                else:
                                      status='PR'
                                      con.close()
                                      return status

              elif day =='Thursday':
                                if hourId=='h1':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h1=(%s)",(uId,classId))
                                elif hourId=='h2':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h2=(%s)",(uId,classId))
                                elif hourId=='h3':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h3=(%s)",(uId,classId))
                                elif hourId=='h4':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h4=(%s)",(uId,classId))
                                elif hourId=='h5':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h5=(%s)",(uId,classId))
                                elif hourId=='h6':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h6=(%s)",(uId,classId))
                                elif hourId=='h7':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h7=(%s)",(uId,classId))
                                else:
                                     status='IHC'
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status='PG'
                                      con.close()
                                      return status

                                else:
                                      status='PR'
                                      con.close()
                                      return status


              elif day == 'Friday':
                                if hourId=='h1':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h1=(%s)",(uId,classId))
                                elif hourId=='h2':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h2=(%s)",(uId,classId))
                                elif hourId=='h3':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h3=(%s)",(uId,classId))
                                elif hourId=='h4':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h4=(%s)",(uId,classId))
                                elif hourId=='h5':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h5=(%s)",(uId,classId))
                                elif hourId=='h6':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h6=(%s)",(uId,classId))
                                elif hourId=='h7':
                                        cur.execute("select count(*) from Thursday where U_ID=(%s) and h7=(%s)",(uId,classId))
                                else:
                                     status='IHC'
                                     con.close()
                                     return status

                                row = cur.fetchone()
                                if row[0] == 1:
                                      status='PG'
                                      con.close()
                                      return status

                                else:
                                      status='PR'
                                      con.close()
                                      return status


        except mdb.Error, e:
              print "Error %d: %s" % (e.args[0],e.args[1])

@app.route('/logout')
def flush():
                        uid=request.args['uid']
                        key=request.args['authkey']
                        token= 'NULL'
                        con = mdb.connect('mysql.server', 'arunpurushothama', 'qwertyuiop', 'arunpurushothama$api')
                        status =[]
                        status.append(uid)
                        status.append(key)
                        status=""
                        try:
                              cur = con.cursor()
                              cur.execute("select count(*) from staff where staffId=(%s) and authkey =(%s)",(uid,key))
                              row = cur.fetchone()
                              if row[0] == 1:
                                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token,uid))
                                        con.commit()
                                        con.close()
                                        status='{"authKey":"success"}'

                              else:
                                    con.close()



                        except mdb.Error, e:
                                    status='{"authKey":"dberror"}'




                        return status
if __name__ == '__main__':
#        app.run(host='192.168.43.241',debug=True)
         app.run(debug=True)
