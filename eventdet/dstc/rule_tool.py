from eventdet.dstc import BaseEventTool
from eventdet.dstc.iq import RuleIqDetectFunc
from eventdet.dstc.ir import RuleIrDetectFunc
from eventdet.dstc.od import RuleOdDetectFunc
from eventdet.dstc.rq import RuleRqDetectFunc
from eventdet.dstc.rr import RuleRrDetectFunc
from eventdet.event import Events

class RuleEventTool(BaseEventTool):

    def __init__(self, configs):
        super(RuleEventTool, self).__init__()
        self.func_name += '->' + '[RuleEventTool]'

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
        self.iq_det_func = RuleIqDetectFunc(self.configs)

    def create_ir_det_func(self):
        self.ir_det_func = RuleIrDetectFunc(self.configs)

    def create_od_det_func(self):
        self.od_det_func = RuleOdDetectFunc(self.configs)

    def create_rq_det_func(self):
        self.rq_det_func = RuleRqDetectFunc(self.configs)

    def create_rr_det_func(self):
        self.rr_det_func = RuleRrDetectFunc(self.configs)

    def detect(self, state, sys_action, goal):
        counts = [0, 0, 0, 0, 0]    # od, ir, rq, rr, iq

        counts[0] = self.od_det_func.detect_od(state, sys_action, goal)
        counts[3] = self.rr_det_func.detect_rr(state, sys_action, goal)
        if counts[3] == 0:
            counts[1] = self.ir_det_func.detect_ir(state, sys_action, goal)
        counts[2] = self.rq_det_func.detect_rq(state, sys_action, goal)
        counts[4] = self.iq_det_func.detect_iq(state, sys_action, goal)

        event = Events(counts)

        return event
