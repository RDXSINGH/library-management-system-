from tkinter import *
from tkinter import Tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

import datetime 

class LibrarySystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSYTEM")
        self.root.geometry("1550x800+0+0")


        self.member_var=StringVar()
        
        self.prn_var=StringVar()

        self.id_var=StringVar()

        self.firstname_var=StringVar()

        self.lastname_var=StringVar()

        self.address1_var=StringVar()

        self.address2_var=StringVar()

        self.postcode_var=StringVar()

        self.mobile_var=StringVar()

        self.bookid_var=StringVar()

        self.booktitle_var=StringVar()

        self.author_var=StringVar()

        self.dateborrowed_var=StringVar()

        self.datedue_var=StringVar()

        self.daysonbook=StringVar()

        self.lateratefine_var=StringVar()

        self.dateoverdue=StringVar()

        self.finallprice=StringVar()
        



        #lbltitle for title bar
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSYTEM",bg="powder Blue",fg="red",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X ) #fill se X axis mai proper fill hojayega
        
        #forframe
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1540,height=350)



        #for adding two frame inside 2nd frame for member info
        #dfl=dataframeleft
        #=================================dataframeleft==============================================================
        dfl=LabelFrame(frame,text="_Member Information_",bg="powder blue",fg="red",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dfl.place(x=0,y=5,width=890,height=300)

        lblmember=Label(dfl,bg="powder blue",text="MemberType",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)#grid mai row col dena hoga hain label ke ander hain islye grid use kr rahe hain

        #combobox is inside ttkmodule
        commem=ttk.Combobox(dfl,font=("times new roman",15,"bold"),width=27,textvariable=self.member_var,state="readonly")#state=readonly karne se value change nhi kr skate hain bus read kr sakte hain
        commem["value"]=("Admin Staff","Student","lecturer")
        commem.current(0)
        commem.grid(row=0,column=1)

        lblprn_no=Label(dfl,bg="powder blue",text="PRN no:",padx=2,font=("arial",12,"bold"))
        lblprn_no.grid(row=1,column=0,sticky=W)
        txtprn_no=Entry(dfl,font=("arial",13,"bold"),textvariable=self.prn_var,width=32)
        txtprn_no.grid(row=1,column=1)

        lbltitle=Label(dfl,bg="powder blue",text="ID No",padx=2,font=("arial",12,"bold"))
        lbltitle.grid(row=2,column=0,sticky=W)
        txttitle=Entry(dfl,font=("arial",13,"bold"),textvariable=self.id_var,width=32)
        txttitle.grid(row=2,column=1)

        lblfirstname=Label(dfl,bg="powder blue",text="First Name",padx=2,font=("arial",12,"bold"))
        lblfirstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(dfl,font=("arial",13,"bold"),textvariable=self.firstname_var,width=32)
        txtfirstname.grid(row=3,column=1)

        lbllastname=Label(dfl,bg="powder blue",text="Last Name",padx=2,font=("arial",12,"bold"))
        lbllastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(dfl,font=("arial",13,"bold"),textvariable=self.lastname_var,width=32)
        txtlastname.grid(row=4,column=1)

        lbladd1=Label(dfl,bg="powder blue",text="Address1",padx=2,font=("arial",12,"bold"))
        lbladd1.grid(row=5,column=0,sticky=W)
        txtadd1=Entry(dfl,font=("arial",13,"bold"),textvariable=self.address1_var,width=32)
        txtadd1.grid(row=5,column=1)

        
        lbladd2=Label(dfl,bg="powder blue",text="Address2",padx=2,font=("arial",12,"bold"))
        lbladd2.grid(row=6,column=0,sticky=W)
        txtadd2=Entry(dfl,font=("arial",13,"bold"),textvariable=self.address2_var,width=32)
        txtadd2.grid(row=6,column=1)


        lblpostalcode=Label(dfl,bg="powder blue",text="Postalcode",padx=2,font=("arial",12,"bold"))
        lblpostalcode.grid(row=7,column=0,sticky=W)
        txtpostalcode=Entry(dfl,font=("arial",13,"bold"),textvariable=self.postcode_var,width=32)
        txtpostalcode.grid(row=7,column=1)

        
        
        lblmobile=Label(dfl,bg="powder blue",text="Mobile",padx=2,font=("arial",12,"bold"))
        lblmobile.grid(row=8,column=0,sticky=W)
        txtmobile=Entry(dfl,font=("arial",13,"bold"),textvariable=self.mobile_var,width=32)
        txtmobile.grid(row=8,column=1)

        lblBookId=Label(dfl,bg="powder blue",text="Book Id",padx=2,font=("arial",12,"bold"))
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(dfl,font=("arial",13,"bold"),textvariable=self.bookid_var,width=32)
        txtBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(dfl,bg="powder blue",text="Book Title",padx=2,font=("arial",12,"bold"))
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(dfl,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=32)
        txtBookTitle.grid(row=1,column=3)

        lblAuthorname=Label(dfl,bg="powder blue",text="Authorname",padx=2,font=("arial",12,"bold"))
        lblAuthorname.grid(row=2,column=2,sticky=W)
        txtAuthorname=Entry(dfl,font=("arial",13,"bold"),textvariable=self.author_var,width=32)
        txtAuthorname.grid(row=2,column=3)


        lblDateBorrowed=Label(dfl,bg="powder blue",text="DateBorrowed",padx=2,font=("arial",12,"bold"))
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(dfl,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=32)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(dfl,bg="powder blue",text="DateDue",padx=2,font=("arial",12,"bold"))
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(dfl,font=("arial",13,"bold"),textvariable=self.dateoverdue,width=32)
        txtDateDue.grid(row=4,column=3)

        lblDaysonBook=Label(dfl,bg="powder blue",text="Days on Book",padx=2,font=("arial",12,"bold"))
        lblDaysonBook.grid(row=5,column=2,sticky=W)
        txtDaysonBook=Entry(dfl,font=("arial",13,"bold"),textvariable=self.daysonbook,width=32)
        txtDaysonBook.grid(row=5,column=3)


        lblLateReturn=Label(dfl,bg="powder blue",text="Late Return Fine",padx=2,font=("arial",12,"bold"))
        lblLateReturn.grid(row=6,column=2,sticky=W)
        txtLateReturn=Entry(dfl,font=("arial",13,"bold"),textvariable=self.lateratefine_var,width=32)
        txtLateReturn.grid(row=6,column=3)

    

        lblDateover=Label(dfl,bg="powder blue",text="Date over Due",padx=2,font=("arial",12,"bold"))
        lblDateover.grid(row=7,column=2,sticky=W)
        txtDateover=Entry(dfl,font=("arial",13,"bold"),textvariable=self.datedue_var,width=32)
        txtDateover.grid(row=7,column=3)

        lblActualPrice=Label(dfl,bg="powder blue",text="Actual Price ",padx=2,font=("arial",12,"bold"))
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(dfl,font=("arial",13,"bold"),textvariable=self.finallprice,width=32)
        txtActualPrice.grid(row=8,column=3)


 
        #=============================DataFrame Right=======================================================
        #dfr=dataframeright
        
        dfr=LabelFrame(frame,text="_book information_",bg="powder blue",fg="red",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dfr.place(x=900,y=5,width=560,height=300)

        self.txtbox=Text(dfr,font=("times new roman",12,"bold"),width=30,height=16,padx=3,pady=7)
        self.txtbox.grid(row=0,column=2)


        listScroll=Scrollbar(dfr)
        listScroll.grid(row=0,column=1,sticky="ns")

        listbooks=["python for everybody","python cook book","ML","SATA","DATAsCIENCE","MEGA","PHYSICS","CHEM","math"]




        listBox=Listbox(dfr,font=("times new roman",12,"bold"),width=32,height=16)
        listBox.grid(row=0,column=0,padx=4,pady=0)
        listScroll.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END,item)





        #=================================Button frame=================================================
        #fbutton means function button

        fbutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        fbutton.place(x=0,y=480,width=1541,height=70)


        BtnaddData=Button(fbutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=23,bg="Red",fg="white",)
        BtnaddData.grid(row=0,column=0)

        BtnaddData=Button(fbutton,text="Show Data",font=("arial",12,"bold"),width=23,bg="Red",fg="white")
        BtnaddData.grid(row=0,column=1)

        BtnaddData=Button(fbutton,text="Update",font=("arial",12,"bold"),width=23,bg="Red",fg="white")
        BtnaddData.grid(row=0,column=2)

        BtnaddData=Button(fbutton,text="Delete",font=("arial",12,"bold"),width=23,bg="Red",fg="white")
        BtnaddData.grid(row=0,column=3)

        BtnaddData=Button(fbutton,text="Reset",font=("arial",12,"bold"),width=23,bg="Red",fg="white")
        BtnaddData.grid(row=0,column=4)

        BtnaddData=Button(fbutton,text="Exit",font=("arial",12,"bold"),width=23,bg="Red",fg="white")
        BtnaddData.grid(row=0,column=5)
        
        
        #=================================database information frame=================================================

        fdetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        fdetails.place(x=0,y=550,width=1540,height=250)

        Table_frame=Frame(fdetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1480,height=220)

        #scrollbar
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.libtable=ttk.Treeview(Table_frame,column=("membertype","PRNno","IDNo","FirstName","LastName","Address1","Address2",
                                                        "Postalcode","Mobile","BookId","BookTitle","Authorname","DateBorrowed",
                                                        "DateDue","DaysonBook","LateReturnFine","DateoverDue","ActualPrice",),xscrollcommand=xscroll.set,yscrollcommand=xscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.libtable.xview)
        yscroll.config(command=self.libtable.yview) #config karne se scroll bar move hoga 


        self.libtable.heading("membertype", text="Member Type")
        self.libtable.heading("PRNno", text="PRN NO")
        self.libtable.heading("IDNo", text="ID NO")
        self.libtable.heading("FirstName", text="First Name")
        self.libtable.heading("LastName", text="Last Name ")
        self.libtable.heading("Address1", text="Address1")
        self.libtable.heading("Address2", text="Address2")
        self.libtable.heading("Postalcode", text="Postal Code")
        self.libtable.heading("Mobile", text="Mobile")
        self.libtable.heading("BookId", text="Book Id")
        self.libtable.heading("BookTitle", text="Book Title")
        self.libtable.heading("Authorname", text="Author Name ")
        self.libtable.heading("DateBorrowed", text="Date Borrowed")
        self.libtable.heading("DateDue", text="Date Due Type")
        self.libtable.heading("DaysonBook", text="Days on Book ")
        self.libtable.heading("LateReturnFine", text="Late Return Fine")
        self.libtable.heading("DateoverDue", text="Date over Due ")
        self.libtable.heading("ActualPrice", text="Actual Price ")

        self.libtable["show"]="headings"
        self.libtable.pack(fill=BOTH,expand=1)

        #database table mai column name ka width set 100 karne ke liye
        self.libtable.column("membertype",width=100)
        self.libtable.column("PRNno",width=100)
        self.libtable.column("IDNo",width=100)
        self.libtable.column("FirstName",width=100)
        self.libtable.column("LastName",width=100)
        self.libtable.column("Address1",width=100)
        self.libtable.column("Address2",width=100)
        self.libtable.column("Postalcode",width=100)
        self.libtable.column("Mobile",width=100)
        self.libtable.column("BookId",width=100)
        self.libtable.column("BookTitle",width=100)
        self.libtable.column("Authorname",width=100)
        self.libtable.column("DateBorrowed",width=100)
        self.libtable.column("DateDue",width=100)
        self.libtable.column("DaysonBook",width=100)
        self.libtable.column("LateReturnFine",width=100)
        self.libtable.column("DateoverDue",width=100)
        self.libtable.column("ActualPrice",width=100)

        

        #mysql se connection
        #uske baad cursor ke help se sabhi datako database mai add karenge
    def add_data(self):
        conn=mysql.connector.connect(host='localhost',username="root",password="kishan1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var().get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finallprice.get()
                                                                                                                ))
        conn.commit()
        conn.close()

        messagebox.showinfo("success","member has been inserted successfully")
        

if __name__=="__main__":
    root=Tk() 
    obj=LibrarySystem(root)
    root.mainloop() #isse window open hoga or close v hoga BUT MAINLOOP nhi use kiya toh window bus pop hoga
