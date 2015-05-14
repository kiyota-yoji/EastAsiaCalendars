# -*- coding: utf-8 -*-

class Lang:

    EN       =  10

    ZH_HANT  = 210
    ZH_HANS  = 220
    ZH_P     = 290
    
    JA       = 310
    JA_P     = 390
    
    KO       = 410
    KO_HANJA = 420
    KO_P     = 490

    VI       = 510

SolarTerms = {}

SolarTerms[Lang.EN] = 'start of spring|rain water|awakening of insects|vernal equinox|clear and bright|grain rain|start of summer|grain full|grain in ear|summer solstice|minor heat|major heat|start of autumn|limit of heat|white dew|autumnal equinox|cold dew|frost descent|start of winter|minor snow|major snow|winter solstice|minor cold|major cold'.split('|')

SolarTerms[Lang.ZH_HANT] = u'立春|雨水|驚蟄|春分|清明|穀雨|立夏|小滿|芒種|夏至|小暑|大暑|立秋|處暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'.split('|')
SolarTerms[Lang.ZH_HANS] = u'立春|雨水|惊蛰|春分|清明|谷雨|立夏|小满|芒种|夏至|小暑|大暑|立秋|处暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'.split('|')
SolarTerms[Lang.ZH_P] = u'lìchūn|yǔshuǐ|jīngzhé|chūnfēn|qīngmíng|gǔyǔ|lìxià|xiǎomǎn|mángzhòng|xiàzhì|xiǎoshǔ|dàshǔ|lìqiū|chǔshǔ|báilù|qiūfēn|hánlù|shuāngjiàng|lìdōng|xiǎoxuě|dàxuě|dōngzhì|xiǎohán|dàhán'.split('|')

SolarTerms[Lang.JA] = u'立春|雨水|啓蟄|春分|清明|穀雨|立夏|小満|芒種|夏至|小暑|大暑|立秋|処暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'.split('|')
SolarTerms[Lang.JA_P] = u'risshun|usui|keichitsu|shunbun|seimei|kokuu|rikka|shōman|bōshu|geshi|shōsho|taisho|risshū|shosho|hakuro|shūbun|kanro|sōkō|rittō|shōsetsu|taisetsu|tōji|shōkan|daikan'.split('|')

SolarTerms[Lang.KO] = u'입춘|우수|경칩|춘분|청명|곡우|입하|소만|망종|하지|소서|대서|입추|처서|백로|추분|한로|상강|입동|소설|대설|동지|소한|대한'.split('|')
SolarTerms[Lang.KO_HANJA] = u'立春|雨水|驚蟄|春分|清明|穀雨|立夏|小滿|芒種|夏至|小暑|大暑|立秋|處暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'.split('|')
SolarTerms[Lang.KO_P] = u'ipchun|usu|gyeongchip|chunbun|cheongmyeong|gogu|ipha|soman|mangjong|haji|soseo|daeseo|ipchu|cheoseo|baengno|chubun|hallo|sanggang|ipdong|soseol|daeseol|dongji|sohan|daehan'.split('|')

SolarTerms[Lang.VI] = u'Lập xuân|Vũ thủy|Kinh trập|Xuân phân|Thanh minh|Cốc vũ|Lập hạ|Tiểu mãn|Mang chủng|Hạ chí|Tiểu thử|Đại thử|Lập thu|Xử thử|Bạch lộ|Thu phân|Hàn lộ|Sương giáng|Lập đông|Tiểu tuyết|Đại tuyết|Đông chí|Tiểu hàn|Đại hàn'.split('|')


Stems = {}

Stems[Lang.EN] = 'wood-yang|wood-yin|fire-yang|fire-yin|earth-yang|earth-yin|metal-yang|metal-yin|water-yang|water-yin'.split('|')

