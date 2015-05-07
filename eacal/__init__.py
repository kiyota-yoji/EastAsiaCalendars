# -*- coding: utf-8 -*-

from lang import Lang
import pytz

class EACal:

    def __init__(self, lang=Lang.EN, tz=pytz.utc,
                 zh_t=False, zh_s=False,
                 ja=False, ko=False,
                 vi=False):
        self.lang = lang
        self.tz = tz
        if zh_t:
            self.lang = Lang.ZH_HANT
            self.tz = pytz.timezone('Asia/Hong_Kong')
        elif zh_s:
            self.lang = Lang.ZH_HANS
            self.tz = pytz.timezone('Asia/Shanghai')
        elif ja:
            self.lang = Lang.JA
            self.tz = pytz.timezone('Asia/Tokyo')
        elif ko:
            self.lang = Lang.KO
            self.tz = pytz.timezone('Asia/Seoul')
        elif vi:
            self.lang = Lang.VI
            self.tz = pytz.timezone('Asia/Ho_Chi_Minh')

