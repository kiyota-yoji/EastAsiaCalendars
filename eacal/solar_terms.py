# -*- coding: utf-8 -*-

import ephem
import nutation
from math import pi

ABERR_CONST = (20.49552 / 3600. / 180. * pi)

_sun = ephem.Sun()                    # used for computing equinoxes


def get_ap_hlon(mj, nutation_dpsi=None):
    _sun.compute(mj)
    if nutation_dpsi is None: nutation_dpsi = nutation.nutation(mj)[1]
    ap_hlon = _sun.hlon + nutation_dpsi - ABERR_CONST + pi
    if ap_hlon < 0.0:
        ap_hlon += 2 * pi
    elif ap_hlon > 2 * pi:
        ap_hlon > 2 * pi
        ap_hlon -= 2 * pi
    return ephem.degrees(ap_hlon)


