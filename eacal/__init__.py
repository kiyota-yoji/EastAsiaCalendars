# -*- coding: utf-8 -*-

from . import cycle
from . import solar_terms
from .lang import Lang, str_solar_terms, str_cycle, str_jp_seasonal_days

import pytz
from datetime import datetime, timedelta


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

    def get_cycle_year(self, year, id=False):
        if id:
            return cycle.cycle_year(year)
        else:
            return str_cycle(cycle.cycle_year(year), self.lang)

    def get_cycle_month(self, year, month, id=False):
        if id:
            return cycle.cycle_month(year, month)
        else:
            return str_cycle(cycle.cycle_month(year, month), self.lang)

    def get_cycle_day(self, date, id=False):
        if id:
            return cycle.cycle_day(dt)
        else:
            return str_cycle(cycle.cycle_day(dt), self.lang)

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

    def get_annual_solar_terms(self, year,
                               boundary_previous=False, 
                               boundary_following=False):

        st_list = solar_terms.annual_solar_terms(year, 
                                                 boundary_previous,
                                                 boundary_following)
        result = []
        for st in st_list:
            (st_id, st_dt_utc) = st
            st_str = str_solar_terms(st_id, self.lang)
            st_dt_local = st_dt_utc.astimezone(self.tz)
            st_new = (st_str, st_id, st_dt_local)
            result.append(st_new)
        return result

    def get_annual_jp_seasonal_days(self, year):
        
        doyo_days = solar_terms.annual_jp_doyo_days(year)
        higan_days = solar_terms.annual_jp_higan_days(year)
        other_days = solar_terms.annual_jp_seasonal_days(year)

        result = []

        for (d_id, d_start, d_end) in doyo_days:
            d_str = str_jp_seasonal_days(d_id, self.lang)
            d_local_start = d_start.astimezone(self.tz)
            d_local_end   = d_end.astimezone(self.tz)
            d_new = (d_str, d_id, d_local_start, d_local_end)
            result.append(d_new)

        for (d_id, d_start, d_end) in higan_days:
            d_str = str_jp_seasonal_days(d_id, self.lang)
            d_local_start = d_start.astimezone(self.tz).replace(hour=0, minute=0, second=0, microsecond=0)
            d_local_end   = d_end.astimezone(self.tz).replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
            d_new = (d_str, d_id, d_local_start, d_local_end)
            result.append(d_new)

        for (d_id, d_dt) in other_days:
            d_str = str_jp_seasonal_days(d_id, self.lang)
            if d_id in [101, 102, 103]:
                d_local_dt = d_dt.astimezone(self.tz).replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                d_local_dt = d_dt.astimezone(self.tz)
            d_new = (d_str, d_id, d_local_dt)
            result.append(d_new)

        return result
            
            
