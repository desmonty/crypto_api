from clients.CoinGeckoClient import CoinGeckoClient
from schemas.DailyMarketSchema import DailyMarketSchema

SUBSET_ID = "test"


if __name__ == "__main__":
    # Create Client
    client_usd = CoinGeckoClient(SUBSET_ID, "usd")

    # Get market data
    df_market = client_usd.daily_market_data(30)
    
    # Validate DataFrame    
    DailyMarketSchema(df_market)

    # Generate Data Quality report