import config

from birdie.db.util import get_engine
from birdie.db.sql_client import SQLClient
from birdie.etl.vantage.handler import VantageHandler
from birdie.etl.vantage.client import AlphaVantageClient


if __name__ == '__main__':
    # Alpha Vantage Client
    stocks_engine = get_engine('stocks')
    vantage_handler = VantageHandler(
        sql_client=SQLClient(engine=stocks_engine),
        data_client=AlphaVantageClient(
            key=config.alpha_vantage_key
        ),
        symbols=config.symbols,
    )
    vantage_handler.run()





