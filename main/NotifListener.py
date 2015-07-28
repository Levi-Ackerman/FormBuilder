__author__ = 'jsonlee'
from abc import abstractmethod
class NotifListner(object):
    @abstractmethod
    def onLogout(self,deviceName):
        pass
    @abstractmethod
    def onSended(self):
        pass
    @abstractmethod
    def onRecved(self):
        pass
    @abstractmethod
    def onTimeout(self):
        pass