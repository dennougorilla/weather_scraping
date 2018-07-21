import pandas as pd
from datetime import datetime, date, timedelta
def every_hour_scraping(sdt, edt):
    while edt != sdt:
            url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=36&block_no=47570&year=' + str(sdt.year) + '&month=' + str(sdt.month) + '&day=' + str(sdt.day) + '&view=p1'
            df = pd.read_html(url, 
                    skiprows=2)[0]
    
            print(sdt)
            #df = df.replace('--', '-1')
            df.loc[:, 0] = pd.date_range(sdt, periods=24, freq='H')
            df.columns = ['time', 'atmospheric_pressure_local', 'atmospheric_pressure_sea', 'precipitation', 'temperature', 'dew_point_temperature', 'vapor_pressure', 'humidity', 'wind_speed', 'wind_direction', 'daylight_hours', 'overall_solar_radiation', 'snowfall', 'fallen_snow', 'weather', 'cloudcover', 'visibility']
            print(df)
            #df.to_csv(path_or_buf = "./Past_weather_data2/" + str(sdt.year) + '_' + str(sdt.month) + '_' + str(sdt.day) + ".csv", index = False)
            sdt = sdt+timedelta(days=1)

sdt = datetime(2016,3,1,1)
edt = datetime(2018,7,21,1)
