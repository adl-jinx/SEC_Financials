import requests
import pandas as pd

# create request header
##  SEC uses no key or codes, but rather the email.

headers = {'User-Agent': "ichessur@gmail.com"}

# Companies data

companyTicker = requests.get(
    "https://www.sec.gov/files/company_tickers.json", 
    headers=headers
    )


#print(companyTicker.json().keys())

firstEntry = companyTicker.json()['0']
directCik = companyTicker.json()['0']['cik_str']

# getting company dataframe

companyData = pd.DataFrame.from_dict(companyTicker.json(),
                                     orient='index')

# the Cik code is actually 10 digits meaning is necessary to add the remaing 0 digit (check SEC documentation)
# https://www.sec.gov/edgar/sec-api-documentation  --> https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)

cik = companyData[0:1].cik_str[0]

# at this point the file is finished because we setted up the API

# Requesting financial data

filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json', 
    headers=headers)

# review json

print(filingMetadata.json().keys())
filingMetadata.json()['filings']
filingMetadata.json()['filings'].keys()

# dictionary to dataframe 

allforms = pd.DataFrame.from_dict(filingMetadata.json()['filings']['recent'])

#saving the data


