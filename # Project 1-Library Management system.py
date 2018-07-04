#Library Mangement System project by Shubham Singh
import time,string
from datetime import date,timedelta,datetime
def home():
    a='1'
    while int(a.isdigit()):
        print(" Library Mangement System ".center(120,'='))
        a=input('''Select a choice
1.Admin Login
2.Admin SignUp
3.Student Login
4.Student SignUp
Enter the '0' to Exit\n''')
        if a is '1':
            adminlog()
        elif a is '3':
            stdlog()
        elif a is '2':
            adminsign()
        elif a is '4':
            stdsign()
        elif a is '0':
            print("---Thank You for accessing the Page---".center(120))
            exit()
        else:
            print("---Enter the valid choice---".center(120))
            home()
        print("")
            
def adminsign():
    print(" Admin SignUp ".center(120,'*'))
    print('UserName : Must be a minimum of 5 characters  '.center(120))
    print('         : First character must be Letter Only'.center(120))
    print('Password : Must be a minimum of 6 characters\n'.center(120))
    b="%s,%s\n"%(input("Enter the New Admin Username\n"),input("Enter the New Admin Password\n"))
    if b.split(",")[0][0].isalpha() and len(b.split(",")[0])>=5 and len(b.split(",")[1])>=6 and 1^(b.split(",")[1]).isspace():
        data = open("Admin.txt").read().split("\n")
        c=0
        for j in range(len(data)-1):
            s= data[j].split(",")
            if b.split(",")[0] == s[0]:
                print("---Username Already Exist---".center(120))
                c=1
                break
        if c==0:
            open("Admin.txt","a").write(b)
            print("---You are Successfully Signed In---".center(120))
            if input("Do You Want to Login (Y/N) : ").lower()=="y":
                adminlog()
            else:
                home()
    else:
        print("---Invalid Credentials---".center(120))
    print("Press 1 to SignUn with Another Username")
    print("Press 2 to Log In with Exist Username")
    print("Press any other key to go back to Main Page")
    inp=input()
    if inp=='1':
        adminsign()
    if inp=='2':
        adminlog()
    else:
        home()
        
    
def adminlog():
    print(" Admin Login ".center(120,'*'))
    b="%s,%s\n"%(input("Enter the Admin Username\n"),input("Enter the Admin Password\n"))
    if b in open("Admin.txt").read():
        print("---You are Successfully Logged In---".center(120))
        print("")
        admin()
    else:
        print("---Invalid Admin Username and Password---".center(120))
        print("Press 1 to Log In Again")
        print("Press any other key to go back to Main Page")
        if input()=='1':
            adminlog()
        else:
            home()
    
def stdsign():
    print(" Student SignUp ".center(120,'*'))
    print('''Password : Must be a minimum of 6 character\n''')
    b="%s,%s,%s\n"%(input("Enter the Student Name\n"),input("Enter the 10 digit Student Rollnumber\n"),input("Create New Password\n"))
    if b.split(",")[0][0].isalpha() and b.split(",")[1].isdigit() and len(b.split(",")[1])==10 and len(b.split(",")[2])>=6 and 1^(b.split(",")[2]).isspace():
        c=0
        data = open("Student.txt").read().split("\n")
        for j in range(len(data)-1):
            s= data[j].split(",")
            if b.split(",")[1] == s[1]:
                print("---User Already Exist---".center(120))
                c=1
        if c==0:
            open("Student.txt","a").write(b)
            print("---You are Successfully Signed In---".center(120))
            if input("Do You Want to Login (Y/N) : ").lower()=="y":
                stdlog()
            else:
                home()
    else:
        print("---Invalid Credentials---".center(120))
    print("Press 1 to SignUn With Another Username.")
    print("Press 2 to Log In With Exist Username.")
    print("Press any other key to go back to Main Page.")
    inp=input()
    if inp=='1':
        stdsign()
    if inp=='2':
        stdlog()
    else:
        home()
        
