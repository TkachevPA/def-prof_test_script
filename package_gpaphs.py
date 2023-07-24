import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

from parser import new_data as data
from main import first_sign, second_sign, result

res = [i.split(' ')[0] for i in result]
print(res)

matplotlib.use('WebAgg')

for art in res:
    deficit = pd.Series(data[art]['deficit'],
                        list(data[art]['remains'].index))
    proficit = pd.Series(data[art]['proficit'],
                         list(data[art]['remains'].index))
    zero = pd.Series(data[art]['zero'],
                     list(data[art]['remains'].index))

    fig = plt.figure(figsize=(13, 7))
    plt.title(
        f'{art} признаки в базе {data[art]["source_first_sign"]}{data[art]["source_second_sign"]}\n'
        # f'Расчетные признаки {first_sign}{second_sign} '
    )
    plt.plot(data[art]['remains'], color='blue', marker='.', label='Остатки')
    plt.plot(deficit, color='red', marker='.', label='Дефицит')
    plt.plot(proficit, color='green', marker='.', label='Профицит')
    plt.plot(zero, color='black', marker='.', label='Обнуление')

    plt.grid()
    plt.legend()
    plt.savefig(f'output/{art}')
