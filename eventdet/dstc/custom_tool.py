from eventdet.dstc import BaseEventTool
from eventdet.dstc.iq import CustomIqDetectFunc
from eventdet.dstc.ir import CustomIrDetectFunc
from eventdet.dstc.od import CustomOdDetectFunc
from eventdet.dstc.rq import CustomRqDetectFunc
from eventdet.dstc.rr import CustomRrDetectFunc
from eventdet.event import Events

class CustomEventTool(BaseEventTool):

    def __init__(self, configs):
        super(CustomEventTool, self).__init__()
        self.func_name += '->' + '[CustomEventTool]'

        self.iq_det_func = None
        self.ir_det_func = None
        self.od_det_func = None
        self.rq_det_func = None
        self.rr_det_func = None

        self.configs = configs

        # initialize
        self.create_iq_det_func()
        self.create_ir_det_func()
        self.create_od_det_func()
        self.create_rq_det_func()
        self.create_rr_det_func()

    def create_iq_det_func(self):
        self.iq_det_func = CustomIqDetectFunc(self.configs)

    def create_ir_det_func(self):
        self.ir_det_func = CustomIrDetectFunc(self.configs)

    def create_od_det_func(self):
        self.od_det_func = CustomOdDetectFunc(self.configs)

    def create_rq_det_func(self):
        self.rq_det_func = CustomRqDetectFunc(self.configs)

    def create_rr_det_func(self):
        self.rr_det_func = CustomRrDetectFunc(self.configs)

    def detect(self, state, sys_action, goal):
        raise NotImplementedError('CustomEventTool is not implemented yet.')