from eventdet.dstc.rr import BaseRrDetectFunc

class RuleRrDetectFunc(BaseRrDetectFunc):

    def __init__(self, configs):
        super(RuleRrDetectFunc, self).__init__()
        self.func_name += '->' + 'RuleRrDetectFunc'

    def detect_rr(self, state, sys_action, goal):

        event_count = 0

        if sys_action['diaact'] == 'request':
            if len(sys_action['inform_slots']) > 0:
                raise NotImplementedError('yield a request action but inform something.')

            for r_slot in sys_action['request_slots'].keys():
                if r_slot in state['rest_slots']:
                    event_count = 1

        if sys_action['diaact'] == 'inform':
            if 'taskcomplete' not in sys_action['inform_slots'].keys():
                for i_slot in sys_action['inform_slots'].keys():
                    if i_slot in sys_action['request_slots'].keys():
                        event_count = 1

                    if i_slot in goal['request_slots'].keys():
                        event_count = 1

        return event_count