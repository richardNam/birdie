import pandas as pd

from . import db_config


TABLE_NAME_Q = '''
SELECT TABLE_NAME AS table_names
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='{db}'
'''


class SQLClient:
    def __init__(self, engine):
        self.engine = engine


    def _get_table_names(self):
        tables_df = pd.read_sql_query(
            TABLE_NAME_Q.format(db=db_config.db_name),
            con=self.engine
        )
        return tables_df.table_names.tolist()


    def replace_table(self, df, table_name):
        """ Replaces table with provided dataframe

        Args:
            df (pandas.DataFrame):
            table_name (str): table name

        """
        table_names = self._get_table_names()
        if table_name not in table_names:
            raise Exception('Table name does not exist in database.')

        df.to_sql(
            table_name,
            con=self.engine,
            if_exists='replace'
        )


