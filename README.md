# EastAsiaCalendars README

EastAsiaCalendars provides an ```eacal``` Python module for accessing
East Asia calendar systems, originated in China, and spread to Korea,
Vietnam, and Japan. This module includes the following.

- [solar terms](http://en.wikipedia.org/wiki/Solar_term) (節氣, 节气, 節気, 절기, tiết khí)
- [sexagenary cycle](http://en.wikipedia.org/wiki/Sexagenary_cycle) (六十花甲, 干支, 간지, Gānzhī)
- [zassetsu](http://ja.wikipedia.org/wiki/%E9%9B%91%E7%AF%80) (雑節, Seasonal days in the Japanese calendar)

Solar terms are calculated based on the planetary motion computed by [PyEphem](http://rhodesmill.org/pyephem/). The accuracy of solar terms may be within one minute.

Results of use of this software is not warrantied. You may use, modify, and redistribute this software under [GNU LESSER GENERAL PUBLIC LICENSE Version 3](http://www.gnu.org/licenses/lgpl.html).

## Requirements

- Python 2.x / 3.x
- [PyEphem](http://rhodesmill.org/pyephem/)
- [pytz](http://pytz.sourceforge.net/)
- [jdcal](https://pypi.python.org/pypi/jdcal)

## Installation

The required packages (PyEphem, pytz, and jdcal) are automatically installed via ```pip```.

```bash
pip install eacal
```

## Example & Usage

This package supports Chinese (traditional / simplified), Japanese, Korean, Vietnamese, and English (translation).
Any timezones can be specified using the pytz package.

### Calculating solar terms in a year

The solar terms of 2015 for English (in UTC).

```py
>>> import eacal
>>> from datetime import datetime
>>> c = eacal.EACal()
>>> for x in c.get_annual_solar_terms(2015):
...     print "%2d %-25s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 minor cold                2015-01-05 16:20 UTC
23 major cold                2015-01-20 09:43 UTC
 0 start of spring           2015-02-04 03:58 UTC
 1 rain water                2015-02-18 23:49 UTC
 2 awakening of insects      2015-03-05 21:55 UTC
 3 vernal equinox            2015-03-20 22:45 UTC
...
20 major snow                2015-12-07 10:53 UTC
21 winter solstice           2015-12-22 04:47 UTC
```

The solar terms of 2015, for Traditional Chinese (in Hong Kong Time), Simplified Chinese (in Chinese Standard Time), Japanese (in Japan Standard Time), Korean (in Korea Standard Time), and Vietnamese (in Indochina Time).

```py
>>> import eacal
>>> from datetime import datetime
>>> c_t = eacal.EACal(zh_t=True)
>>> for x in c_t.get_annual_solar_terms(2015):
...     print "%2d %s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 小寒 2015-01-06 00:20 HKT
23 大寒 2015-01-20 17:43 HKT
 0 立春 2015-02-04 11:58 HKT
 1 雨水 2015-02-19 07:49 HKT
 2 驚蟄 2015-03-06 05:55 HKT
 3 春分 2015-03-21 06:45 HKT
...
20 大雪 2015-12-07 18:53 HKT
21 冬至 2015-12-22 12:47 HKT

>>> c_s = eacal.EACal(zh_s=True)
>>> for x in c_s.get_annual_solar_terms(2015):
...     print "%2d %s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 小寒 2015-01-06 00:20 CST
23 大寒 2015-01-20 17:43 CST
 0 立春 2015-02-04 11:58 CST
 1 雨水 2015-02-19 07:49 CST
 2 惊蛰 2015-03-06 05:55 CST
 3 春分 2015-03-21 06:45 CST
小寒 2015-01-06 00:20 CST
大寒 2015-01-20 17:43 CST
立春 2015-02-04 11:58 CST
雨水 2015-02-19 07:49 CST
惊蛰 2015-03-06 05:55 CST
春分 2015-03-21 06:45 CST
...
20 大雪 2015-12-07 18:53 CST
21 冬至 2015-12-22 12:47 CST

>>> c_j = eacal.EACal(ja=True)
>>> for x in c_j.get_annual_solar_terms(2015):
...     print "%2d %s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 小寒 2015-01-06 01:20 JST
23 大寒 2015-01-20 18:43 JST
 0 立春 2015-02-04 12:58 JST
 1 雨水 2015-02-19 08:49 JST
 2 啓蟄 2015-03-06 06:55 JST
 3 春分 2015-03-21 07:45 JST
...
20 大雪 2015-12-07 19:53 JST
21 冬至 2015-12-22 13:47 JST

>>> c_k = eacal.EACal(ko=True)
>>> for x in c_k.get_annual_solar_terms(2015):
...     print "%2d %s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 소한 2015-01-06 01:20 KST
23 대한 2015-01-20 18:43 KST
 0 입춘 2015-02-04 12:58 KST
 1 우수 2015-02-19 08:49 KST
 2 경칩 2015-03-06 06:55 KST
 3 춘분 2015-03-21 07:45 KST
...
20 대설 2015-12-07 19:53 KST
21 동지 2015-12-22 13:47 KST

>>> c_v = eacal.EACal(vi=True)
>>> for x in c_v.get_annual_solar_terms(2015):
...     print "%2d %-12s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 Tiểu hàn     2015-01-05 23:20 ICT
23 Đại hàn      2015-01-20 16:43 ICT
 0 Lập xuân     2015-02-04 10:58 ICT
 1 Vũ thủy      2015-02-19 06:49 ICT
 2 Kinh trập    2015-03-06 04:55 ICT
 3 Xuân phân    2015-03-21 05:45 ICT
...
20 Đại tuyết    2015-12-07 17:53 ICT
21 Đông chí     2015-12-22 11:47 ICT
```

The solar terms of 2015 in North American Eastern Time Zone.

```py
>>> import eacal
>>> import pytz
>>> from datetime import datetime
>>> c = eacal.EACal(tz=pytz.timezone('America/New_York'))
>>> for x in c.get_annual_solar_terms(2015):
...     print "%2d %-25s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 minor cold                2015-01-05 11:20 EST
23 major cold                2015-01-20 04:43 EST
 0 start of spring           2015-02-03 22:58 EST
 1 rain water                2015-02-18 18:49 EST
 2 awakening of insects      2015-03-05 16:55 EST
 3 vernal equinox            2015-03-20 18:45 EDT  # in DST
...
20 major snow                2015-12-07 05:53 EST
21 winter solstice           2015-12-21 23:47 EST
```


### Calculating sexagenary cycles

Calculating the cyclic year of 2015.

```py
>>> import eacal
>>> print(eacal.EACal().get_cycle_year(2015))
wood-yin goat   # 乙未
>>> print(eacal.EACal(zh_t=True).get_cycle_year(2015))
乙未
>>> print(eacal.EACal(vi=True).get_cycle_year(2015))
ất mùi   # 乙未
>>> print(eacal.EACal().get_cycle_year(2015, id=True))
31       # 31=wood-yin goat
```

Calculating the Cyclic month of May 2015.

```py
>>> import eacal
>>> print(eacal.EACal().get_cycle_month(2015, 5))
metal-yin snake   # 辛巳
>>> print(eacal.EACal(ja=True).get_cycle_month(2015, 5))
辛巳
>>> print(eacal.EACal(ko=True).get_cycle_month(2015, 5))
신사   # 辛巳
>>> print(eacal.EACal().get_cycle_month(2015, 5, id=True))
17    # 17=metal-yin snake
```

Calculating the Cyclic day of 10th, May 2015.
```py
>>> import eacal
>>> from datetime import datetime
>>> print(eacal.EACal().get_cycle_day(datetime(2015, 5, 10)))
fire-yang dog   # 丙戌
>>> print(eacal.EACal(zh_s=True).get_cycle_day(datetime(2015, 5, 10)))
丙戌
>>> print(eacal.EACal(vi=True).get_cycle_day(datetime(2015, 5, 10)))
bính tuất   # 丙戌
>>> print(eacal.EACal().get_cycle_day(datetime(2015, 5, 10), id=True))
22          # 22=fire-yang dog
```

Calculating the Cyclic year, month, and day around the start of spring in 2015.
```py
>>> import eacal
>>> from datetime import datetime
>>> c = eacal.EACal()     # for English, in UTC
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 3))))
wood-yang horse|fire-yin ox|metal-yang dog     # 甲午年 丁丑月 庚戌日
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 4))))
wood-yin goat|earth-yang tiger|metal-yin pig   # 乙未年 戊寅月 辛亥日 (cyclic year and cyclic month incremented at the start of spring)
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 5))))
wood-yin goat|earth-yang tiger|water-yang rat  # 乙未年 戊寅月 壬子日
>>> print(c.get_cycle_ymd(datetime(2015, 2, 3), id=True))
(30, 13, 46)    # 30=wood-yang horse, 13=fire-yin ox, 46=metal-yang dog
>>> print(c.get_cycle_ymd(datetime(2015, 2, 4), id=True))
(31, 14, 47)    # 31=wood-yin goat, 14=earth-yang tiger, 47=metal-yin pig
>>> print(c.get_cycle_ymd(datetime(2015, 2, 5), id=True))
(31, 14, 48)    # 48=water-yang rat
```

### Calculating Zassetsu

```py
>>> import eacal
>>> import pytz
>>> from datetime import datetime, timedelta
>>> c = eacal.EACal(tz=pytz.timezone('Asia/Tokyo'))   # for English, in Japan Standard Time
>>> for x in c.get_annual_jp_seasonal_days(2015):
...    if len(x) == 4:
...        print("%3d %s %s %s" % (x[1], datetime.strftime(x[2], "%Y-%m-%d"), datetime.strftime(x[3]-timedelta(days=1), "%Y-%m-%d"), x[0]))
...    else:
...        print("%3d %s %s" % (x[1], datetime.strftime(x[2], "%Y-%m-%d"), x[0]))
  1 2015-01-17 2015-02-03 doyō:winter
  2 2015-04-17 2015-05-05 doyō:spring
  3 2015-07-20 2015-08-07 doyō:summer
  4 2015-10-21 2015-11-07 doyō:autumn
 11 2015-03-18 2015-03-24 higan:spring
 12 2015-09-20 2015-09-26 higan:autumn
101 2015-02-03 setsubun:the day before the start of spring
102 2015-05-02 hachijū-hachi-ya:the 88th night after the start of spring
103 2015-09-01 nihyaku-tōka:the 210th day after the start of spring
111 2015-06-11 nyūbai:the beginning of rainy season
112 2015-07-02 hangeshō:the end of field work

>>> c_j = eacal.EACal(ja=True)   # for Japanese, in Japan Standard Time
>>> for x in c_j.get_annual_jp_seasonal_days(2015):
...    if len(x) == 4:
...        print("%3d %s %s %s" % (x[1], datetime.strftime(x[2], "%Y-%m-%d"), datetime.strftime(x[3]-timedelta(days=1), "%Y-%m-%d"), x[0]))
...    else:
...        print("%3d %s %s" % (x[1], datetime.strftime(x[2], "%Y-%m-%d"), x[0]))
  1 2015-01-17 2015-02-03 土用:冬
  2 2015-04-17 2015-05-05 土用:春
  3 2015-07-20 2015-08-07 土用:夏
  4 2015-10-21 2015-11-07 土用:秋
 11 2015-03-18 2015-03-24 彼岸:春
 12 2015-09-20 2015-09-26 彼岸:秋
101 2015-02-03 節分
102 2015-05-02 八十八夜
103 2015-09-01 二百十日
111 2015-06-11 入梅
112 2015-07-02 半夏生
```

## History

### Version 0.0.3 (2015-05-17)

- Add an "id" option to get_cycle_year(), get_cycle_month(), and get_cycle_day()
	- this option enabled the methods to return IDs (0-59) of the sexagenary cycle.
- Refine implementations of solar_term_finder()
- Renumber IDs of solar terms
	- begins at "start of spring" (0=start of spring - 23=major cold)

### Version 0.0.2 (2015-05-13)

- Fixed documents (README.md, README_ja.md)
- Add install_requires to setup.py
	- required packages PyEphem, pytz, and jdcal are automatically installed via pip
- Fixed a earthly branch in English

### Version 0.0.1 (2015-05-12)

- The first release.


## TODO

- a method for finding days which have a specified sexagenary cycle
- lunisolar calendars
- regnal years
- adapt to Chinese cycle years
- write unit tests
- documentation for Windows environments
