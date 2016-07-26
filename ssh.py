import paramiko
import tkinter

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
    result = []
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read())

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

if __name__ == '__main__':

    #cmd = 'ps -ef|grep src'
    cmd = 'cat /proc/loadavg'
    hostname = '10.30.51.230'
    username = 'root'
    password = '123456'
    Myssh(hostname,username,password)
    send_command(cmd)
    #Mytransport(hostname,username,password)
    download()
    quit_ssh()

    """
    ##窗口化
    top = tkinter.Tk()
    top.geometry('600x400')   #设置了主窗口的初始大小
    label = tkinter.Label(top, text='Myssh',font='Helvetica -12 bold')
    label.pack()
    top.mainloop()
    """