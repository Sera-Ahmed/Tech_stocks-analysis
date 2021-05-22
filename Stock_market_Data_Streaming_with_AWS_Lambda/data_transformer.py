
import json
import yfinance as yf
import boto3
import datetime


#kinesis = boto3.client('kinesis', "us-east-2")


def lambda_handler(event,context):
    kinesis = boto3.client('kinesis', "us-east-2")
    #record_dump={}
    start_date = '2021-05-11'
    end_date = '2021-05-12'
    interval = '5m'
    stocks = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    
    for stock in stocks:
        stream = yf.Ticker(stock).history(start=start_date,end=end_date,interval=interval)
        
        for index, value in stream.iterrows():
            record_dump = json.dumps({'high':value['High'],'low':value['Low'],'ts':str(index),'name':stock},separators=(',',': '))+"\n"
            print(record_dump)
            kinesis.put_record(
                StreamName="sta9760s2021_stream1",
                Data=record_dump.encode('utf-8'),
                PartitionKey="partitionkey")
                
    
    return{
        'statusCode': 200,
        'body': record_dump
    }

