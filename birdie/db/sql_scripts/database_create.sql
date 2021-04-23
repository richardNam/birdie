CREATE DATABASE stocks;
CREATE USER 'db_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hello';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, DROP, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON stocks.* TO 'db_user'@'localhost';

USE stocks;
CREATE TABLE vantage_data (
	close FLOAT DEFAULT NULL comment 'close price',
	high FLOAT DEFAULT NULL comment 'intra day high price',
	low FLOAT DEFAULT NULL comment 'intra day low price',
	observation_ts INT NOT NULL comment 'unix timestamp of observation',
	open FLOAT DEFAULT NULL comment 'open price',
	volume FLOAT DEFAULT NULL comment 'trade volume',
	last_refreshed_ts INT DEFAULT NULL comment 'last time the stock data was updated',
	timezone VARCHAR(255) DEFAULT NULL comment 'timezone',
	symbol VARCHAR(255) DEFAULT NULL comment 'stock symbol',
INDEX symbol_obs_ts (symbol, observation_ts));

