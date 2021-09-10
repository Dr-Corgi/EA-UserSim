import json
import codecs

class ProfileReader(object):

    def __init__(self, profile_path='./profiles.json'):
        self.profile_path = profile_path

        self.profiles = json.load(codecs.open(self.profile_path, 'r', encoding='utf8'))

    def get_profile(self):
        return self.profiles
