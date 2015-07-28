import main

__author__ = 'jsonlee'
from main.Device import Device
from main.NotifListener import NotifListner
from abc import abstractmethod
class Task(NotifListner):
    def __init__(self):
        self.deviceSend = Device('88e3ab7bf0cb')
        self.deviceRecv = Device('')
        self.deviceRecv.setNotifListener(self)
        self.deviceSend.setNotifListener(self)
        self.deviceRecv.start()
        self.deviceSend.start()

    def onLogout(self,deviceName):
        if deviceName == self.deviceRecv.getName():
            self.deviceSend.sendMsg()

    def onSended(self):

        pass
    def onRecved(self):
        self.deviceSend.sendMsg()
        pass
    def onTimeout(self):
        self.deviceSend.sendMsg()
        pass
    def doTest(self):
        self.deviceRecv.logout()
        pass