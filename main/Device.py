import threading
import subprocess

__author__ = 'jsonlee'

class Device(threading.Thread):
    def __init__(self,deviceName):
        threading.Thread.__init__(self)
        self.sendMsgStr = "adb shell am start -a android.intent.action.VIEW -n cn.ninegame.gamemanager/cn.ninegame.gamemanager.activity.MainActivity -e request sendMsg"
        self.logoutStr = "adb shell am start -a android.intent.action.VIEW -n cn.ninegame.gamemanager/cn.ninegame.gamemanager.activity.MainActivity -e request logout"
        self.deviceName = deviceName
        self.listenLog = "adb -s "+deviceName+" logcat"
        pass

    def setNotifListener(self,listener):
        self.listener = listener
        pass
    def getName(self):
        return self.deviceName

    def logout(self):
        self.timeout_command(self.logoutStr,2)
        pass

    def sendMsg(self,targetId):
        self.timer = threading.Timer(10,self.timeout)
        self.start()
        self.timeout_command(self.sendMsgStr,2)
        pass

    def timout(self):
        self.listener.onTimeout()
        pass
    def timeout_command(self,command, timeout):
        """call shell-command and either return its output or kill it
        if it doesn't normally exit within timeout seconds and return None"""
        import subprocess, datetime, time
        start = datetime.datetime.now()
        process = subprocess.Popen(command.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=False)
        while process.poll() is None:
            time.sleep(0.1)
            now = datetime.datetime.now()
            if (now - start).seconds> timeout:
                process.terminate()
        return process.stdout.read()

    def run(self):
        popen = subprocess.Popen(self.listenLog.split(" "),stdout=subprocess.PIPE,shell=False)
        while popen != None and popen.stdout is not None and popen.poll() is None:
            try:
                line = popen.stdout.readline()
                if "login success" in line :
                    self.listener.onLogout()
                    pass
                elif "send msg" in line :
                    self.listener.onSended()
                    pass
                elif "recv msg" in line:
                    self.listener.onRecved();
                    if self.timer.isAlive():
                        self.timer.cancel()
                    pass
            except Exception as e:
                print(e)