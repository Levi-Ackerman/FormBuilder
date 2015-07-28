__author__ = 'jsonlee'
from abc import abstractmethod
class NotifListner(object):
    @abstractmethod
    def onLogout(self,deviceName):
        pass