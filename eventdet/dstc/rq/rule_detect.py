from eventdet.dstc.rq import BaseRqDetectFunc

class RuleRqDetectFunc(BaseRqDetectFunc):

    def __init__(self, configs):
        super(RuleRqDetectFunc, self).__init__()
        self.func_name += '->' + 'RuleRqDetectFunc'

    def detect_rq(self, state, sys_action, goal):

        event_count = 0

        if sys_action['diaact'] == 'request':
            for r_slot in sys_action['request_slots'].keys():
                if r_slot in state['history_slots'].keys() or r_slot in state['inform_slots'].keys():
                    event_count = 1

        return event_count