def stdlog():
    print(" Student Login ".center(120,'*'))
    b="%s,%s"%(input("Enter the Student Rollnumber\n"),input("Enter the Student Password\n"))
    data = open("Student.txt").read().split("\n")
    c=0
    for j in range(len(data)-1):
        s= data[j].split(",")
        if b.split(",")[0] == s[1] and b.split(",")[1]==s[2]:
    #if b in open("Student.txt").read():
            print("---You are Successfully Logged In---".center(120))
            c=1
            stdpage(b)
    if c==0:
        #print("---Enter The Valid Student Username and Password---".center(120))
        print("---Invalid Student Username and Password---".center(120))
        print("Press 1 to Log In Again")
        print("Press any other key to go back to Main Page")
        if input()=='1':
            stdlog()
        else:
            home()

        
def admin():
    a='1'
    while int(a.isdigit()):
        print(" Admin Page ".center(120,'*'))
        a=input('''Select a Choice
1.Add Books in Library
2.List Of Books 
3.Update Book
4.Availability of Books
5.Students Detail
Enter the '0' to Logout\n''')
        if a is '1':
            addbook()
        elif a is '4':
            booksearch("admin","")
        elif a is '2':
            listbook("admin","")
        elif a is '3':
            bookupdate()
        elif a is '5':
            userdetail()
        elif a is '0':
            print("---Successfully Logged Out---".center(120))
            home()
        else:
            print("---Enter the valid choice---".center(120))
            admin()
        
def addbook():
    print(" Add Book ".center(120,"*"))
    b="%s,%s,%s,%s,0\n"%(input("ISBN No.  :  "),input("Auth. Name:  "),input("Book Name :  "),input("Quantity  :  "))
    if b.split(",")[0].isdigit() and b.split(",")[3].isdigit() and b.split(",")[3]>'0':
        data = open("Books.txt").read().split("\n")
        c=0
        for j in range(len(data)-1):
            s= data[j].split(",")
            if b.split(",")[0] == s[0]:
            #if b.split(",")[0] in open("Books.txt").read():
                print("Cannot Add: 'Books with ISBN No.",(b.split(",")[0]),"is already exist")
                c=1
        if c==0:
                open("Books.txt","a").write(b)
                print("---Book is Successfully Added---".center(120))
    else:
          print("---Enter Valid ISBN No. or Quantity---".center(120))
          
    c=(input('''
Press 1 to Add More Books in the Library.
Press any other key to go back to Admin Page.\n'''))
    if c is '1':
          addbook()
    else:
          print("---Back to Admin Page---".center(120))
          admin()
    
def booksearch(X,st):
    print(" Book Availability".center(120,"*"))
    print("\n")
    c=0
    t=0
    if X=="admin":
        m="No of Issued Book"
    if X=="std":
        m="Available"
    print("".center(80,"~").center(120))
    print("||{:<8}||{:<16}||{:<16}||{:<4}||{:<4}||".format("ISBN No",'Author Name','Book Name','Quantity',m).center(120))
    print("".center(80,"~").center(120))
    data = open("Books.txt").read().split("\n")
    for j in range(len(data)-1):
        d= data[j].split(",")
        if  int(d[3])-int(d[4])!=0:
            c=1
            if X=="admin":
                t=str(int(d[4]))
                print("{:<7}  {:<16}  {:<17}  {:<8}  {:<16}".format(d[0],d[1],d[2],d[3],t).center(120))
            if X=="std":
                t=str(int(d[3])-int(d[4]))
                print("{:<7}  {:<16}  {:<17}  {:<8}  {:<8}".format(d[0],d[1],d[2],d[3],t).center(120))
    print("".center(80,"~").center(120))
            
    if c==0:
        print("---Book not Found---".center(120))
    c=input('''
Press any key to go back to Previous Page.\n''')
    if c :
        if X=="admin":
            admin()
        if X=="std":
            stdpage(st)
        
