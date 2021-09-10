import abc

class BaseIrDetectFunc(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseIrDetectFunc]'

    @abc.abstractmethod
    def detect_ir(self, state, sys_action, goal):
        return