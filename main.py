from os import write
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import*
dsAccount=[]
currentAccount=None
pheptinh=""
def openSignup(win):
    win.destroy()
    Signup()
def openTopUpScreen(win):
    win.destroy()
    topUpScreen()
def openLogin(win):
    win.destroy()
    login()
def openMainScreen(win):
    win.destroy()
    mainScreen()
def openCalculator(win):
    win.destroy()
    cal()
def openWithdraw(win):
    win.destroy()
    withdrawScreen()
#===========================================================================================================
def nhanso(num,mhnhap):
    global pheptinh
    pheptinh=pheptinh+num
    mhnhap.configure(text=pheptinh)

def Del(mhnhap):
    global pheptinh
    pheptinh=""
    mhnhap.configure(text=pheptinh)
    
def Bang(mhnhap):
    global pheptinh

    pheptinh=str(eval(pheptinh))
    mhnhap.configure(text=pheptinh)    

def thongtin():
    messagebox.showinfo("About us","tôi là Thành Phát ")

def phienban():
    messagebox.showinfo("Version","Day la phien ban 1.0")
def cal():
    win=Tk()
    win.title("Calculator")
    mainMenu=Menu(win)
    optionMenu=Menu(mainMenu,tearoff=0)
    win.configure(menu=mainMenu)
    mainMenu.add_cascade(label="Edit",menu=optionMenu)
    optionMenu.add_command(label="Back",command=lambda:openMainScreen(win))
    mhnhap=Label(win)
    mhnhap.grid(columnspan=4,row=0,column=1)
    #================================================================
    btn7=Button(win,text="7",width="5",command=lambda:nhanso("7",mhnhap))
    btn7.grid(row=1,column=1)
    btn8=Button(win,text="8",width="5",command=lambda:nhanso("8",mhnhap))
    btn8.grid(row=1,column=2)
    btn9=Button(win,text="9",width="5",command=lambda:nhanso("9",mhnhap))
    btn9.grid(row=1,column=3)
    btncong=Button(win,text="+",width="5",command=lambda:nhanso("+",mhnhap))
    btncong.grid(row=1,column=4)
    #=================================================================
    btn4=Button(win,text="4",width="5",command=lambda:nhanso("4",mhnhap))
    btn4.grid(row=2,column=1)
    btn5=Button(win,text="5",width="5",command=lambda:nhanso("5",mhnhap))
    btn5.grid(row=2,column=2)
    btn6=Button(win,text="6",width="5",command=lambda:nhanso("6",mhnhap))
    btn6.grid(row=2,column=3)
    btntru=Button(win,text="-",width="5",command=lambda:nhanso("-",mhnhap))
    btntru.grid(row=2,column=4)
    #==================================================================
    btn1=Button(win,text="1",width="5",command=lambda:nhanso("1",mhnhap))
    btn1.grid(row=3,column=1)
    btn2=Button(win,text="2",width="5",command=lambda:nhanso("2",mhnhap))
    btn2.grid(row=3,column=2)
    btn3=Button(win,text="3",width="5",command=lambda:nhanso("3",mhnhap))
    btn3.grid(row=3,column=3)
    btnnhan=Button(win,text="*",width="5",command=lambda:nhanso("*",mhnhap))
    btnnhan.grid(row=3,column=4)
    #==================================================================
    btn0=Button(win,text="0",width="5",command=lambda:nhanso("0",mhnhap))
    btn0.grid(row=4,column=1)
    btnchia=Button(win,text="/",width="5",command=lambda:nhanso("/",mhnhap))
    btnchia.grid(row=4,column=2)
    btnbang=Button(win,text="=",width="5",command=lambda:Bang(mhnhap))
    btnbang.grid(row=4,column=3)
    btndel=Button(win,text="AC",width="5",command=lambda:Del(mhnhap))
    btndel.grid(row=4,column=4)
    mainloop()
#======================================================================================================
def dangky(entryUsername,entryPassword,rdSelect,cmbNationality,chkstate):
    username=entryUsername.get()
    password=entryPassword.get()
    gender=rdSelect.get()
    nationality=cmbNationality.get()
    s="Username: "+ username+"\n"
    s+="Password: "+ password+"\n"
    s+="Gender: "+gender+"\n"
    s+="Nationality: "+nationality
    
    kq=messagebox.askyesno("Bạn có muốn đăng ký???",s)
    s=username+","+password+","+gender+","+nationality+","+str(chkstate.get())+",0"
    if(kq==True):
        file=open("account.txt","a")
        file.write(s+"\n")
        file.close()
        
    print(kq)

