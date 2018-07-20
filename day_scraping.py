import pandas as pd
from datetime import datetime, date, timedelta
dt = datetime(2016,3,1,1)
while dt.year != 2017:
        url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=36&block_no=47570&year=' + str(dt.year) + '&month=' + str(dt.month) + '&day=' + str(dt.day) + '&view=p1'
        df = pd.read_html(url, 
                skiprows=4)[0]

        print(dt.year)
        print(dt.month)
        #df = df.replace('--', '-1')
        print(df)
        df.to_csv(path_or_buf = "./Past_weather_data2/" + str(dt.year) + '_' + str(dt.month) + '_' + str(dt.day) + ".csv", index = False)
        dt = dt+timedelta(days=1)
