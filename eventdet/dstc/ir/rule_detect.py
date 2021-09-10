from eventdet.dstc.ir import BaseIrDetectFunc

class RuleIrDetectFunc(BaseIrDetectFunc):

    def __init__(self, configs):
        super(RuleIrDetectFunc, self).__init__()
        self.func_name += '->' + 'RuleIrDetectFunc'

    def detect_ir(self, state, sys_action, goal):

        event_count = 0

        if sys_action['diaact'] == 'request':
            for r_slot in sys_action['request_slots'].keys():
                if r_slot not in goal['request_slots'].keys() and r_slot not in goal['inform_slots'].keys():
                    event_count = 1
        if sys_action['diaact'] == 'inform':
            if 'taskcomplete' not in sys_action['inform_slots'].keys():
                for r_slot in sys_action['inform_slots'].keys():
                    if r_slot not in goal['request_slots'].keys() and r_slot not in goal['inform_slots'].keys():
                        event_count = 1

        return event_count