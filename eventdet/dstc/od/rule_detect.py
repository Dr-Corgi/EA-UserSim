from eventdet.dstc.od import BaseOdDetectFunc

class RuleOdDetectFunc(BaseOdDetectFunc):

    def __init__(self, configs):
        super(RuleOdDetectFunc, self).__init__()
        self.func_name += '->' + 'RuleOdDetectFunc'

        self.turn_threshold = configs['turn_threshold']

    def detect_od(self, state, sys_action, goal):

        event_count = 0

        turn = state['turn']
        if turn > self.turn_threshold:
            event_count = 1

        return event_count