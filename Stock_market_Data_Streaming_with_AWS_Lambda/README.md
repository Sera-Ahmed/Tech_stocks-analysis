# Data Streaming with AWS Lambda

In this project, I am interested in processing stock market data in real time or near real time capacity. For this project I will be using the <https://pypi.org/project/yfinance/ "yfinance"> module to get the stock market data. The period of data I am interested in is one full trading day stock name, high, low and date for May 11th 2021 at a 5 minute interval. 

Below are the stocks I am most interested in:
* Facebook (FB)
* Shopify (SHOP)
* Beyond Meat (BYND)
* Netflix (NFLX)
* Pinterest (PINS)
* Square (SQ)
* The Trade Desk (TTD)
* Okta (OKTA)
* Snap (SNAP)
* Datadog (DDOG)


# <u>Steps taken:</u>

# Data Transformer
* Create an AWS Lambda function - This function will help collect the stock data using the yfinance module and tranform it in JSON format and the data will be pushed to the Kinesis data stream. We could use a trigger as well to run the lambda function automatically when needed. 

# Data Collector
* Kinesis - The Kinesis data stream will help hold the data and then pass it to the firehose which will then save the data in the specific s3 bucket it is linked to.

* S3 bucket - This is where the stock market data will be stored.

# Data Analyzer
* AWS Glue and Athena - We will then use Glue to crawl the s3 file where the data is stored and this will help create the tables for the database. Athena will be used to query the data for analysis purpose. 


* Data Visualization - To check the max high per hour for each stock I ran a query and stored the results in results.csv. This results.csv file was then used for visualization purposes. Seaborn and Matplotlib were used to create charts and the code and visuals are stored in Analysis.ipynb (it has a pdf version as well).



![kinesis_config](/Users/sera/Desktop/Baruch Books/CIS 9760 Big Data/Projects/project03/assets/kinesis_config.png)



