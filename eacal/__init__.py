# -*- coding: utf-8 -*-

import cycle
from lang import Lang, str_cycle

import pytz
from datetime import datetime


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

    def get_cycle_ymd(self, dt, id=False):

        # if "dt" is a tuple, it is interpreted as (year, month, day)
        if isinstance(dt, tuple):
            dt = datetime(dt[0], dt[1], dt[2])
        
        # if "dt" is a naive datetime, it is interpreted using 
        # the specified timezone.
        if dt.tzinfo is None:
            dt = self.tz.localize(dt)

        (y_id, m_id, d_id) = cycle.cycle_ymd(dt)

        if id:
            return (y_id, m_id, d_id)
        else:
            return (str_cycle(y_id, self.lang), 
                    str_cycle(m_id, self.lang), 
                    str_cycle(d_id, self.lang))

