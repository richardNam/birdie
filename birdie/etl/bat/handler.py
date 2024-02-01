import time

from .transform import process_response


class VantageHandler:
    def __init__(self, sql_client, data_client, symbols, sleep_seconds):
        """ Gets data from the Alpha Vantage API and
        stores the results in a database table.

        Args:
            sql_client (db.sql_client):
            data_client (vantage.AlphaVantageClient):
            symbols (List[str]): A list of stock ticker symbols
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

