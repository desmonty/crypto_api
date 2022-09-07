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

## Dashboard

Run the following command at the repo source to deploy a dashboard that can be
viewed at http://127.0.0.1:8888/

```bash
python dashboards/daily_market/app.py
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
    - [X] Data Extraction
        - [X] CoinGecko
            - [X] API Connection Test
            - [X] Connector
            - [X] daily_market_data
            - [X] Fully tested
    - [X] Data Validation
        - [X] Create visuals for data integrity
            - [X] plot for each metrics
            - [X] Total NA values
        - [ ] `DailyMarketSchema.py`: Check if dates are no later than `days` ago
    - [ ] Add Code Coverage metrics in Git

- [ ] V1
    - [ ] Data Infrastructure
        - [ ] ClickHouse Docker instance for errors, raw data and data warehouse
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
        - [ ] Unittest for dashboard
