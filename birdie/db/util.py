from . import db_config

import sqlalchemy


def get_engine(database):
    url = 'mysql://%s:%s@%s:%d/%s' % (
        db_config.db_user,
        db_config.db_password,
        db_config.db_host,
        db_config.db_port,
        database
    )
    return sqlalchemy.create_engine(url)
