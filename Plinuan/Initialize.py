import random
import tkinter
import time
import os

def gettime(): #获取时间函数
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      MainForm.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

def db():
      if RegUNI.get() == 'root':
            if RegUPI.get() == '123456':
                  print("验证通过,正在重启系统")

                  i = 0
                  while i <= 100:
                        print("初始化中...["+str(i)+"%]")
                        i += 1

                  ii = 0
                  while ii <= 100:
                        print("加载组件中...["+str(ii)+"%]")
                        ii += 1

                  lj = os.getcwd()
                  os.system("python system.py")
            elif RegUPI.get() != '123456':
                  print("验证失败")
      elif RegUNI.get() != 'root':
            print("验证失败")
      else:
            print("验证失败")
MainForm = tkinter.Tk() #实例化tk模块
var=tkinter.StringVar() #创建一个tk模块stringVar组件

GetTime = tkinter.Label(MainForm,textvariable=var,fg='#fff',bg='blue',font=("黑体",16)) #显示
GetTime.grid(column=1,columnspan=2,ipadx=20,row=0)
gettime()

Signal = random.randint(0,100)
GetSignal = tkinter.Label(MainForm,text="信号:"+str(Signal),fg='#fff',bg='blue',font=("楷体",16))
GetSignal.grid(column=10,columnspan=2,ipadx=20,row=0)

InitializeInfo = tkinter.Message(MainForm,text="完成一些设置(或者初始化系统)以启动系统",fg='#fff',bg='blue',font=("楷体",16))
InitializeInfo.grid(column=10,columnspan=1,ipadx=30,row=2)

RegUN = tkinter.Label(MainForm,text="用户名:",fg='#fff',bg='blue',font=("楷体",16))
RegUN.grid(column=9,columnspan=1,ipadx=40,row=3)

RegUNI = tkinter.Entry(MainForm,font=("楷体",16))
RegUNI.grid(column=10,columnspan=1,ipadx=40,row=3)

RegUP = tkinter.Label(MainForm,text="密码:",fg='#fff',bg='blue',font=("楷体",16))
RegUP.grid(column=9,columnspan=1,ipadx=40,row=4)

RegUPI = tkinter.Entry(MainForm,font=("楷体",16))
RegUPI.grid(column=10,columnspan=1,ipadx=40,row=4)

N = tkinter.Label(MainForm,text="\n\n\n",fg='#fff',bg='blue',font=("楷体",16))
N.grid(column=9,columnspan=1,ipadx=40,row=5)

Initialize = tkinter.Button(MainForm,text="initialize",font=("黑体",12),command=db)
Initialize["bd"] = "2px"
Initialize["activebackground"] = "#2d3aff"
Initialize["activeforeground"] = "#fff"
Initialize.grid(column=125,columnspan=1,ipadx=30,row=8)
#btn1 = Button(MainForm, text='方法一')
#btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

MainForm.config(background = "blue")
MainForm.overrideredirect(True)
MainForm.mainloop()
