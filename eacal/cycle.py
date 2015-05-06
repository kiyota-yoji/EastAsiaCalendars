# -*- coding: utf-8 -*-

import solar_terms

import ephem
import jdcal

def cycle_year(year):
    return (year - 4) % 60

def cycle_month(year, month):
    return (year * 12 + month + 12) % 60

def cycle_day(date):
    return (int(jdcal.gcal2jd(date.year, date.month, date.day)[1]) + 50) % 60

def get_cycle_ymd(date):
    d = ephem.Date(date)
    (y_n, y_deg, y_d0) = solar_terms.solar_term_finder_adjacent(d, divisor=360.0,
                                                                remainder=315.0, reverse=True)
    (m_n, m_deg, m_d0) = solar_terms.solar_term_finder_adjacent(d, reverse=True)

    print y_d0
    print m_d0
    c_year = y_d0.datetime().year
    c_month = (m_n + 5) % 24 / 2 + 1

    return (cycle_year(c_year), cycle_month(c_year, c_month), cycle_day(date))