def Signup():
    win=Tk()
    win.title("Sign up")
    win.geometry("600x140")
        
    lbUsername=Label(win,text="Username")
    lbPassword=Label(win,text="Password")
    lbUsername.place(x=10,y=0)
    lbPassword.place(x=10,y=30)

    entryUsername=Entry(win)
    entryPassword=Entry(win,show="*")
    entryUsername.place(x=70,y=0)
    entryPassword.place(x=70,y=30)


    lbGender=Label(win,text="Gender")
    lbNationality=Label(win,text="Nationality")
    lbGender.place(x=10,y=60)
    lbNationality.place(x=300,y=0)

    lbCal=Label(win,text="Calculator")
    lbCal.place(x=300,y=60)

    chkstate=BooleanVar()
    chkCal=Checkbutton(win,text="Do you want to use calculator?",var=chkstate)
    chkCal.place(x=360,y=60)

    rdSelect=StringVar()
    rdSelect.set("Male")
    rdMale=Radiobutton(win,text="Male",value="Male",var=rdSelect)
    rdFemale=Radiobutton(win,text="Female",value="Female",var=rdSelect)

    rdMale.place(x=70,y=60)
    rdFemale.place(x=150,y=60)

    dsNationality=["Vietnamese","Korean","Japanese","China","American"]
    cmbNationality=Combobox(win,values=dsNationality,state="readonly")
    cmbNationality.current(0)
    cmbNationality.place(x=300,y=30)
        
    BtnSignup=Button(win,text="SignUp",width=10,command=lambda:dangky(entryUsername,entryPassword,rdSelect,cmbNationality,chkstate))
    BtnSignup.place(x=260,y=100)
    BtnBack=Button(win,text="Back",width=10,command=lambda:openLogin(win))
    BtnBack.place(x=180,y=100)
    mainloop()
#=========================================================================
def thoatchuongtrinh():
    quit()

def testFile(Username,Password):
    global currentAccount
    ok=False
    file=open("account.txt","r")
    data=file.readlines()
    dsAccount.clear()
    for vitri in range(0,len(data)):
        line=data[vitri]
        line=line.replace("\n","")
        line=line.split(",")
        line[5]=int(line[5])
        dsAccount.append(line)
        if(line[0]==Username and line[1]==Password):
            currentAccount=dsAccount[-1]
            ok = True
    file.close()
    return ok
def Clickloginbutton(entryUsername,entryPassword,lbMilo,win):
    username=entryUsername.get()
    password=entryPassword.get()
    if (testFile(username,password)==True):
        openMainScreen(win)
    else:
        lbMilo.configure(text="Bạn đăng nhập sai quá sai.")

def thongtin():
    messagebox.showinfo("About us","Đây là chương trình hỗ trợ ngân hàng\nNgười tạo ra Thành Phát.K")

def phienban():
    messagebox.showinfo("Version","Đây là phiên bản 1.0")

def login():
    win = Tk()
    win.title("Login")
    win.geometry("300x300")

    mainMenu=Menu(win)
    optionMenu=Menu(mainMenu,tearoff=0)
    optionMenu.add_command(label="Signup",command=lambda:openSignup(win))
    optionMenu.add_command(label="Quit",command=thoatchuongtrinh)
    helpMenu=Menu(mainMenu,tearoff=0)
    helpMenu.add_command(label="About us",command=thongtin)
    helpMenu.add_command(label="Version",command=phienban)

    win.configure(menu=mainMenu)
    mainMenu.add_cascade(label="Option",menu=optionMenu)
    mainMenu.add_cascade(label="Help",menu=helpMenu)
    

    lbLoginPrompt = Label(win,text="Login prompt",foreground="Blue")
    lbLoginPrompt.pack()

    lbUsername = Label(win,text="Username",foreground="black")
    lbUsername.pack()

    entryUsername = Entry(win)
    entryUsername.pack()

    lbPassword = Label(win,text="Password",foreground="black")
    lbPassword.pack()

    entryPassword = Entry(win,show="*")
    entryPassword.pack()


    lbMilo= Label(win,text="")
    lbMilo.pack()
    buttonLogin=Button(win,text="Login",width=10,command=lambda:Clickloginbutton(entryUsername,entryPassword,lbMilo,win))
    
    buttonLogin.pack()
    

    mainloop()
