import sqlalchemy

import config


def get_engine(database):
    url = 'mysql://%s:%s@%s:%d/%s' % (
        config.db_user,
        config.db_password,
        config.db_host,
        config.db_port,
        database
    )
    return sqlalchemy.create_engine(url)
