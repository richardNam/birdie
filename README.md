# birdie

A personal, for fun, project that fetches stock ticker data and stores it in a database. Data is fetched using the [Alpha Vantange](https://www.alphavantage.co) API.

The `birdie/etl/vantage/` directory is a good place to start. Under that directory you'll see the following files. 

- `handler.py`, file that calls the Alpha Vantage client, a SQL client, and a transform function.
- `client.py`, file that contains the Alpha Vantage client.
- `transform.py`, transformations that are used in the handler. 

There is some additonal code under `birdie/db/` that defines a db client along with helpful SQL statements.
