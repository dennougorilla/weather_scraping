import pandas as pd
from datetime import datetime, date, timedelta

def hourly(dt):
    url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=36&block_no=47570&year=' + str(dt.year) + '&month=' + str(dt.month) + '&day=' + str(dt.day) + '&view=p1'
    df = pd.read_html(url, skiprows=2)[0]
    #df = df.replace('--', '-1')
    df.loc[:, 0] = pd.date_range(dt, periods=24, freq='H')
    df.columns = ['time', 'atmospheric_pressure_local', 'atmospheric_pressure_sea', 'precipitation', 'temperature', 'dew_point_temperature', 'vapor_pressure', 'humidity', 'wind_speed', 'wind_direction', 'daylight_hours', 'overall_solar_radiation', 'snowfall', 'fallen_snow', 'weather', 'cloudcover', 'visibility']
    return df

def daily():
    url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=36&block_no=47570&year=' + str(dt.year) + '&month=' + str(dt.month) + '&day=' + str(dt.day) + '&view=p1'
    df = pd.read_html(url, skiprows=4)[0]
    df.columns = ['日', '気圧(hPa)現地平均', '気圧(hPa)海面平均', '降水量(mm)合計', '降水量(mm)最大一時間', '降水量(mm)最大１０分間', '気温(℃)平均', '気温(℃)最高', '気温(℃)最低', '湿度(%)平均', '湿度(%)最小', '平均風速(m/s)', '最大風速風速(m/s)', '最大風速風向', '最大瞬間風速風速(m/s)', '最大瞬間風速風向', '日照時間(h)', '雪降雪合計(cm)', '雪最深積雪値(cm)']
    #df = df.replace('--', '-1')
    return df
