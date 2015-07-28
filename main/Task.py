__author__ = 'jsonlee'
import NotifListener;
import Device
class Task(NotifListener):
    def __init__(self):
        self.deviceSend = Device('88e3ab7bf0cb')
        self.deviceRecv = Device('')
        self.deviceRecv.setNotifListener(self)
        self.deviceSend.setNotifListener(self)
        self.deviceRecv.start()
        self.deviceSend.start()
        self.reset()
        self.doTest()

    def onLogout(self,deviceName):
        if self.status == 1:
            if deviceName == self.deviceRecv.getName():
                self.status = 2
                self.deviceSend.sendMsg()

    def onSended(self):
        pass

    def onRecved(self):
        pass
    def doTest(self):
        if self.status == 0:
            self.status = 1
            self.deviceRecv.logout()

    def reset(self):
        self.status = 0