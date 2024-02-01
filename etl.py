import config

from birdie.db.util import get_engine
from birdie.db.sql_client import SQLClient
from birdie.etl.bat.handler import VantageHandler
from birdie.etl.bat.client import AlphaVantageClient


if __name__ == '__main__':

    # BaT Client
    # Add BaT job here. stocks_engine = get_engine('stocks')
    # Add BaT job here. vantage_handler = VantageHandler(
    # Add BaT job here.     sql_client=SQLClient(engine=stocks_engine),
    # Add BaT job here.     data_client=AlphaVantageClient(
    # Add BaT job here.         key=config.alpha_vantage_key
    # Add BaT job here.     ),
    # Add BaT job here.     symbols=config.symbols,
    # Add BaT job here.     sleep_seconds=config.sleep_seconds,
    # Add BaT job here. )
    # Add BaT job here. vantage_handler.run()


