import pandas as pd
import datetime
import sqlalchemy
import pymssql
from pandas.io.sql import SQLTable

def _execute_insert(self, conn, keys, data_iter):
    try:
        data = [dict((k, v) for k, v in zip(keys, row)) for row in data_iter]
        conn.execute(self.insert_statement().values(data))
    except Exception as error:
        print(error)

SQLTable._execute_insert = _execute_insert

def s3ToSQL(engine):
    s3_link = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/index.csv'
    df = pd.read_csv(s3_link, skiprows=5, dtype={'EndingRange': 'str'}, converters={'Availability':p2f, 'Durability': p2f}, keep_default_na=False, na_values='')
    print('AWS Storage Read In -',len(df.index),'records at',datetime.datetime.now())

    with engine.begin() as conn:
        startTime = datetime.datetime.now()
        try:
            df.to_sql('AmazonS3', conn, if_exists='append', chunksize=1000, index=False)
        except Exception as error:
            print(error)
            return False
        endTime = datetime.datetime.now()
        print('Time Taken for AWS Storage - ',(endTime - startTime).total_seconds())
        return True
    
    
    # print('Table Read In',datetime.datetime.now())

def ec2ToSQL(engine):
    ec2_link = 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.csv'
    df = pd.read_csv(ec2_link, skiprows=5, dtype={'EndingRange': 'str', 'Pre Installed S/W': 'str'}, keep_default_na=False,  na_values='')
    df.to_csv("test.csv")
    print('AWS Compute Read In -',len(df.index),'records at',datetime.datetime.now())
    with engine.begin() as conn:
        startTime = datetime.datetime.now()
        try:
            df.to_sql('AmazonEC2', conn, if_exists='append', chunksize=1000, index=False)
        except Exception as error:
            print(error)
            return False
        endTime = datetime.datetime.now()
        print('Time Taken for AWS Compute - ',(endTime - startTime).total_seconds())
        return True
    

def AWSVendorUpdate(engine):  
    with engine.begin() as conn:
        startTime = datetime.datetime.now()
        try:
            conn.execute('UPDATE [dbo].[Vendor] SET [UpdatedDate] = \''+datetime.datetime.now().strftime("%Y-%m-%d")+'\' where [dbo].[Vendor].[Name] = \'AWS\' ')
        except Exception as error:
            print(error)
            return False
        endTime = datetime.datetime.now()
        print('Time Taken for AWS Vendor Update - ',(endTime - startTime).total_seconds())
        return True

def p2f(x):
    if "%" in x:
        return float(x.strip('%'))/100
    else:
        return


