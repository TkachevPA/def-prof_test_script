import pandas as pd
import datetime

data = pd.DataFrame()
data = pd.read_pickle('data')
data = data.set_index('катал. номер') # установка артикулов индексами

arts = list(set(data.index)) # создание списка артикулов

completed_data = {}

for art in arts: # Парсинг таблицы
    if data.loc[art, 'Дата старости'][0] == 0:
        old_date = ''
    else:
        old_date = datetime.date(
            int(data.loc[art, 'Дата старости'][0][6:10]),
            int(data.loc[art, 'Дата старости'][0][3:5]),
            int(data.loc[art, 'Дата старости'][0][0:2])
        )
    completed_data[art] = {
        'remains': pd.Series(list(data.loc[art, 'Остаток на дату'][1:]),
                             list(data.loc[art, 'Дата'][1:])),
        'old_date': old_date,
        'have_sales': True if data.loc[art, 'Были продажи'][0] == 'Да'
        else False,
        'have_pred': True if data.loc[art, 'План 12 утв'][0] else False,
        'zero': data.loc[art, 'Уровень обнуления'][0],
        'deficit': data.loc[art, 'Уровень дефицита в штуках'][0],
        'proficit': data.loc[art, 'Уровень профицита в штуках'][0],
        'source_zero': True if
        data.loc[art, 'Остаток пересекает уровень обнуления сверху вниз'][
            0] == 'Да' else False,
        'source_def': True if
        data.loc[art, 'Остаток пересекает уровень дефицита сверху вниз'][
            0] == 'Да' else False,
        'source_prof': True if
        data.loc[art, 'Остаток пересекает уровень профицита снизу вверх'][
            0] == 'Да' else False,
        'source_first_sign': data.loc[art, 'Признак текущего остатка'][0],
        'source_second_sign': data.loc[art, 'Признак будущего остатка'][0] if
        data.loc[art, 'Признак будущего остатка'][0] != 0 else '',
        'source_mean': data.loc[art, 'Средний остаток в процентах'][0],

    }
