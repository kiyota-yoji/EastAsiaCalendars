# -*- coding: utf-8 -*-

from . import solar_terms

import ephem
import pytz
import jdcal
from datetime import timedelta, datetime

def cycle_year(year):
    return (year - 4) % 60

def cycle_month(year, month):
    return (year * 12 + month + 12) % 60

def cycle_day(date):
    return (int(jdcal.gcal2jd(date.year, date.month, date.day)[1]) + 50) % 60

def cycle_ymd(date):
    date_start = date.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    d = ephem.Date(date_start.astimezone(pytz.utc))
    (y_n, y_deg, y_d0) = solar_terms.solar_term_finder_adjacent(d, divisor=360.0,
                                                                remainder=315.0, reverse=True)
    (m_n, m_deg, m_d0) = solar_terms.solar_term_finder_adjacent(d, reverse=True)
    date_ym = m_d0.datetime() + timedelta(days=15)
    
    return (cycle_year(y_d0.datetime().year), cycle_month(date_ym.year, date_ym.month), cycle_day(date))

def search_cycle_year(cy, year_from=1800, year_to=datetime.now().year+1):
    year = year_from + (cy + 4 - year_from) % 60
    result = []
    while True:
        result.append(year)
        year += 60
        if year > year_to: break
    return result
