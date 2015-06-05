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
    result = []
    year = year_from + (cy - cycle_year(year_from)) % 60  # find the first year whose cycle year is equal to cy
    while True:
        result.append(year)
        year += 60
        if year > year_to: break
    return result

def search_cycle_month(cy, cm, year_from=1800, year_to=datetime.now().year+1):
    result = []
    year = year_from
    if cy is None:
        while True:
            for month in range(1, 12+1):
                if cycle_month(year, month) == cm:
                    result.append((year, month))
                    year_from = year
                    for year in range(year_from, year_to+1, 5):
                        result.append((year, month))
                    break
            year += 1
            if year > year_to: break
    else:
        while True:
            for year in range(year_from, year_to+1):
                # 1月は昨年扱い
                if cycle_year(year-1) == cy and cycle_month(year, 1) == cm:
                    result.append((year, 1))
                    year_from = year
                    for year in range(year_from, year_to+1, 60):
                        result.append((year, 1))
                    break
            year += 1
            if year > year_to: break
                
                
    return result

