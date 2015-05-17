# EastAsiaCalendars README

本プロジェクトでは、Pythonモジュール ```eacal``` を提供しています。
```eacal``` は、中国を起源とし、東アジア地域に広まった暦法の計算機能の実装を目指しています。
現時点では、以下の暦法が実装済みです。

- [二十四節気](http://ja.wikipedia.org/wiki/%E4%BA%8C%E5%8D%81%E5%9B%9B%E7%AF%80%E6%B0%97)
- [干支](http://ja.wikipedia.org/wiki/%E5%B9%B2%E6%94%AF)
- [雑節](http://ja.wikipedia.org/wiki/%E9%9B%91%E7%AF%80)

二十四節気の計算にあたっては、[PyEphem](http://rhodesmill.org/pyephem/)による天体運動計算の結果を利用しています。[国立天文台](http://www.nao.ac.jp/)が発表している[暦要項](http://eco.mtk.nao.ac.jp/koyomi/yoko/)と比較して、概ね1分以内の精度が得られているようです。

本ソフトウェアの利用の結果は無保証です。本ソフトウェアの利用、修正、再配布は[GNU LESSER GENERAL PUBLIC LICENSE Version 3](http://www.gnu.org/licenses/lgpl.html)に従ってください。


## 動作環境

- Python 2.x / 3.x
- [PyEphem](http://rhodesmill.org/pyephem/)
- [pytz](http://pytz.sourceforge.net/)
- [jdcal](https://pypi.python.org/pypi/jdcal)

## インストール

```pip``` を使うと、必要なパッケージ(PyEphem, pytz, jdcal)もあわせて自動的にインストールされます。

```bash
pip install eacal
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

>>> c_u = eacal.EACal(lang=Lang.EN, tz=pytz.timezone('America/New_York'))  # 英語、米国東部標準時(EST)
>>> for x in c_u.get_annual_solar_terms(2015):
...     print "%2d %-25s %s" % (x[1], x[0], datetime.strftime(x[2], "%Y-%m-%d %H:%M %Z"))
22 minor cold                2015-01-05 11:20 EST
23 major cold                2015-01-20 04:43 EST
 0 start of spring           2015-02-03 22:58 EST
 1 rain water                2015-02-18 18:49 EST
 2 awakening of insects      2015-03-05 16:55 EST
 3 vernal equinox            2015-03-20 18:45 EDT  # ここから夏時間(EDT)
...
17 frost descent             2015-10-23 13:46 EDT  # ここまで夏時間
18 start of winter           2015-11-07 12:58 EST
19 minor snow                2015-11-22 10:25 EST
20 major snow                2015-12-07 05:53 EST
21 winter solstice           2015-12-21 23:47 EST
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
>>> print(eacal.EACal(ja=True).get_cycle_year(2015, id=True))
31             # 31=乙未
```

#### 2015年5月の月干支

```py
>>> import eacal
>>> print(eacal.EACal(ja=True).get_cycle_month(2015, 5))
辛巳
>>> print(eacal.EACal().get_cycle_month(2015, 5))
metal-yin snake  # 辛 = 金の弟 = metal-yin, 巳 = snake
>>> print(eacal.EACal(ja=True).get_cycle_month(2015, 5, id=True))
17               # 17=辛巳
```

#### 2015年5月10日の日干支

```py
>>> import eacal
>>> from datetime import datetime
>>> print(eacal.EACal(ja=True).get_cycle_day(datetime(2015, 5, 10)))
丙戌
>>> print(eacal.EACal().get_cycle_day(datetime(2015, 5, 10)))
fire-yang dog    # 丙 = 火の兄 = fire-yang, 戌 = dog
>>> print(eacal.EACal(ja=True).get_cycle_day(datetime(2015, 5, 10), id=True))
22               # 22=丙戌
```

#### 年干支、月干支、日干支を同時に取得 (2015年の立春前後)

```py
>>> import eacal
>>> from datetime import datetime
>>> c = eacal.EACal(ja=True)
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 3))))
甲午|丁丑|庚戌
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 4))))
乙未|戊寅|辛亥    # 立春(節入り日)で年干支、月干支が一つ進む (甲午→乙未、丁丑→戊寅)
>>> print('|'.join(c.get_cycle_ymd(datetime(2015, 2, 5))))
乙未|戊寅|壬子    # 節入り日以外は日干支のみ一つ進む (辛亥→壬子)
>>> print(c.get_cycle_ymd(datetime(2015, 2, 3), id=True))
(30, 13, 46)    # 30=甲午, 13=丁丑, 46=庚戌
>>> print(c.get_cycle_ymd(datetime(2015, 2, 4), id=True))
(31, 14, 47)    # 31=乙未, 14=戊寅, 47=辛亥
>>> print(c.get_cycle_ymd(datetime(2015, 2, 5), id=True))
(31, 14, 48)    # 48=壬子
```

### 雑節の計算

```py
>>> import eacal
>>> import pytz
>>> from datetime import datetime, timedelta
>>> c_j = eacal.EACal(ja=True)
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

## 変更履歴

### Version 0.0.3 (2015-05-17)

- "id"オプションを干支暦用メソッド get_cycle_year(), get_cycle_month(), get_cycle_day() に追加
	- 干支のID番号(0-59)を取得可能に
- solar_term_finder() の実装を改善
- 二十四節気のID番号体系を変更
	- 立春から開始 (0=立春 → 23=大寒)

### Version 0.0.2 (2015-05-13)

- ドキュメントの訂正 (README.md, README_ja.md)
- setup.py にパッケージ依存関係(install_requires)オプションを追加
	- pip によるインストールの際、 PyEphem, pytz, jdcal が自動的にインストールされます
- 地支の英語表現にスペルミスがあったため修正

### Version 0.0.1 (2015-05-12)

- 最初のリリース


## TODO

- 干支暦からの日付の検索
- 旧暦 (太陰太陽暦)
- 元号
- 中国語圏での年干支の扱いへの対応
- ユニットテストの実装
- Windows環境でのインストール手順の記載
