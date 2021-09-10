from eventdet.dstc.ir import BaseIrDetectFunc

class CustomIrDetectFunc(BaseIrDetectFunc):

    def __init__(self, configs):
        super(CustomIrDetectFunc, self).__init__()
        self.func_name += '->' + 'CustomIrDetectFunc'

    def detect_ir(self, state, sys_action, goal):

        raise NotImplementedError('CustomIrDetectFunc is not implemented yet.')