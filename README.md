# vinter_test

## Proposal

A Client interface will allow for easy extraction and validation of market
data while providing us with a systematic data structure for all API,
making cross validation data checking easier for basic information, defined
to be, for each digital assets within a given set:
- Daily prices
- Daily total volumes
- Daily market capitalizations

Each Client can implement its own data extraction procedure as well.


## Tests

Run the following command at the repo source to test the package:

```bash
pip install -r requirements.txt
python -m unittest discover tests
```


## Env variables
There are 3 environement variables defined within this project, that should be
set for the CircleCI project running the pipeline.
Those env variables are API keys used for CoinMarketCap, Nomics and CoinAPI.


## TODO.md

- [ ] PoC
    - [X] Read about given website and their APIs
    - [X] Find more about stakeable digital asset
    - [X] Implement unittest / CircleCI framework
    - [ ] Data Extraction
        - [ ] CoinGecko
            - [X] API Connection Test
            - [X] Connector
            - [X] daily_market_data
            - [ ] Fully tested
        - [ ] Other API
            - [ ] API Connection Test
            - [ ] Connector
            - [ ] daily_market_data
            - [ ] Fully tested
    - [ ] Data Validation Reporting
        - [ ] Create visuals for data integrity
            - [ ] Distribution for each dimensions/metrics
            - [ ] Total NA values

- [ ] V1
    - [ ] Data Infrastructure
        - [ ] ClickHouse Docker instance for errors, raw data
        - [ ] Data warehousing
    - [ ] Implement Failsafes
        - [ ] Save all raw extracted data in raw_data_table
        - [ ] Save all requests/pipeline errors in error_table
        - [ ] Save operations logs for easier debugging
        - [ ] Email alert for errors
    - [ ] Data Extraction
        - [ ] CoinMarketCap
            - [X] API Connection Test
            - [ ] Connector
            - [ ] Airflow Daily extraction (frequency depending on API rights)
    - [ ] Data Validation
        - [ ] Value range checking following expert's recommendation