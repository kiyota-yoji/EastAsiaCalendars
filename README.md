# EastAsiaCalendars README

EastAsiaCalendars provides an ```eacal``` Python module for accessing
East Asia calendar systems, originated in China, and spread to Korea,
Vietnam, and Japan. This module includes the following.

- [solar terms](http://en.wikipedia.org/wiki/Solar_term) (節氣, 节气, 節気, 절기, tiết khí)
- [sexagenary cycle](http://en.wikipedia.org/wiki/Sexagenary_cycle) (六十花甲, 干支, 간지, Gānzhī)
- [zassetsu](http://ja.wikipedia.org/wiki/%E9%9B%91%E7%AF%80) (Seasonal days in the Japanese calendar)

## Requirements

- Python 2.7
- [PyEphem](http://rhodesmill.org/pyephem/)
- [pytz](http://pytz.sourceforge.net/)
- [jdcal](https://pypi.python.org/pypi/jdcal)

## Installation

```bash
pip install pyephem
pip install pytz
pip install jdcal
python setup.py install
```

## Example & Usage

### Calculating solar terms in a year

The solar terms of 2015, in UTC (in English)

```py
>>> import eacal
>>> from datetime import datetime
>>> c = eacal.EACal()
>>> for x in c.get_annual_solar_terms(2015):
...     print "%-25s %s" % (x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
... 
minor cold                2015-01-05 16:20 UTC
major cold                2015-01-20 09:43 UTC
start of spring           2015-02-04 03:58 UTC
rain water                2015-02-18 23:49 UTC
awakening of insects      2015-03-05 21:55 UTC
vernal equinox            2015-03-20 22:45 UTC
clear and bright          2015-04-05 02:39 UTC
grain rain                2015-04-20 09:41 UTC
start of summer           2015-05-05 19:52 UTC
grain full                2015-05-21 08:44 UTC
grain in ear              2015-06-05 23:58 UTC
summer solstice           2015-06-21 16:38 UTC
minor heat                2015-07-07 10:12 UTC
major heat                2015-07-23 03:30 UTC
start of autumn           2015-08-07 20:01 UTC
limit of heat             2015-08-23 10:37 UTC
white dew                 2015-09-07 22:59 UTC
autumnal equinox          2015-09-23 08:20 UTC
cold dew                  2015-10-08 14:42 UTC
frost descent             2015-10-23 17:46 UTC
start of winter           2015-11-07 17:58 UTC
minor snow                2015-11-22 15:25 UTC
major snow                2015-12-07 10:53 UTC
winter solstice           2015-12-22 04:47 UTC
```

The solar terms of 2015, in Hong Kong Time (in Traditional Chinese)

```py
>>> import eacal
>>> from datetime import datetime
>>> c = eacal.EACal(zh_t=True)
>>> for x in c.get_annual_solar_terms(2015):
...     print "%s %s" % (x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
... 
小寒 2015-01-06 00:20 HKT
大寒 2015-01-20 17:43 HKT
立春 2015-02-04 11:58 HKT
雨水 2015-02-19 07:49 HKT
驚蟄 2015-03-06 05:55 HKT
春分 2015-03-21 06:45 HKT
清明 2015-04-05 10:39 HKT
穀雨 2015-04-20 17:41 HKT
立夏 2015-05-06 03:52 HKT
小滿 2015-05-21 16:44 HKT
芒種 2015-06-06 07:58 HKT
夏至 2015-06-22 00:38 HKT
小暑 2015-07-07 18:12 HKT
大暑 2015-07-23 11:30 HKT
立秋 2015-08-08 04:01 HKT
處暑 2015-08-23 18:37 HKT
白露 2015-09-08 06:59 HKT
秋分 2015-09-23 16:20 HKT
寒露 2015-10-08 22:42 HKT
霜降 2015-10-24 01:46 HKT
立冬 2015-11-08 01:58 HKT
小雪 2015-11-22 23:25 HKT
大雪 2015-12-07 18:53 HKT
冬至 2015-12-22 12:47 HKT
```
