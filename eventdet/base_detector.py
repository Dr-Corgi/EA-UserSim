import abc

class BaseEventDetector(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.event_tool = None

    @abc.abstractmethod
    def create_event_tool(self):
        return
