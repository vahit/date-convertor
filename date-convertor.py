#!/usr/sbin/env python

# filename: data-convertor.py
# description: Simple date convertor by using calverter python module.
# version: 1.0
# feedback: Vahid.Maani@gmail.com

# import needed mopdules:
# standard modules:
import time
import sys

# third party modules:
from calverter import Calverter

# convert Jalalian date to Gregorian
def hijri_date(zero_date):
    cal = Calverter()
    iso_day = cal.jalali_to_jd(
        int(zero_date[0]),
        int(zero_date[1]),
        int(zero_date[2])
    )
    end_date = cal.jd_to_gregorian(iso_day)
    end_date = list(end_date)
    week_day_num = cal.jwday(iso_day)
    end_date.append(week_day_num)
    print(end_date[0], end_date[1], end_date[2], end_date[3])

# convert Gregorian date to Jalalian
def gregorian_date(zero_date):
    cal = Calverter()
    iso_day = cal.gregorian_to_jd(
        int(zero_date[0]),
        int(zero_date[1]),
        int(zero_date[2])
    )
    end_date = cal.jd_to_jalali(iso_day)
    end_date = list(end_date)
    week_day_num = cal.jwday(iso_day)
    end_date.append(week_day_num)
    print(end_date[0], end_date[1], end_date[2], end_date[3])

# main function
def main():
    zero_date = sys.argv[2]
    try:
        zero_date = zero_date.split(sep='/')
        for each_item in zero_date:
            if not(each_item.isdigit()):
                raise TypeError
        if zero_date.__len__() != 3:
            raise TypeError
    except TypeError:
        print("Enter date in yy/mm/dd format.")
        return()

    if sys.argv[1] == "h":
        hijri_date(zero_date)
    elif sys.argv[1] == "g":
        gregorian_date(zero_date)
    else:
        return('Error!')

if __name__ == "__main__":
    main()
else:
    print('Error!')
