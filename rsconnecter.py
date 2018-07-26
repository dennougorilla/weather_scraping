def dbconnect(df):
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
    
    pr.connect_to_s3(aws_access_key_id = os.getenv('ACCESS_KEY_ID'),
                    aws_secret_access_key = os.getenv('SECRET_ACCESS_KEY'),
                    bucket = 'TODO'
                    ) 
    pr.pandas_to_redshift(data_frame = df,
                            redshift_table_name = 'weather_data',
                            append = True)
