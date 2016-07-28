# -*- coding: utf8 -*-
import paramiko
#import tkinter
from tkinter import  *

##建立ssh连接
def Myssh(hostname,username,password):
    global ssh
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,username=username,password=password)
    except Exception as e:
        print(e)

##发送命令
def send_command(cmd):
    #for m in cmd:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    #print("command is ",cmd)
    result = []
    for line in stdout.readlines():
        result.append(line)
    return result

##上传文件
def upload():
    sftp = ssh.open_sftp()
    remotepath = '/data/test.txt'
    localpath = 'testLosspasswd.txt'
    sftp.put(localpath,remotepath)

##下载文件
def download():
    sftp = ssh.open_sftp()
    remotepath = '/data/test.txt'
    localpath = 'test.txt'
    sftp.get(remotepath,localpath)

#退出ssh连接
def quit_ssh():
    ssh.close()

def MyUI():
    ##窗口化
    top = Tk()
    top.title("Myssh")
    top.geometry('800x400')  # 设置了主窗口的初始大小\

    label = Label(top, text='Myssh', font='Helvetica -12 bold').pack()

    frm = Frame(top)
    Label(frm, text='input you command:', font='Helvetica -10 bold').grid(row=0)
    Label(frm, text='ssh result:', font='Helvetica -10 bold').grid(row=1)
    var1 = StringVar()
    e1 = Entry(frm, textvariable=var1)
    e2 = Text(frm)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    def read_command():
        cmd = (var1.get())
        result = send_command(cmd)
        for i in result:
            e2.insert(1.0,i)
    Button(frm, text='commit', command=read_command).grid(row=0, column=3)
    frm.pack()

    top.mainloop()


if __name__ == '__main__':
    #cmd = 'ps -ef|grep src'
    hostname = '10.30.51.230'
    username = 'root'
    password = '123456'
    Myssh(hostname,username,password)
    MyUI()
    #send_command(cmd)
    #Mytransport(hostname,username,password)
    #download()
    quit_ssh()


