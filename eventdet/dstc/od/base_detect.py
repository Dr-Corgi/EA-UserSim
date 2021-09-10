import abc

class BaseOdDetectFunc(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseOdDetectFunc]'

    @abc.abstractmethod
    def detect_od(self, state, sys_action, goal):
        return