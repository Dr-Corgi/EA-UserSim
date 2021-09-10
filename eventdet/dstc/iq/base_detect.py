import abc

class BaseIqDetectFunc(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseIqDetectFunc]'

    @abc.abstractmethod
    def detect_iq(self, state, sys_action, goal):
        return