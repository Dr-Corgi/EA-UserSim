from eventdet.dstc.iq import BaseIqDetectFunc

class RuleIqDetectFunc(BaseIqDetectFunc):

    def __init__(self, configs):
        super(RuleIqDetectFunc, self).__init__()
        self.func_name += '->' + 'RuleIqDetectFunc'

    def detect_iq(self, state, sys_action, goal):

        event_count = 0

        if sys_action['diaact'] == 'inform':
            if 'taskcomplete' not in sys_action['inform_slots'].keys():
                for i_slot in sys_action['inform_slots'].keys():
                    if i_slot in goal['request_slots'].keys() and i_slot in state['rest_slots']:
                        event_count = 1

        if sys_action['diaact'] == 'request':
            for i_slot in sys_action['request_slots'].keys():
                if i_slot in goal['inform_slots'].keys() and i_slot in state['rest_slots']:
                    event_count = 1

        return event_count