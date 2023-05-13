import requests
import pandas as pd

# Requesting financial data

filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json', 
    headers=headers)

# review json

print(filingMetadata.json().keys())
filingMetadata.json()['filings']
filingMetadata.json()['filings'].keys()

