import datetime
import MySQLdb as mdb
from flask import  jsonify


def test(uid,key,hourid,classid,absentees):
                    debug       = True
                    # uid         = request.args['uid']
                    # key         = request.args['authkey']
                    # hourid      = request.args['hour']
                    # classid     = request.args['class']
                    # absentees   = request.args['absentees']
                    privilage   = chek_privilages(uid,key,hourid,classid)
                    x=[]
                    if debug== True:
                                print uid
                                print key
                                print hourid
                                print classid
                                print absentees
                                print privilage

                    priv = ''.join(privilage)
                    if priv == 'PG':
                                    print "inside pg"
                                    con     = mdb.connect('localhost', 'root', '', 'api')
                                    cur     = con.cursor()
                                    cur.execute("INSERT INTO attendance VALUES ((%s),(%s),(%s),(%s))",(uid,classid,hourid,absentees))
                                    con.commit()
                                    con.close()
                                    print "Success"
                    elif priv == 'PR':
                                    print "PermissionDenied"

                    elif priv == 'IHC':
                                    print "InvalidHourCode"


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


uid='001'
key ='qwerty'
hour = 'h4'
classid='Class4'
absentess='1#2#3#4'


test(uid,key,hour,classid,absentess)
