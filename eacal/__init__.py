# -*- coding: utf-8 -*-

from . import cycle
from . import solar_terms
from .lang import Lang, str_solar_terms, str_cycle, str_jp_seasonal_days, id_solar_terms, id_cycle

import pytz
from datetime import datetime, timedelta


class EACal:

    def __init__(self, lang=Lang.EN, tz=pytz.utc,
                 zh_t=False, zh_s=False,
                 ja=False, ko=False,
                 vi=False, year_range=(1800, datetime.now().year+1)):
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
        self.year_range = year_range

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

    def get_cycle_day(self, dt, id=False):
        
        # if "dt" is a tuple, it is interpreted as (year, month, day)
        if isinstance(dt, tuple):
            dt = datetime(dt[0], dt[1], dt[2])
        
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

    def get_specified_solar_term(self, year, st):

        if isinstance(st, int):
            st_id = st
            st_str = str_solar_terms(st_id, self.lang)
        else:
            # find st_id by searching
            st_id = id_solar_terms(st, self.lang)
            st_str = str_solar_terms(st_id, self.lang)
            
        st_dt_utc = solar_terms.specified_solar_term(year, st_id)
        st_dt_local = st_dt_utc.astimezone(self.tz)
        return (st_str, st_id, st_dt_local)

    def get_specified_cycle_years(self, cy):
        cy_str, cy_id = self._get_cycle_id(cy)

        years_list = cycle.search_cycle_year(cy_id, year_from=self.year_range[0],
                                             year_to=self.year_range[1])
        return (cy_str, cy_id, years_list)

    def get_specified_cycle_months(self, cm):
        cm_str, cm_id = self._get_cycle_id(cm)

        months_list = cycle.search_cycle_month(cm_id, year_from=self.year_range[0],
                                               year_to=self.year_range[1])
        return (cm_str, cm_id, months_list)

    def get_specified_cycle_days(self, cd):
        cd_str, cd_id = self._get_cycle_id(cd)

        days_list = cycle.search_cycle_day(cd_id, year_from=self.year_range[0],
                                           year_to=self.year_range[1])
        return (cd_str, cd_id, days_list)
        
    def _get_cycle_id(self, c):
        if isinstance(c, int):
            c_id = c
            c_str = str_cycle(c_id, self.lang)
        else:
            # find c_id by searching
            c_id = id_cycle(c, self.lang)
            c_str = str_cycle(c_id, self.lang)
        return (c_str, c_id)

