import config

from client import AlphaVantageClient
from transform import process_response



class Handler:
    def __init__(self, data_client, symbols):
        self.data_client = data_client
        self.symbols = symbols


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
                print(df)
            except ValueError:
                print('Incorrect symbol: %r' % symbol)


if __name__ == '__main__':
    Handler(
        data_client=AlphaVantageClient(
            key=config.alpha_vantage_key
        ),
        symbols=config.symbols,
    ).run()


