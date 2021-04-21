import calendar
import pandas as pd
import pytz

from dateutil.parser import parse


def extract_refresh_ts(
        data_dict,
        refresh_key='3. Last Refreshed',
        tz_key='6. Time Zone',
    ):
    """ takes in the meta data response and returns
    the last refreshed timestamp.

    Args:
        data_dict (dict):

    Returns: tuple(int, str)

    """
    date_string = data_dict.get(refresh_key)
    timezone = data_dict.get(tz_key)

    ts = None
    if (date_string is not None) and (timezone is not None):
        dt = parse(date_string)
        ts = localize_timestamp(
            dt=dt,
            timezone=timezone
        )

    return ts, timezone


def localize_timestamp(dt, timezone):
    """ Localizes the datetime to timestamp

    Args:
        dt (datetime.datetime):
        timezone (str):

    Returns: int

    """
    tz = pytz.timezone(timezone)
    local_dt = tz.localize(dt)
    return calendar.timegm(local_dt.utctimetuple())


def transform_observations(data):
    """ takes in a dictionary of obserations and transforms
    them into the correct types:

    Args:
        data (Dict[str: str]):

    Returns: Dict[str: float]

    """
    output_data = {}
    for col, value in data.items():
        parsed_col = parse_data_column(col)
        dollars = float(value)
        output_data[parsed_col] = dollars

    return output_data


def parse_data_column(x):
    """ parses the keys of the data object.
    ex. '2. high'.

    Args:
        x (str):

    Returns str

    """
    return x.split('.')[-1].strip()


def flatten_observations(observations, tz):
    """ flattens the observations into a single "row".

    Args:
        observations (Dict[str: str]):

    Returns: pd.DataFrame

    """
    total = []
    for obs_date, obs_data in observations.items():
        obs_dt = parse(obs_date)
        obs_ts = localize_timestamp(obs_dt, tz)
        _data = transform_observations(obs_data)
        _data['observation_ts'] = obs_ts
        total.append(_data)

    return pd.DataFrame(total)

def process_response(data, meta_data):
    last_refreshed_ts, timezone = extract_refresh_ts(
        meta_data
    )
    df = flatten_observations(data, tz=timezone)
    df['last_refreshed_ts'] = last_refreshed_ts
    df['timezone'] = timezone

    return df



