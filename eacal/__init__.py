# -*- coding: utf-8 -*-

from lang import Lang
import pytz

class EACal:

    def __init__(self, lang=Lang.EN, tz=pytz.utc,
                 shortcut_zh_t=False, shortcut_zh_s=False,
                 shortcut_ja=False, shortcut_ko=False,
                 shortcut_vi=False):
        self.lang = lang
        self.tz = tz
        if shortcut_zh_t:
            self.lang = Lang.ZH_HANT
            self.tz = pytz.timezone('Asia/Hong_Kong')
        elif shortcut_zh_s:
            self.lang = Lang.ZH_HANS
            self.tz = pytz.timezone('Asia/Shanghai')
        elif shortcut_ja:
            self.lang = Lang.JA
            self.tz = pytz.timezone('Asia/Tokyo')
        elif shortcut_ko:
            self.lang = Lang.KO
            self.tz = pytz.timezone('Asia/Seoul')
        elif shortcut_vi:
            self.lang = Lang.VI
            self.tz = pytz.timezone('Asia/Ho_Chi_Minh')

        print "lang=%d tz=%s" % (self.lang, self.tz)

