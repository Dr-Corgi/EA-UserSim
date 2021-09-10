from eventdet.dstc.iq import BaseIqDetectFunc

class CustomIqDetectFunc(BaseIqDetectFunc):

    def __init__(self, configs):
        super(CustomIqDetectFunc, self).__init__()
        self.func_name += '->' + 'CustomIqDetectFunc'

    def detect_iq(self, state, sys_action, goal):

        raise NotImplementedError('CustomIqDetectFunc is not implemented yet.')