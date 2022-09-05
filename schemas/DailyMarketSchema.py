import pandera as pa

from datetime import datetime
from pandera.typing import Series
from pandera.dtypes import Timestamp


class DailyMarketSchema(pa.SchemaModel):
	dates: Series[Timestamp] = pa.Field(
		lt=datetime.today(),
		coerce=True,
		nullable=False
	)
	asset_name: Series[str] = pa.Field(
		coerce=True,
		nullable=False
	)
	prices: Series[float] = pa.Field(
		ge=0, 
		coerce=True,
		nullable=True
	)
	total_volumes: Series[float] = pa.Field(
		ge=0, 
		coerce=True,
		nullable=True
	)
	market_caps: Series[float] = pa.Field(
		ge=0, 
		coerce=True,
		nullable=True
	)