Stems[Lang.ZH_HANT] = u'甲|乙|丙|丁|戊|己|庚|辛|壬|癸'.split('|')
Stems[Lang.ZH_HANS] = u'甲|乙|丙|丁|戊|己|庚|辛|壬|癸'.split('|')
Stems[Lang.ZH_P] = u'jiǎ|yǐ|bǐng|dīng|wù|jǐ|gēng|xīn|rén|guǐ'.split('|')

Stems[Lang.JA] = u'甲|乙|丙|丁|戊|己|庚|辛|壬|癸'.split('|')
Stems[Lang.JA+1] = u'きのえ|きのと|ひのえ|ひのと|つちのえ|つちのと|かのえ|かのと|みずのえ|みずのと'.split('|')
Stems[Lang.JA_P] = u'kō|otsu|hei|tei|bo|ki|kō|shin|jin|ki'.split('|')
Stems[Lang.JA_P+1] = u'kinoe|kinoto|hinoe|hinoto|tsuchinoe|tsuchinoto|kanoe|kanoto|mizunoe|mizunoto'.split('|')

Stems[Lang.KO] = u'갑|을|병|정|무|기|경|신|임|계'.split('|')
Stems[Lang.KO_HANJA] = u'甲|乙|丙|丁|戊|己|庚|辛|壬|癸'.split('|')
Stems[Lang.KO_P] = u'gap|eul|byeong|jeong|mu|gi|gyeong|sin|im|gye'.split('|')

Stems[Lang.VI] = u'giáp|ất|bính|đinh|mậu|kỷ|canh|tân|nhâm|quý'.split('|')


Branches = {}

Branches[Lang.EN] = 'rat|ox|tiger|rabbit|dragon|snake|horse|goat|monkey|rooster|dog|pig'.split('|')

Branches[Lang.ZH_HANT] = u'子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥'.split('|')
Branches[Lang.ZH_HANS] = u'子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥'.split('|')
Branches[Lang.ZH_P] = u'zǐ|chǒu|yín|mǎo|chén|sì|wǔ|wèi|shēn|yǒu|xū|hài'.split('|')

Branches[Lang.JA] = u'子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥'.split('|')
Branches[Lang.JA+1] = u'ね|うし|とら|う|たつ|み|うま|ひつじ|さる|とり|いぬ|い'.split('|')
Branches[Lang.JA+2] = u'鼠|牛|虎|兎|龍|蛇|馬|羊|猿|鶏|犬|猪'.split('|')
Branches[Lang.JA_P] = u'shi|chū|in|bō|shin|shi|go|bi|shin|yū|jutsu|gai'.split('|')
Branches[Lang.JA_P+1] = u'ne|ushi|tora|u|tatsu|mi|uma|hitsuji|saru|tori|inu|i'.split('|')

Branches[Lang.KO] = u'자|축|인|묘|진|사|오|미|신|유|술|해'.split('|')
Branches[Lang.KO_HANJA] = u'子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥'.split('|')
Branches[Lang.KO_P] = u'ja|chuk|in|myo|jin|sa|o|mi|sin|yu|sul|hae'.split('|')

Branches[Lang.VI] = u'tý|sửu|dần|mão|thìn|tỵ|ngọ|mùi|thân|dậu|tuất|hợi'.split('|')


Cycle = {}

Cycle[Lang.EN] = ['%s %s' % (Stems[Lang.EN][i % 10],
                             Branches[Lang.EN][i % 12])
                  for i in range(60)]

Cycle[Lang.ZH_HANT] = ['%s%s' % (Stems[Lang.ZH_HANT][i % 10],
                                 Branches[Lang.ZH_HANT][i % 12])
                       for i in range(60)]
Cycle[Lang.ZH_HANS] = ['%s%s' % (Stems[Lang.ZH_HANS][i % 10],
                                 Branches[Lang.ZH_HANS][i % 12])
                       for i in range(60)]
Cycle[Lang.ZH_P] = ['%s %s' % (Stems[Lang.ZH_P][i % 10],
                               Branches[Lang.ZH_P][i % 12])
                    for i in range(60)]

