# -*- coding: utf-8 -*-

import ephem, sys
from math import pi, floor, fabs, sin, cos

NUT_SCALE = 1e4
NUT_SERIES = 106
NUT_MAXMUL = 4

SECPERCIRC = (3600. * 360.)

def degrad(x):
    return x * pi / 180.

'''Delaunay arguments, in arc seconds; they differ slightly from ELP82B'''
delaunay = [
    [485866.733,  1717915922.633, 31.310,  0.064], # M', moon mean anom
    [1287099.804, 129596581.224,  -0.577, -0.012], # M, sun mean anom
    [335778.877,  1739527263.137, -13.257, 0.011], # F, moon arg lat
    [1072261.307, 1602961601.328, -6.891,  0.019], # D, elong moon sun
    [450160.280,  -6962890.539,   7.455,   0.008], # Om, moon l asc node
]


'''multipliers for Delaunay arguments'''
multarg = [
    # bounds:  -2..3, -2..2, -2/0/2/4, -4..4, 0..2
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2],
    [-2, 0, 2, 0, 1],
    [2, 0, -2, 0, 0],
    [-2, 0, 2, 0, 2],
    [1, -1, 0, -1, 0],
    [0, -2, 2, -2, 1],
    [2, 0, -2, 0, 1],
    [0, 0, 2, -2, 2],
    [0, 1, 0, 0, 0],
    [0, 1, 2, -2, 2],
    [0, -1, 2, -2, 2],
    [0, 0, 2, -2, 1],
    [2, 0, 0, -2, 0],
    [0, 0, 2, -2, 0],
    [0, 2, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 2, 2, -2, 2],
    [0, -1, 0, 0, 1],
    [-2, 0, 0, 2, 1],
    [0, -1, 2, -2, 1],
    [2, 0, 0, -2, 1],
    [0, 1, 2, -2, 1],
    [1, 0, 0, -1, 0],
    [2, 1, 0, -2, 0],
    [0, 0, -2, 2, 1],
    [0, 1, -2, 2, 0],
    [0, 1, 0, 0, 2],
    [-1, 0, 0, 1, 1],
    [0, 1, 2, -2, 0],
    [0, 0, 2, 0, 2],
    [1, 0, 0, 0, 0],
    [0, 0, 2, 0, 1],
    [1, 0, 2, 0, 2],
    [1, 0, 0, -2, 0],
    [-1, 0, 2, 0, 2],
    [0, 0, 0, 2, 0],
    [1, 0, 0, 0, 1],
    [-1, 0, 0, 0, 1],
    [-1, 0, 2, 2, 2],
    [1, 0, 2, 0, 1],
    [0, 0, 2, 2, 2],
    [2, 0, 0, 0, 0],
    [1, 0, 2, -2, 2],
    [2, 0, 2, 0, 2],
    [0, 0, 2, 0, 0],
    [-1, 0, 2, 0, 1],
    [-1, 0, 0, 2, 1],
    [1, 0, 0, -2, 1],
    [-1, 0, 2, 2, 1],
    [1, 1, 0, -2, 0],
    [0, 1, 2, 0, 2],
    [0, -1, 2, 0, 2],
    [1, 0, 2, 2, 2],
    [1, 0, 0, 2, 0],
    [2, 0, 2, -2, 2],
    [0, 0, 0, 2, 1],
    [0, 0, 2, 2, 1],
    [1, 0, 2, -2, 1],
    [0, 0, 0, -2, 1],
    [1, -1, 0, 0, 0],
    [2, 0, 2, 0, 1],
    [0, 1, 0, -2, 0],
    [1, 0, -2, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 2, 0, 0],
    [1, -1, 2, 0, 2],
    [-1, -1, 2, 2, 2],
    [-2, 0, 0, 0, 1],
    [3, 0, 2, 0, 2],
    [0, -1, 2, 2, 2],
    [1, 1, 2, 0, 2],
    [-1, 0, 2, -2, 1],
    [2, 0, 0, 0, 1],
    [1, 0, 0, 0, 2],
    [3, 0, 0, 0, 0],
    [0, 0, 2, 1, 2],
    [-1, 0, 0, 0, 2],
    [1, 0, 0, -4, 0],
    [-2, 0, 2, 2, 2],
    [-1, 0, 2, 4, 2],
    [2, 0, 0, -4, 0],
    [1, 1, 2, -2, 2],
    [1, 0, 2, 2, 1],
    [-2, 0, 2, 4, 2],
    [-1, 0, 4, 0, 2],
    [1, -1, 0, -2, 0],
    [2, 0, 2, -2, 1],
    [2, 0, 2, 2, 2],
    [1, 0, 0, 2, 1],
    [0, 0, 4, -2, 2],
    [3, 0, 2, -2, 2],
    [1, 0, 2, -2, 0],
    [0, 1, 2, 0, 1],
    [-1, -1, 0, 2, 1],
    [0, 0, -2, 0, 1],
    [0, 0, 2, -1, 2],
    [0, 1, 0, 2, 0],
    [1, 0, -2, -2, 0],
    [0, -1, 2, 0, 1],
    [1, 1, 0, -2, 1],
    [1, 0, -2, 2, 0],
    [2, 0, 0, 2, 0],
    [0, 0, 2, 4, 2],
    [0, 1, 0, 1, 0]
]