#======================================================================================================
def CheckMoney():
    global currentAccount
    messagebox.showinfo("Kiểm tiền","Tiền của bạn là: "+str(currentAccount[5]))

def mainScreen():
    win=Tk()
    labelHello=Label(win,text="Xin Chào Qúy Khách "+currentAccount[0])
    labelHello.pack()
    btnCheck=Button(win,text="Check Money",width=20,command=lambda:CheckMoney())
    btnCheck.pack()
    btnWithdraw=Button(win,text="Withdraw Money",width=20,command=lambda:openWithdraw(win))
    btnWithdraw.pack()
    btnTopup=Button(win,text="Top-up Money",width=20,command=lambda:openTopUpScreen(win))
    btnTopup.pack()
    if currentAccount[4]=="True":
        btnCal=Button(win,text="Calculator",width=20,command=lambda:openCalculator(win))
        btnCal.pack()
    btnLogout=Button(win,text="Logout",width=20,command=lambda:openLogin(win))
    btnLogout.pack() 
    mainloop()
#========================================================================================================
def ghiFile():
    file=open("account.txt","w")
    for account in dsAccount:
        file.write(account[0]+","+account[1]+","+account[2]+","+account[3]+","+account[4]+","+str(account[5])+"\n")
    file.close()
def naptien(entry20,entry50,entry100,entry200,entry500):
    to20=int(entry20.get())
    to50=int(entry50.get())
    to100=int(entry100.get())
    to200=int(entry200.get())
    to500=int(entry500.get())
    tong=(to20*20000)+(to50*50000)+(to100*100000)+(to200*200000)+(to500*500000)
    messagebox.showinfo("Nạp tiền","Bạn đã nạp: "+str(tong))
    currentAccount[5]+=tong
    ghiFile()
def topUpScreen():
    win=Tk()
    win.title("Số nạp")
    labelnap=Label(win,text="Topup")
    labelnap.grid(row=1,column=1,columnspan=2)

    labelgia=Label(win,text="Value")
    labelgia.grid(row=2,column=1)

    labelluong=Label(win,text="Amount")
    labelluong.grid(row=2,column=2)

    label20=Label(win,text="20.000")
    label20.grid(row=3,column=1)

    label50=Label(win,text="50.000")
    label50.grid(row=4,column=1)

    label100=Label(win,text="100.000")
    label100.grid(row=5,column=1)

    label200=Label(win,text="200.000")
    label200.grid(row=6,column=1)

    label500=Label(win,text="500.000")
    label500.grid(row=7,column=1)

    entry20=Entry(win,width=15)
    entry20.grid(row=3,column=2)

    entry50=Entry(win,width=15)
    entry50.grid(row=4,column=2)

    entry100=Entry(win,width=15)
    entry100.grid(row=5,column=2)

    entry200=Entry(win,width=15)
    entry200.grid(row=6,column=2)

    entry500=Entry(win,width=15)
    entry500.grid(row=7,column=2)

    buttonBack=Button(win,text="Back",command=lambda:openMainScreen(win))
    buttonBack.grid(row=8,column=1)

    buttonTopup=Button(win,text="Top-up",command=lambda:naptien(entry20,entry50,entry100,entry200,entry500))
    buttonTopup.grid(row=8,column=2)
    mainloop()
#=====================================================================================================================
def withdraw(entry):
    money=int(entry.get())
    if (money<=currentAccount[5]):
        currentAccount[5]-=money
        ghiFile()
        messagebox.showinfo("Số tiền đã rút","Tiền của bạn đã rút:"+str(money)) 
    else:
        messagebox.showinfo("Thông Báo","Giao dịch không thể thực hiện")
def withdrawScreen():
    win=Tk()
    win.title("Rút tiền")
    label=Label(win,text="How much do you want to withdraw?")
    label.grid(row=1,column=1,columnspan=2)
    entry=Entry(win,width=30)
    entry.grid(row=2,column=1,columnspan=2)
    buttonBack=Button(win,text="Back",command=lambda:openMainScreen(win))
    buttonBack.grid(row=3,column=1)
    buttonWithdraw=Button(win,text="Withdraw",command=lambda:withdraw(entry))
    buttonWithdraw.grid(row=3,column=2)
    mainloop()
#====================================================================================================================================
login()