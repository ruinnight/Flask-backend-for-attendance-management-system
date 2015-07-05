import MySQLdb as mdb
import datetime
def chek():
        con = mdb.connect('localhost', 'root', '', 'api')
        try:
              cur = con.cursor()
              cur.execute("select * from attendance")
              while True:
                    row = cur.fetchone()
                    if row == None:
                          break
                    else:
                        classId=row[1]
                        hourId =row[2]
                        print hourId,classId
                        if classId == 'Class1':
                                            if hourId == 'h1':

                                                args=row[3]
                                                sql='update Class1 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()

                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class1 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class1 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update Class1 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class1 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class1 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class1 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                        elif classId ==  'Class2':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update Class2 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class2 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class2 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update Class2 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class2 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class2 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class2 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                        elif classId ==  'Class3':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update Class3 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class3 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class3 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update Class3 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class3 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class3 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class3 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                        elif classId ==  'Class4':
                                            print "inside class4"
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update Class4 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class4 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)
                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class4 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                print "inside h4"
                                                args=row[3]
                                                sql='update Class4 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class4 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class4 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class4 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                        elif classId ==  'Class5':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update Class5 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class5 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class5 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update Class5 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class5 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class5 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class5 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                        elif classId ==  'Class6':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update Class6 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update Class6 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update Class6 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update Class6 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update Class6 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update Class6 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update Class6 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()

                        elif classId ==  'Class7':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update class1 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update class1 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update class1 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update class1 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update class1 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update class1 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update class1 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                        elif classId ==  'Class8':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update class8 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update class8 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update class8 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update class8 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update class8 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update class8 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update class8 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                        elif classId ==  'Class9':
                                            if hourId == 'h1':
                                                args=row[3]
                                                sql='update class9 SET h1=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h2':
                                                args=row[3]
                                                sql='update class9 SET h2=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h3':
                                                args=row[3]
                                                sql='update class9 SET h3=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h4':
                                                args=row[3]
                                                sql='update class9 SET h4=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h5':
                                                args=row[3]
                                                sql='update class9 SET h5=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h6':
                                                args=row[3]
                                                sql='update class9 SET h6=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                            if hourId == 'h7':
                                                args=row[3]
                                                sql='update class9 SET h7=0 where roll in (%s)'
                                                in_p=', '.join(map(lambda x: '%s', args))
                                                sql = sql % in_p
                                                cur.execute(sql, args)

                                                con.commit()
                                                con.close()
        except mdb.Error, e:
              x=x+1
def  findBunksters():
                x=0
                con = mdb.connect('localhost', 'root', '', 'api')
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class1 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur.execute("select studentId from Class2 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      cur = con.cursor()
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class3 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class4 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class5 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class6 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class7 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class8 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)
                      con.commit()
                except mdb.Error, e:
                      x=x+1
                try:
                      cur = con.cursor()
                      cur.execute("select studentId from Class9 where h1 = 0 or h2 =0 or h3 =0 or h4 =0 or h5 = 0 or h6=0 or h7 =0")
                      args=[]
                      while True:
                              row = cur.fetchone()
                              if row == None:
                                    break
                              else:
                                   args.append(row[0])

                      sql='update studentRecord SET attendance=attendance-1 where studentId in (%s)'
                      in_p=', '.join(map(lambda x: '%s', args))
                      sql = sql % in_p
                      cur.execute(sql, args)

                      con.commit()
                      con.close()
                except mdb.Error, e:
                      x=x+1

def reset():
    con = mdb.connect('localhost', 'root', '', 'api')
    try:
          cur = con.cursor()
          cur.execute("drop table class1")
          cur.execute("drop table class2")
          cur.execute("drop table class3")
          cur.execute("drop table class4")
          cur.execute("drop table class5")
          cur.execute("drop table class6")
          cur.execute("drop table class7")
          cur.execute("drop table class8")
          cur.execute("drop table class9")
          cur.execute("drop table attendance")

          cur.execute("CREATE TABLE `attendance` (`U_ID` varchar(11) NOT NULL,`class` varchar(11) DEFAULT NULL,`hour` varchar(11) DEFAULT NULL,`absentees` varchar(200) DEFAULT NULL,PRIMARY KEY (`U_ID`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")

          cur.execute("create table Class1(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class2(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class3(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class4(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class5(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class6(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class7(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class8(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("create table Class9(roll int,studentId varchar(20),h1 int,h2 int,h3 int,h4 int,h5 int,h6 int ,h7 int)")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '001/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '002/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '003/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '004/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '005/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '006/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '007/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '008/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '009/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class1` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '010/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '011/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '012/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '013/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '014/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '015/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '016/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '017/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '018/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '019/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class2` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '020/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '031/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '032/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '033/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '034/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '035/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '036/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '037/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '038/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '039/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class3` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '040/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '041/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '042/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '043/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '044/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '045/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '046/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '047/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '048/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '049/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class4` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '050/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '051/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '052/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '053/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '054/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '055/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '056/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '057/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '058/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '059/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class5` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '060/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '061/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '062/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '063/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '064/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '065/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '066/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '067/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '068/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '069/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class6` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '070/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '071/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '072/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '073/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '074/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '075/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '076/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '077/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '078/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '079/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class7` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '080/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '081/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '082/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '083/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '084/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '085/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '086/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '087/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '088/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '089/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class8` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '090/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('1', '091/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('2', '092/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('3', '093/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('4', '094/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('5', '095/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('6', '096/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('7', '097/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('8', '098/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('9', '099/12', '1', '1', '1', '1', '1', '1', '1')")
          cur.execute("INSERT INTO `api`.`Class9` (`roll`, `studentId`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`) VALUES ('10', '100/12', '1', '1', '1', '1', '1', '1', '1')")

          con.commit()
          con.close()
    except mdb.Error, e:
                      x=x+1

chek()
findBunksters()
#reset()