def bookupdate():
    print("Book Update".center(120,"*"))
    b="%s"%(input("ISBN NO :   "))
    if b.isdigit():
     if b in open("Books.txt").read():
        e=input('''
1.Edit Quantity of book
2.Delete Book Detail from Library System 
Press any other key to go back to Admin Page\n''')
        data=open("Books.txt").read().split("\n")
        if e is '1':
                data = open("Books.txt").read().split("\n")
                for j in range(len(data)-1):
                    s= data[j].split(",")
                    if b==s[0]:
                      print("Old Quantity  ",(data[j].split(",")[-2]))
                      n=input("Enter new Quantity  ")
                      if n.isdigit():
                       if s[-1]<=n and n>'0':
                          q=s[0]+","+s[1]+","+s[2]+","+n+","+s[4]+"\n"
                          r=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+"\n"
                          s=open("Books.txt").read().replace(r,q)
                          open("Books.txt","w").write(s)
                          print("---Book is Successfully Updated--".center(120))
                       else:
                          print("---Cannot Edit: New Quantity is less than No. of Issued Book---".center(120))
                      else:
                          print("---Invalid New Quantity---".center(120))
                                
        elif e is '2':
            for j in range(len(data)-1):
                  s=data[j].split(",")
                  if b ==s[0]:
                      if s[-1]=='0':
                          r=s[0]+","+s[1]+","+s[2]+","+s[3]+","+s[4]+"\n"
                          s=open("Books.txt").read().replace(r,"")
                          open("Books.txt","w").write(s)
                          print("---Book is Successfully Deleted--".center(120))
                      else:
                          print("---Cannot Delete: Books are still issued---".center(120))
        else:
            print("---Back to Admin Page---".center(120))
            admin()
            
     else:
        print("No Book record found for ISBN No : ",b)
    else:
        print("---Invalid ISBN No.---".center(120))
    c=(input('''
Press 1 to More Updatation in the Library.
Press any other key to go back to Admin Page.\n'''))
    if c is '1':
              bookupdate()
    else:
              admin()
     
def listbook(X,st):
    if X=="admin":
        print(" List of Book ".center(120,"*"))
    print("".center(60,"~").center(120))
    print("||{:<8}||{:<16}||{:<16}||{:<4}||".format('ISBN No','Author Name','Book Name','Quantity').center(120))
    print("".center(60,"~").center(120))
    data=open("Books.txt").read().split("\n")
    c=0
    e=0
    for i in range(len(data)-1):
        d=data[i].split(",")
        c+=int(d[3])
        e+=1
        print("{:<7}  {:<16}  {:<16}  {:<4}".format(d[0],d[1][:14],d[2][:14],d[3]).center(120))
    print("".center(60,"~").center(120))
    print("Types of Book : %s \n No of  Books : %s"%(e,c))
    print("")
    if X=="admin":
        if input('Press any key to go back to Previous Page : '):
            admin()
    if X=="std":
        pass

def userdetail():
    print(" Students Detail ".center(120,"*"))
    print("".center(63,"~").center(120))
    print("||{:<11}||{:<13}||{:<30}||".format('RollNumber','Student Name','No of Book Isssued + ISBN No.').center(120))
    print("".center(63,"~").center(120))
    data=open("Student.txt").readlines()
    a=open("Issuedbook.txt").readlines()
    for j in data:
        c=0
        d=""
        k=j.split(",")
        for i in a:
            if k[1] in i:
                c+=1
                b=i.split(",")[0]
                d=d+","+b
        print("  {:<10}   {:<13}   {:<32}".format(k[1],k[0][:13],str(c)+"  ("+d[1:25]+")").center(120))
        i=25
        while(d[i:]):
            print("{:<33}{:<28}".format(" ","("+d[i:]+" )").center(120))
            i=i+25
    print("".center(63,"~").center(120))
    print("")
    if input('Press any key to go back to Admin Page : '):
        admin()
        
def stdpage(b):
    a='1'
    while int(a.isdigit()):
        print(" Student Page ".center(120,'*'))
        a=input('''Select a Choice
1.Available Books
2.Issue A Book
3.View Issued Book Detail
4.Return a Book
Enter 0 to Logout\n''')
        if a is '1':
            booksearch("std",b)
        elif a is '2':
            issuebook(b)
        elif a is '3':
            viewissue(b)
        elif a is '4':
            returnb(b)
        elif a is '0':
            print("---Successfully Logged Out---".center(120))
            home()
        else:
            print("---Enter the valid choice---".center(120))
            stdpage(b)

