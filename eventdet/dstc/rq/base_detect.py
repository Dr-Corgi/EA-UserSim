import abc

class BaseRqDetectFunc(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseRqDetectFunc]'

    @abc.abstractmethod
    def detect_rq(self, state, sys_action, goal):
        return