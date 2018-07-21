# coding: utf-8
#import {{{
import pandas as pd
import pandas_redshift as pr
from datetime import datetime, date, timedelta
#}}}

#def every_hour_scraping {{{
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
            sdt = sdt+timedelta(days=1)
    return df
#}}}

#main {{{
if __name__ == "__main__":
    sdt = datetime(2016,3,1,1)
    edt = datetime(2018,7,21,1)
    
    df = every_hour_scraping(sdt, edt)
    
    dbname = os.getenv('REDSHIFT_DB')
    host = os.getenv('REDSHIFT_HOST')
    port = os.getenv('REDSHIFT_PORT')
    user = os.getenv('REDSHIFT_USER')
    password = os.getenv('REDSHIFT_PASS')
    
    pr.connect_to_redshift(dbname = dbname,
                            host = host,
                            port = port,
                            user = user,
                            password = password)
    
    pr.connect_to_s3(aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'),
                    bucket = ''
                    ) 
    pr.pandas_to_redshift(data_frame = df,
                            redshift_table_name = '',
                            append = True)
    #}}}
