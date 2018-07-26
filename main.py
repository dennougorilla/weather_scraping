# coding: utf-8
import pandas as pd
import pandas_redshift as pr
from datetime import datetime, date, timedelta
import os

import weather_scraping
import rsconnecter

if __name__ == "__main__":
    sdt = datetime(2016,3,1,1)
    edt = datetime(2018,7,21,1)
    while edt != sdt:
       df = weather_scraping.hourly(sdt)
       rsconnecter.dbconnect()
       sdt = sdt+timedelta(days=1)
