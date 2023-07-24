from parser import new_data as data
from calc_dp import calc_second_sign, calc_first_sign


result = []

for art in data:
    first_sign = calc_first_sign(data[art]['remains'], data[art]['zero'],
                                 data[art]['deficit'], data[art]['proficit'],
                                 data[art]['old_date'],
                                 data[art]['have_sales'],
                                 data[art]['have_pred'])
    if first_sign in ['Z', 'G', 'N']:
        second_sign = ''
    else:
        second_sign = calc_second_sign(data[art]['remains'], data[art]['zero'],
                                       data[art]['deficit'],
                                       data[art]['proficit'])

    if first_sign != data[art]['source_first_sign']:
        result.append(
            f'{art} В базе {data[art]["source_first_sign"]}{data[art]["source_second_sign"]}, расчет {first_sign}{second_sign}\n')
    if second_sign != data[art]['source_second_sign']:
        result.append(
            f'{art} В базе {data[art]["source_first_sign"]}{data[art]["source_second_sign"]}, расчет {first_sign}{second_sign}\n')

print(*result)
