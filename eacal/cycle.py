# -*- coding: utf-8 -*-

from . import solar_terms

import ephem
import pytz
import jdcal
from datetime import timedelta, datetime, date

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

def search_cycle_month(cm, year_from=1800, year_to=datetime.now().year+1):
    result = []
    year = year_from
    while True:
        for month in range(1, 12+1):
            if cycle_month(year, month) == cm:  # find the first month whose cycle month is equal to cm
                result.append((year, month))
                year_from = year
                for year in range(year_from, year_to+1, 5):
                    result.append((year, month))
                break
        year += 1
        if year > year_to: break
                
    return result

def search_cycle_day(cd, year_from=datetime.now().year-1, year_to=datetime.now().year+1):
    result = []
    day_from = date(year_from, 1, 1)
    day_to = date(year_to+1, 1, 1) - timedelta(days=1)
    day = day_from + timedelta(days=((cd - cycle_day(day_from)) % 60))
    while True:
        result.append(day)
        day += timedelta(days=60)
        if day > day_to: break

    return result

def search_cycle_ymd(cd, cy=None, cm=None, year_from=1800, year_to=datetime.now().year+1, timezone=pytz.utc):
    result = []
    if cy is None:
        date_list = search_cycle_day(cd, year_from=year_from, year_to=year_to)
        for date in date_list:
            dt = timezone.localize(datetime(date.year, date.month, date.day))
            (_cy, _cm, _cd) = cycle_ymd(dt)
            if cm is None or _cm == cm:
                result.append((dt, _cy, _cm, _cd))
    else:
        for year in search_cycle_year(cy, year_from, year_to):
            date_list = search_cycle_day(cd, year_from=year, year_to=year+1)
            for date in date_list:
                dt = timezone.localize(datetime(date.year, date.month, date.day))
                (_cy, _cm, _cd) = cycle_ymd(dt)
                if _cy == cy and (cm is None or _cm == cm):
                    result.append((dt, _cy, _cm, _cd))
    
    return result
    
