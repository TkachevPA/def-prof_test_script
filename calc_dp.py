import datetime
import pandas as pd


def calc_first_sign(remains, zero, deficit, proficit, old_date, have_sales,
                    have_pred):
    if old_date:
        if old_date > datetime.date(2023, 7, 20):
            return 'N'
    if not have_pred:
        return 'Z'
    if not have_sales:
        return 'G'
    elif remains[0] <= zero:
        sign = 'O'
    elif remains[0] < deficit:
        sign = 'D'
    elif remains[0] > proficit:
        sign = 'P'
    else:
        sign = 'A'
    return sign


def calc_second_sign(remains, zero, deficit, proficit) -> str:
    result = []

    for i in range(len(remains) - 1):
        if remains[i + 1] <= zero < remains[i]:
            result.append('O')
        elif remains[i + 1] <= deficit < remains[i]:
            result.append('D')
        elif remains[i + 1] >= proficit > remains[i]:
            result.append('P')

    if max(remains) <= zero or 'O' in result:
        return 'O'

    elif max(remains) <= deficit or 'D' in result:
        return 'D'

    elif min(remains) >= proficit or 'P' in result:
        return 'P'

    else:
        return 'A'

# MEAN_REMAIN = (mean(REMAINS) - DEF[0]) / (PROF[0] - DEF[0])
# MEAN_REMAIN_STR = f'{round(MEAN_REMAIN * 100, 0)}%'
