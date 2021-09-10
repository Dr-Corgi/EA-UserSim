from eventdet.dstc.rq import BaseRqDetectFunc

class CustomRqDetectFunc(BaseRqDetectFunc):

    def __init__(self, configs):
        super(CustomRqDetectFunc, self).__init__()
        self.func_name += '->' + 'CustomRqDetectFunc'

    def detect_rq(self, state, sys_action, goal):

        raise NotImplementedError('CustomRqDetectFunc is not implemented yet.')