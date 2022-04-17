# 计算中国的工作日
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
from datetime import datetime

start_day = '20220401'  # 都改成yyyy-mm-dd格式也可以。
end_day = '20220509'
public_holidays = pd.DatetimeIndex(['20220404', '20220405', '20220502', '20220503', '20220504',
                                    ])  # 如果不加DatetimeIndex 则20220404这种格式不认，2022-04-04认。
extra_work_day = ['20220424', '20220507']


def workday(start_day, end_day):
    cbd = CustomBusinessDay(holidays=public_holidays)
    bus_day = pd.date_range(start=start_day, end=end_day, freq=cbd)

    diextra_work_day = pd.DatetimeIndex(extra_work_day)
    bus_day2 = pd.DatetimeIndex( sorted( bus_day.append(diextra_work_day) ) )
    print(bus_day2)
    print( 'Work Days:', [ datetime.strftime(x, '%F') for x in bus_day2 ], end='\n\n')
    print( f'Count of Work days: {len(bus_day2)} days.' )


if __name__ == '__main__':
    workday(start_day, end_day)
