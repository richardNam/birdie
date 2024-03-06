#Example url: https://bringatrailer.com/listing/2003-toyota-land-cruiser-42/
import time

from .transform import process_response


class BringATrailerHandler:
    def __init__(self, sql_client, data_client, keys, sleep_seconds):
        """ Handler for Bring A Trailer.

        Args:
            sql_client (db.sql_client):
            data_client (BringATrailerClient):
            keys (List[str]): A list of stock ticker symbols
            sleep_seconds (int): The number of seconds to
                wait between calls.


        """
        self.sql_client = sql_client
        self.data_client = data_client
        self.symbols = symbols
        self.sleep_seconds = sleep_seconds


    def run(self):
        for symbol in self.symbols:
            try:
                data, meta_data = self.data_client.get_timeseries_data(
                    symbol=symbol
                )
                df = process_response(
                    data=data,
                    meta_data=meta_data,
                    symbol=symbol
                )
                self.sql_client.update_table(
                    df=df,
                    table_name='vantage_data',
                    update_on=['observation_ts', 'symbol'],
                )
            except ValueError:
                print('Incorrect symbol: %r' % symbol)

            time.sleep(self.sleep_seconds)

