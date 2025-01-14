# Postgresql

## Installation

Installation [under Debian](https://wiki.debian.org/PostgreSql)
```
apt install postgresql postgresql-client
```
This creates a linux user postgres

## Using the psql command line

```
su - postgresql
psql
```

#### Create database

```
create database <databasename>;
```
Where `<databasename>`has to replaced by the name of the databse

#### Important command line prompts

connect to database
```
\c <databasename>
```
List all available databases
```
\l
```
List all tables in database
```
\dt
```
Show sql help
```
\h
```
Show prompts help
```
\?
```
#### Create new role

