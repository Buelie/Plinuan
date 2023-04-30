import random
import tkinter
import time

MainTK = tkinter.Tk()
var=tkinter.StringVar()

def gettime(): #获取时间函数
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      MainTK.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

def style_w():
      MainTK.config(background = "#fff")
      InitializeInfo.config(fg='#000',bg='#fff')
      GetSignal.config(fg='#000',bg='#fff')
      GetTime.config(fg='#000',bg='#fff')
      Initialize.config(text="切换到深色模式",bg="#fff",fg="#000",command=style_b)

def style_b():
      MainTK.config(background = "#202020")
      InitializeInfo.config(fg='#fff',bg='#202020')
      GetSignal.config(fg='#fff',bg='#202020')
      GetTime.config(fg='#fff',bg='#202020')
      Initialize.config(text="切换到浅色模式",bg="#202020",fg="#fff",command=style_w)

GetTime = tkinter.Label(MainTK,textvariable=var,fg='#000',bg='#fff',font=("黑体",8)) #显示
GetTime.grid(column=1,columnspan=1,ipadx=1,row=1)
gettime()

Signal = random.randint(0,100)
GetSignal = tkinter.Label(MainTK,text="信号:"+str(Signal),fg='#000',bg='#fff',font=("楷体",8))
GetSignal.grid(column=10,columnspan=2,ipadx=20,row=1)

InitializeInfo = tkinter.Message(MainTK,text="\n\n\n\n\n\n\n\n\n\n\n",fg='#000',bg='#fff',font=("楷体",16))
InitializeInfo.grid(column=10,columnspan=100,ipadx=30,row=3)

Initialize = tkinter.Button(MainTK,text="切换到深色模式",font=("黑体",10),command=style_b)
Initialize["bd"] = "2px"
Initialize["activebackground"] = "#2d3aff"
Initialize["activeforeground"] = "#fff"
Initialize.grid(column=125,columnspan=1,ipadx=30,row=8)

MainTK.config(background = "#fff")
MainTK.overrideredirect(True)
MainTK.mainloop()
