from eventdet.dstc.od import BaseOdDetectFunc

class CustomOdDetectFunc(BaseOdDetectFunc):

    def __init__(self, configs):
        super(CustomOdDetectFunc, self).__init__()
        self.func_name += '->' + 'CustomOdDetectFunc'

        self.turn_threshold = configs['turn_threshold']

    def detect_od(self, state, sys_action, goal):

        raise NotImplementedError('CustomOdDetectFunc is not implemented yet.')