def issuebook(b):
    print("Issue Book(s)".center(120,"*"))
    listbook("std",b)
    c=input("\nEnter the ISBN No. :  ")
    data = open("Books.txt").read().split("\n")
    aval='0'
    d=0
    for j in range(len(data)-1):
        s= data[j].split(",")
        l=s
        if c==s[0]:
    #if c in open("Books.txt").read():
            if c+","+b.split(",")[0] in open("Issuedbook.txt").read():
                print("---Book is Already Issued---".center(120))
            else:
                print("".center(70,"~").center(120))
                print("||{:<8}||{:<16}||{:<16}||{:<4}||{:<4}||".format('ISBN No','Author Name','Book Name','Quantity','Available').center(120))
                print("".center(70,"~").center(120))
                aval=str(int(s[3])-int(s[4]))
                print("{:<10}{:<18}{:<18}{:<10}{:>6}".format(s[0],s[1][:16],s[2][:16],s[3],aval).center(120))
                print("".center(70,"~").center(120))          
                if aval=='0':
                  print("")
                  print("---Book is not available---".center(120))
                else:
                  t=date.today()
                  print("\nIssue date : ",t)
                  et=t+timedelta(30)
                  print("Return by date : ",et)
                  iss=c+","+b.split(",")[0]+","+str(t)+","+str(et)+"\n"
                  open("Issuedbook.txt","a").write(iss)
                  print("---Book is successfully Issued---".center(120))
                  q=l[0]+","+l[1]+","+l[2]+","+l[3]+","+str(int(l[4])+1)+"\n"
                  r=l[0]+","+l[1]+","+l[2]+","+l[3]+","+l[4]+"\n"
                  s=open("Books.txt").read().replace(r,q)
                  open("Books.txt","w").write(s)
            d=1
            
    if d==0:
        print("---No Book in library with this ISBN No---".center(120))
    q=input('''
Press 1 to Issue more Books from Library
Press any other key to go back to Previous Page\n''')
    if q is '1':
        issuebook(b)
    else:
        stdpage(b)
                  
def  viewissue(b):
      print("View Issued Book Detail".center(120,"*"))
      print("\nBook(s) issued by You ")
      print("".center(46,"~").center(120))
      print("||{:<10}||{:<13}||{:<14}||".format('ISBN No','Issued Date','Return by Date').center(120))
      print("".center(46,"~").center(120))
      data=open("Issuedbook.txt").read().split("\n")
      k=0
      for i in range(len(data)-1):
          d=data[i].split(",")
          if b.split(",")[0] ==d[1]:
                print(" {:<12} {:<15} {:<16}".format(d[0],d[2],d[3]).center(120))
                k+=1
      print("".center(46,"~").center(120))
      if k==0:
            print("---No Book is issued till now---".center(120))
      else:
            print("No. of books Issued : ",k)                       
      if input('Press any key to go back to Previous Page : '):
          stdpage(b)
          
def returnb(b):
    print("Returning a Book".center(120,"*"))
    data=open("Issuedbook.txt").read().split("\n")
    k=0
    l=0
    bn=input("Enter the ISBN No : ")
    for i in range(len(data)-1):
      d=data[i].split(",")
      if b.split(",")[0] ==d[1]:
        k=1
        if bn==d[0]:
            fine(d[-1])
            l=1
            if input("Do you Want to return book Y/N : ").lower()=='y':
                e=d[0]+","+d[1]+","+d[2]+","+d[3]+"\n"
                s=open("Issuedbook.txt").read().replace(e,"")
                open("Issuedbook.txt","w").write(s)
                dt=open("Books.txt").read().split("\n")
                for j in range(len(dt)-1):
                  t=dt[j].split(",")
                  if bn==t[0]:
                      e=t[0]+","+t[1]+","+t[2]+","+t[3]+","+t[4]+"\n"
                      f=t[0]+","+t[1]+","+t[2]+","+t[3]+","+str(int(t[4])-1)+"\n"
                      st=open("Books.txt").read().replace(e,f)
                      open("Books.txt","w").write(st)
                      print("---Book is Successfully returned---".center(120))
    if l==0:
        print("---This book is not issued---".center(120))
    if k==0:
        print("---No Book is issued till now---".center(120))
    q=input('''
Press 1 to Return Book.
Press any other key to go back to Previous Page\n''')
    if q is '1':
        returnb(b)
    else:
        stdpage(b)
        
def fine(dt):
    f="%Y-%m-%d"
    a=datetime.strptime(str(date.today()),f)-datetime.strptime(dt,f)
    fin=(a.days)*20
    if fin>0:
        print("\nFine per day : ",u"\u20B9","20")
        print("Total Fine : ",u"\u20B9",fin)
    else:
        print("\nNo Fine : Book is under Return by Date")                       
    print("")

if __name__=="__main__":
    home()

