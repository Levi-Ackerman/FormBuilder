import threading
import subprocess
import thread

__author__ = 'jsonlee'

class LogMonitor(threading.Thread):
    def __init__(self,deviceName):
        threading.Thread.__init__(self)
        self.command = "adb -s "+deviceName+" logcat"
        pass
    def run(self):
        popen = subprocess.Popen(self.command.split(" "),stdout=subprocess.PIPE,shell=False)
        while popen != None and popen.stdout is not None and popen.poll() is None:
            try:
                line = popen.stdout.readline()
                print(line)
            except Exception as e:
                print(e)