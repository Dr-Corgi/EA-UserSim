import abc

class BaseRrDetectFunc(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseRrDetectFunc]'

    @abc.abstractmethod
    def detect_rr(self, state, sys_action, goal):
        return