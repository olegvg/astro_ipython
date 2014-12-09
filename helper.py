# -*- coding: utf-8 -*-

__author__ = 'ogaidukov'

from datetime import timedelta, datetime
import pytz
import matplotlib.dates as mdates

dt_epoc = datetime.fromtimestamp(0, pytz.utc)


def timedelta_formatter(x, pos):
    td = timedelta(microseconds=x/1000.0)
    return str(td)


def timedelta_as_dt_formatter(x, pos):
    dt = mdates.num2date(x)
    if dt < dt_epoc:
        inv_dt = timedelta(0) - (dt - dt_epoc)
        return "-" + str(inv_dt)
    return str(dt.time())