# Data-Modeling-with-Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Prerequisites

This project makes the folowing assumptions:

    Python 3 is available
    pandas and psycopg2 are available
    A PosgreSQL database is available on localhost
    for the AWS database, you must create postgres data and specify the secuirty group to allow traffic and to put the database config in .env


## Database Schema

After examining the Log and Song JSON files, I created a Star schema (shown below) that include one Fact table (songplays) and 4 Dimension tables.


<img width="785" alt="sparkifydb_erd 3" src="https://user-images.githubusercontent.com/22025520/180621766-f7e9a8f4-4841-4906-8a73-738cf6a8a687.png">


## Description of Files

### Directory: data/log_data

This directory contains a collection of JSON log files. These files are used to populate our Fact table - Song Plays - and to populate the Dimension tables for Users and Time.

### Directory: data/song_data

This directory contains a collection of Song JSON files. These files are used to populate Dimension tables for Songs and Artists.

### create_tables.py

This Python script recreates the database and tables used to storethe data.

### etl.py

This Python script reads in the Log and Song data files, processes and inserts data into the database.

### sql_queries.py

A Python script that defines all the SQL statements used by this project.

### test.ipynb

A Python Jupyter Notebook that was used to test that data was loaded properly.
