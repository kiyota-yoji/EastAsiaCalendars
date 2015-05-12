# EastAsiaCalendars README

本プロジェクトでは、Pythonモジュール```eacal```を提供しています。
```eacal```では、中国を起源とし、東アジア地域に広まった暦法の計算機能の実装を目指しています。
現時点では、以下の暦法が実装済みです。

- [二十四節気](http://ja.wikipedia.org/wiki/%E4%BA%8C%E5%8D%81%E5%9B%9B%E7%AF%80%E6%B0%97)
- [干支](http://ja.wikipedia.org/wiki/%E5%B9%B2%E6%94%AF)
- [雑節](http://ja.wikipedia.org/wiki/%E9%9B%91%E7%AF%80)

二十四節気の計算にあたっては、[PyEphem](http://rhodesmill.org/pyephem/)による天体運動計算の結果を利用しています。[国立天文台](http://www.nao.ac.jp/)が発表している[暦要項](http://eco.mtk.nao.ac.jp/koyomi/yoko/)と比較して、概ね1分以内の精度が得られているようです。

結果は無保証です。

## 動作環境

- Python 2.x / 3.x
- [PyEphem](http://rhodesmill.org/pyephem/)
- [pytz](http://pytz.sourceforge.net/)
- [jdcal](https://pypi.python.org/pypi/jdcal)

## インストール

```bash
pip install pyephem
pip install pytz
pip install jdcal
python setup.py install
```

## 使用例

日本語のほか、中国語(繁体字・簡体字)、朝鮮語・韓国語、ベトナム語、英語(訳語)に対応しています。タイムゾーンも指定可能です。

```eacal.EACal(ja=True)``` でインスタンスを作成した場合は、日本語、日本標準時(JST)で取得できます。


### 一年間の二十四節気の計算

```py
>>> import eacal
>>> from eacal.lang import Lang
>>> import pytz
>>> from datetime import datetime
>>> c_j = eacal.EACal(ja=True)    # 日本語、日本標準時(JST)
>>> for x in c_j.get_annual_solar_terms(2015):
...     print "%s %s" % (x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
小寒 2015-01-06 01:20 JST
大寒 2015-01-20 18:43 JST
立春 2015-02-04 12:58 JST
雨水 2015-02-19 08:49 JST
啓蟄 2015-03-06 06:55 JST
春分 2015-03-21 07:45 JST
...
大雪 2015-12-07 19:53 JST
冬至 2015-12-22 13:47 JST

>>> c_u = eacal.EACal(lang=Lang.EN, tz=pytz.timezone('America/New_York'))  # 英語、米国東部標準時(EST)
>>> for x in c_u.get_annual_solar_terms(2015):
...     print "%-25s %s" % (x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
minor cold                2015-01-05 11:20 EST
major cold                2015-01-20 04:43 EST
start of spring           2015-02-03 22:58 EST
rain water                2015-02-18 18:49 EST
awakening of insects      2015-03-05 16:55 EST
vernal equinox            2015-03-20 18:45 EDT  # ここから夏時間(EDT)
...
frost descent             2015-10-23 13:46 EDT  # ここまで夏時間
start of winter           2015-11-07 12:58 EST
minor snow                2015-11-22 10:25 EST
major snow                2015-12-07 05:53 EST
winter solstice           2015-12-21 23:47 EST
```

### 干支暦の計算

年干支、月干支、日干支を計算できます。
二十四節気の計算結果にもとづく節入り日(例: 立春、啓蟄、清明、...)が利用されます。

タイムゾーンによって節入り日が異なるため、年干支・月干支にも差異が生じます。たとえば、2013年4月の節入り日(清明)は、日本・韓国では4月5日、中国・ベトナムでは4月4日となります。よって、2013年4月4日の干支は、日本・韓国では「癸巳年 乙卯月 庚子日」、中国・ベトナムでは「癸巳年 丙辰月 庚子日」となります。

#### 2015年の年干支

```py
>>> import eacal
>>> print(eacal.EACal(ja=True).get_cycle_year(2015))
乙未
>>> print(eacal.EACal().get_cycle_year(2015))
wood-yin goat  # 乙 = 木の弟 = wood-yin, 未 = goat
```

#### 2015年4月の月干支

```py
>>> import eacal
>>> print(eacal.EACal(ja=True).get_cycle_month(2015, 4))
庚辰
>>> print(eacal.EACal().get_cycle_month(2015, 5))
metal-yang dragon  # 庚 = 金の兄 = metal-yang, 辰 = dragon
```

