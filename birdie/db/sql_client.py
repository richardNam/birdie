import pandas as pd

from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from . import db_config


class SQLClient:
    def __init__(self, engine):
        self.engine = engine
        self.conn = engine.connect()

    def _get_table_names(self):
        tables_df = pd.read_sql_query(
            'show tables',
            con=self.engine
        )
        return tables_df.Tables_in_stocks.tolist()


    def _check_table_name(self, table_name):
        table_names = self._get_table_names()
        if table_name not in table_names:
            raise Exception('Table {} does not exist in database.'.format(
                table_name))


    def replace_table(self, df, table_name):
        """ Replaces table with provided dataframe

        Args:
            df (pandas.DataFrame):
            table_name (str): table name

        """
        self._check_table_name(table_name)

        df.to_sql(
            table_name,
            con=self.engine,
            if_exists='replace',
            index=False,
        )


    def update_table(self, df, table_name, update_on):
        """ Update a table based on the provided columns.
        If a row does not already exist a row will be appended.

        Args:
            df (pd.DataFrame):
            table_name (str):
            update_on (List[str]): List of column names to update on.

        """
        self._check_table_name(table_name)

        _session_maker = sessionmaker(bind=self.conn)
        session = _session_maker()
        metadata = MetaData()
        db_data = Table(
            table_name,
            metadata,
            autoload=True,
            autoload_with=self.engine
        )

        for _, row in df.iterrows():
            _dict = row.to_dict()
            _filter = and_(db_data.c[i] == _dict.get(i) for i in update_on)
            _data = session.query(db_data).filter(_filter)
            if not len(_data.all()):
                session.execute(db_data.insert(), _dict)
            else:
                _data.update(_dict)
            session.commit()

        session.close()

