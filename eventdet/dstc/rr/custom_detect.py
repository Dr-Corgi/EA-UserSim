from eventdet.dstc.rr import BaseRrDetectFunc

class CustomRrDetectFunc(BaseRrDetectFunc):

    def __init__(self, configs):
        super(CustomRrDetectFunc, self).__init__()
        self.func_name += '->' + 'CustomRrDetectFunc'

    def detect_rr(self, state, sys_action, goal):

        raise NotImplementedError('CustomRrDetectFunc is not implemented yet.')