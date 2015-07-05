from flask import Flask, url_for
from flask import request
from flask import  jsonify
import MySQLdb as mdb
import datetime

    # http://127.0.0.1:5000/attendance?uid=001&authkey=qwerty&hour=h4&class=Class4&absentees=1,2,3,4

app = Flask(__name__)


@app.route('/')
def hello():
            success="{'welcome':'Google ee appinde aishwaryam'}"
            list = []
            list.append(success)
            return success

@app.route('/login')
def login():
        return chek(request.args['name'],request.args['password'])

def chek(username,password):
        con = mdb.connect('localhost', 'root', '', 'api')
        try:
              token='{"status":"qwerty"}'
              error='error'
              cur = con.cursor()
              cur.execute("select count(*) from staff where staffId=(%s) and password =(%s)",(username,password))
              row = cur.fetchone()
              if row[0] == 1:
                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token,username))
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
                    priv=""
                    priv=''.join(privilage)
                    if priv == 'PG':
                                    con     = mdb.connect('localhost', 'root', '', 'api')
                                    cur     = con.cursor()
                                    try:
                                        cur.execute("INSERT INTO attendance VALUES ((%s),(%s),(%s),(%s))",(uid,classid,hourid,absentees))
                                        con.commit()
                                        con.close()
                                    except mdb.Error, e:

                                        con.close()
                                    x='{"status":"Success"}'
                    elif priv == 'PR':
                                    x='{"status":"Permission Denied"}'

                    elif priv == 'IHC':
                                    x='{"status":"Invalid Hour Code"}'
                    return x


def chek_privilages(uId,key,hourId,classId):
        con     = mdb.connect('localhost', 'root', '', 'api')
        cur     = con.cursor()
        now     = datetime.datetime.now()
        day     = now.strftime("%A")
        status  = []


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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status

                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
                                      con.close()
                                      return status


        except mdb.Error, e:
              print "Error %d: %s" % (e.args[0],e.args[1])

@app.route('/logout')
def flush():
                        uid=request.args['uid']
                        key=request.args['authkey']
                        token= 'NULL'
                        con = mdb.connect('localhost', 'root', '', 'api')
                        status =[]
                        status.append(uid)
                        status.append(key)
                        status=[]
                        try:
                              cur = con.cursor()
                              cur.execute("select count(*) from staff where staffId=(%s) and authkey =(%s)",(uid,key))
                              row = cur.fetchone()
                              if row[0] == 1:
                                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token,uid))
                                        con.commit()
                                        con.close()
                                        x='{"status":"Success"}'

                              else:
                                    con.close()



                        except mdb.Error, e:
                                    x='{"status":"Db Error"}'




                        return x
if __name__ == '__main__':
        app.run(debug=True)
from flask import Flask, url_for
from flask import request
from flask import  jsonify
import MySQLdb as mdb
import datetime

    # http://127.0.0.1:5000/attendance?uid=001&authkey=qwerty&hour=h4&class=Class4&absentees=1,2,3,4

app = Flask(__name__)


@app.route('/')
def hello():
            success="{'welcome':'Google ee appinde aishwaryam'}"
            list = []
            list.append(success)
            return jsonify(auth=list)

@app.route('/login')
def login():
        return chek(request.args['name'],request.args['password'])

def chek(username,password):
        con = mdb.connect('localhost', 'root', '', 'api')
        try:
              token="{'status':'qwerty'}"
              error='error'
              cur = con.cursor()
              cur.execute("select count(*) from staff where staffId=(%s) and password =(%s)",(username,password))
              row = cur.fetchone()
              if row[0] == 1:
                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token,username))
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
                    priv=""
                    priv=''.join(privilage)
                    if priv == 'PG':
                                    con     = mdb.connect('localhost', 'root', '', 'api')
                                    cur     = con.cursor()
                                    try:
                                        cur.execute("INSERT INTO attendance VALUES ((%s),(%s),(%s),(%s))",(uid,classid,hourid,absentees))
                                        con.commit()
                                        con.close()
                                    except mdb.Error, e:

                                        con.close()
                                    x="{'status':'Success'}"
                    elif priv == 'PR':
                                    x="{'status':'Permission Denied'}"

                    elif priv == 'IHC':
                                    x="{'status':'Invalid Hour Code'}"
                    return x


def chek_privilages(uId,key,hourId,classId):
        con     = mdb.connect('localhost', 'root', '', 'api')
        cur     = con.cursor()
        now     = datetime.datetime.now()
        day     = now.strftime("%A")
        status  = []


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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status
                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
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
                                     status.append('IHC')
                                     con.close()
                                     return status

                                row = cur.fetchone()
                                if row[0] == 1:
                                      status.append('PG')
                                      con.close()
                                      return status

                                else:
                                      status.append('PR')
                                      con.close()
                                      return status


        except mdb.Error, e:
              print "Error %d: %s" % (e.args[0],e.args[1])

@app.route('/logout')
def flush():
                        uid=request.args['uid']
                        key=request.args['authkey']
                        token= 'NULL'
                        con = mdb.connect('localhost', 'root', '', 'api')
                        status =[]
                        status.append(uid)
                        status.append(key)
                        status=[]
                        try:
                              cur = con.cursor()
                              cur.execute("select count(*) from staff where staffId=(%s) and authkey =(%s)",(uid,key))
                              row = cur.fetchone()
                              if row[0] == 1:
                                        cur.execute("UPDATE `staff` SET `authkey`=(%s) WHERE staffId=(%s)",(token,uid))
                                        con.commit()
                                        con.close()
                                        x="{'status':'Success'}"

                              else:
                                    con.close()



                        except mdb.Error, e:
                                    x="{'status':'Db error'}"




                        return x
if __name__ == '__main__':
        app.run('192.168.43.241',debug=True)
