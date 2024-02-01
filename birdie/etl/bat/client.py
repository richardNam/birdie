from alpha_vantage.timeseries import TimeSeries


class BringATrailerClient:
    def __init__(self, key):
        self.key = key

    def get_timeseries_data(self, symbol):
        ts = TimeSeries(key=self.key)
        data, meta_data = ts.get_intraday(
            symbol,
        )
        return data, meta_data
