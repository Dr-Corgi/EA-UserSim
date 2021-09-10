from eventdet.dstc import *
from eventdet import BaseEventDetector

class DstcEventDetector(BaseEventDetector):

    def __init__(self, configs):

        super(DstcEventDetector, self).__init__()
        assert configs['dataset'] == 'dstc'

        self.configs = configs
        self.event_tool = None

        self.create_event_tool()

    def create_event_tool(self):
        if self.configs['event_detector'] == 'RuleEventDetector':
            self.event_tool = RuleEventTool(self.configs)
        else:
            raise NotImplementedError('Unknown Detector Type.')

    def detect(self, state, sys_action, goal):
        event = self.event_tool.detect(state, sys_action, goal)
        return event