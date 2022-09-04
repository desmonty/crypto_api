TODO.md
=======

- [X] Read about given website and their APIs
- [X] Find more about stakeable digital asset
- [X] Implement unittest / CircleCI framework
- [ ] Data Extraction
	- [ ] CoinGecko
		- [X] API Connection Test
		- [ ] Connector
		- [ ] daily_market_data
	- [ ] CoinMarketCap
		- [X] API Connection Test
		- [ ] ClickHouse Docker instance to gather information
		- [ ] Connector
		- [ ] Airflow Daily extraction (frequency depending on API rights)
	- [ ] Failsafes
		- [ ] Save all raw extracted data in raw_data_table
		- [ ] Save all requests/pipeline errors in error_table
		- [ ] Save operations logs for easier debugging
- [ ] Data Validation
	- [ ] Check for NA values
	- [ ] Cross validation using data from several sources
- [ ] Reporting
	- [ ] Create visuals for data integrity
		- [ ] Distribution for each dimensions/metrics
		- [ ] Total NA values
	- [ ] Email alert when error after retry strategy  