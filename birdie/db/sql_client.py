import pandas as pd

from . import db_config


class SQLClient:
    def __init__(self, engine):
        self.engine = engine


    def _get_table_names(self):
        tables_df = pd.read_sql_query(
            'show tables',
            con=self.engine
        )
        return tables_df.Tables_in_stocks.tolist()


    def replace_table(self, df, table_name):
        """ Replaces table with provided dataframe

        Args:
            df (pandas.DataFrame):
            table_name (str): table name

        """
        table_names = self._get_table_names()
        if table_name not in table_names:
            raise Exception('Table {} does not exist in database.'.format(
                table_name))

        df.to_sql(
            table_name,
            con=self.engine,
            if_exists='replace'
        )