Cycle[Lang.JA] = ['%s%s' % (Stems[Lang.JA][i % 10],
                            Branches[Lang.JA][i % 12])
                  for i in range(60)]
Cycle[Lang.JA+1] = ['%s%s' % (Stems[Lang.JA+1][i % 10],
                              Branches[Lang.JA+1][i % 12])
                    for i in range(60)]
Cycle[Lang.JA_P] = ['%s %s' % (Stems[Lang.JA_P][i % 10],
                               Branches[Lang.JA_P][i % 12])
                    for i in range(60)]
Cycle[Lang.JA_P+1] = ['%s %s' % (Stems[Lang.JA_P+1][i % 10],
                                 Branches[Lang.JA_P+1][i % 12])
                      for i in range(60)]

Cycle[Lang.KO] = ['%s%s' % (Stems[Lang.KO][i % 10],
                            Branches[Lang.KO][i % 12])
                  for i in range(60)]
Cycle[Lang.KO_HANJA] = ['%s%s' % (Stems[Lang.KO_HANJA][i % 10],
                                  Branches[Lang.KO_HANJA][i % 12])
                        for i in range(60)]
Cycle[Lang.KO_P] = ['%s %s' % (Stems[Lang.KO_P][i % 10],
                               Branches[Lang.KO_P][i % 12])
                    for i in range(60)]

Cycle[Lang.VI] = ['%s %s' % (Stems[Lang.VI][i % 10],
                             Branches[Lang.VI][i % 12])
                  for i in range(60)]


JPSeasonalDays = {}

JPSeasonalDays[Lang.EN] = {1: u'doyō:winter',
                           2: u'doyō:spring',
                           3: u'doyō:summer',
                           4: u'doyō:autumn',
                           11: u'higan:spring',
                           12: u'higan:autumn',
                           101: u'setsubun:the day before the start of spring',
                           102: u'hachijū-hachi-ya:the 88th night after the start of spring',
                           103: u'nihyaku-tōka:the 210th day after the start of spring',
                           111: u'nyūbai:the beginning of rainy season',
                           112: u'hangeshō:the end of field work'}

JPSeasonalDays[Lang.JA] = {1: u'土用:冬',
                           2: u'土用:春',
                           3: u'土用:夏',
                           4: u'土用:秋',
                           11: u'彼岸:春',
                           12: u'彼岸:秋',
                           101: u'節分',
                           102: u'八十八夜',
                           103: u'二百十日',
                           111: u'入梅',
                           112: u'半夏生'}
                    

def str_solar_terms(solar_term_id, lang):
    return SolarTerms[lang][solar_term_id]

def str_stems(stem_id, lang, ja_kun_yomi=False):
    if lang == Lang.JA and ja_kun_yomi:
        _lang = Lang.JA + 1
    elif lang == Lang.JA_P and ja_kun_yomi:
        _lang = Lang.JA_P + 1
    else:
        _lang = lang
    return Stems[_lang][stem_id]

def str_branches(branch_id, lang, ja_kun_yomi=False):
    if lang == Lang.JA and ja_kun_yomi:
        _lang = Lang.JA + 1
    elif lang == Lang.JA_P and ja_kun_yomi:
        _lang = Lang.JA_P + 1
    else:
        _lang = lang
    return Branches[_lang][branch_id]
    
def str_cycle(cycle_id, lang, ja_kun_yomi=False):
    if lang == Lang.JA and ja_kun_yomi:
        _lang = Lang.JA + 1
    elif lang == Lang.JA_P and ja_kun_yomi:
        _lang = Lang.JA_P + 1
    else:
        _lang = lang
    return Cycle[_lang][cycle_id]
    
def str_jp_seasonal_days(day_id, lang):
    if lang == Lang.JA:
        _lang = Lang.JA
    else:
        _lang = Lang.EN
    return JPSeasonalDays[_lang][day_id]
    
