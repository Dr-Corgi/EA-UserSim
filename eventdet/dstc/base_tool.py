import abc

class BaseEventTool(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.func_name = '[BaseEventTool]'

    @abc.abstractmethod
    def create_od_det_func(self):
        return

    @abc.abstractmethod
    def create_iq_det_func(self):
        return

    @abc.abstractmethod
    def create_ir_det_func(self):
        return

    @abc.abstractmethod
    def create_rq_det_func(self):
        return

    @abc.abstractmethod
    def create_rr_det_func(self):
        return

    @abc.abstractmethod
    def detect(self, state, sys_action, goal):
        return