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
        for key in self.keys:
            try:
                raw_data = self.data_client.get_vin_response(
                    key=key,
                )
                df = process_response(
                    data=raw_data,
                    key=key,
                )
                self.sql_client.update_table(
                    df=df,
                    table_name='bat_data',
                    update_on=['vin'],
                )
            except ValueError:
                print(f'Incorrect symbol: {key}')

            time.sleep(self.sleep_seconds)