'''amplitudes which  have secular terms; in 1/NUT_SCALE arc seconds
{index, constant dPSI, T/10 in dPSI, constant in dEPS, T/10 in dEPS}'''
ampsecul = [
    [0  ,-171996 ,-1742 ,92025 ,89],
    [1  ,2062    ,2     ,-895  ,5],
    [8  ,-13187  ,-16   ,5736  ,-31],
    [9  ,1426    ,-34   ,54    ,-1],
    [10 ,-517    ,12    ,224   ,-6],
    [11 ,217     ,-5    ,-95   ,3],
    [12 ,129     ,1     ,-70   ,0],
    [15 ,17      ,-1    ,0     ,0],
    [17 ,-16     ,1     ,7     ,0],
    [30 ,-2274   ,-2    ,977   ,-5],
    [31 ,712     ,1     ,-7    ,0],
    [32 ,-386    ,-4    ,200   ,0],
    [33 ,-301    ,0     ,129   ,-1],
    [37 ,63      ,1     ,-33   ,0],
    [38 ,-58     ,-1    ,32    ,0],
    # termination
    [ -1, ]
];


'''amplitudes which only have constant terms; same unit as above
{dPSI, dEPS}
indexes which are already in ampsecul[][] are zeroed'''
ampconst = [
    [0,0],
    [0,0],
    [46,-24],
    [11,0],
    [-3,1],
    [-3,0],
    [-2,1],
    [1,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [48,1],
    [-22,0],
    [0,0],
    [-15,9],
    [0,0],
    [-12,6],
    [-6,3],
    [-5,3],
    [4,-2],
    [4,-2],
    [-4,0],
    [1,0],
    [1,0],
    [-1,0],
    [1,0],
    [1,0],
    [-1,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [-158,-1],
    [123,-53],
    [63,-2],
    [0,0],
    [0,0],
    [-59,26],
    [-51,27],
    [-38,16],
    [29,-1],
    [29,-12],
    [-31,13],
    [26,-1],
    [21,-10],
    [16,-8],
    [-13,7],
    [-10,5],
    [-7,0],
    [7,-3],
    [-7,3],
    [-8,3],
    [6,0],
    [6,-3],
    [-6,3],
    [-7,3],
    [6,-3],
    [-5,3],
    [5,0],
    [-5,3],
    [-4,0],
    [4,0],
    [-4,0],
    [-3,0],
    [3,0],
    [-3,1],
    [-3,1],
    [-2,1],
    [-3,1],
    [-3,1],
    [2,-1],
    [-2,1],
    [2,-1],
    [-2,1],
    [2,0],
    [2,-1],
    [1,-1],
    [-1,0],
    [1,-1],
    [-2,1],
    [-1,0],
    [1,-1],
    [-1,1],
    [-1,1],
    [1,0],
    [1,0],
    [1,-1],
    [-1,0],
    [-1,0],
    [1,0],
    [1,0],
    [-1,0],
    [1,0],
    [1,0],
    [-1,0],
    [-1,0],
    [-1,0],
    [-1,0],
    [-1,0],
    [-1,0],
    [-1,0],
    [1,0],
    [-1,0],
    [1,0]
];


def nutation(mj):
    # static double lastmj = -10000, lastdeps, lastdpsi;
    # double T, T2, T3, T10;			/* jul cent since J2000 */
    # double prec;				/* series precis in arc sec */
    # int i, isecul;				/* index in term table */

    delcache = []
    for i in range(5):
        delcache.append([None] * (2 * NUT_MAXMUL + 1))
    
    lastmj = None

    if mj == lastmj:
        deps = lastdeps
        dpsi = lastdpsi
        return (deps, dpsi)

    prec = 0.0

    # augment for abundance of small terms
    prec *= NUT_SCALE / 10

    T = (mj - ephem.J2000) / 36525.
    T2 = T * T
    T3 = T2 * T
    T10 = T/10.

    # calculate delaunay args and place in cache
    for i in range(5):
        x = (delaunay[i][0] +
             delaunay[i][1] * T +
             delaunay[i][2] * T2 +
             delaunay[i][3] * T3)

        # convert to radians
        x /= SECPERCIRC
        x -= floor(x)
        x *= 2. * pi

        # fill cache table
        for j in range(2 * NUT_MAXMUL + 1):
            delcache[i][j] = (j - NUT_MAXMUL) * x

    
    # find dpsi and deps
    lastdpsi = lastdeps = 0.

    isecul = 0
    for i in range(NUT_SERIES):
        # double arg = 0., ampsin, ampcos;
        arg = 0.

        if (ampconst[i][0] or ampconst[i][1]):
            # take non-secular terms from simple array
            ampsin = ampconst[i][0]
            ampcos = ampconst[i][1]
        else:
            # secular terms from different array
            ampsin = float(ampsecul[isecul][1]) + float(ampsecul[isecul][2]) * T10
            ampcos = float(ampsecul[isecul][3]) + float(ampsecul[isecul][4]) * T10
            isecul += 1

        for j in range(5):
            arg += delcache[j][NUT_MAXMUL + multarg[i][j]]

        if fabs(ampsin) >= prec:
            lastdpsi += ampsin * sin(arg)

        if fabs(ampcos) >= prec:
            lastdeps += ampcos * cos(arg)

    
    # convert to radians.
    lastdpsi = degrad(lastdpsi/3600./NUT_SCALE)
    lastdeps = degrad(lastdeps/3600./NUT_SCALE)

    lastmj = mj
    return (lastdeps, lastdpsi)
