import threading
import subprocess
from main import NotifListener

__author__ = 'jsonlee'

class Device(threading.Thread):

    def __init__(self,deviceName):
        threading.Thread.__init__(self)
        self.deviceName = deviceName
        self.command = "adb -s "+deviceName+" logcat"
        pass

    def setNotifListener(self,listener):
        self.listener = listener
        pass
    def getName(self):
        return self.deviceName

    def logout(self):
        pass

    def sendMsg(self):
        pass
    def run(self):
        popen = subprocess.Popen(self.command.split(" "),stdout=subprocess.PIPE,shell=False)
        while popen != None and popen.stdout is not None and popen.poll() is None:
            try:
                line = popen.stdout.readline()
                if "keyword" in line :
                    self.listener.onLogout()
                    pass
                elif "keywords" in line :
                    self.listener.onSended()
                    pass
                elif "keywordrecv" in line:
                    self.listener.onRecved();
                    pass
            except Exception as e:
                print(e)