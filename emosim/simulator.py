from emosim.emocalc import *
from emosim import Emotion

class EmoSimulator(object):

    def __init__(self, emo_configs, profile):

        if emo_configs['emo_calculator'] == 'LinearEmoCalculator':
            self.emo_calculator = LinearEmoCalculator(emo_configs)
        else:
            raise NotImplementedError('Unknown Calculator Type.')

        self.emo = Emotion(profile['mood'], profile['personality'])

    def get_personality(self):
        return self.emo.personality

    def get_mood(self):
        return self.emo.mood

    def set_profile(self, profile):
        self.emo = Emotion(profile['mood'], profile['personality'])

    def set_mood(self, new_mood):
        self.emo.mood = new_mood

    def set_personality(self, new_personality):
        self.emo.personality = new_personality

    def update_mood(self, events):
        self.set_mood(self.emo_calculator.update_mood(self.emo, events))