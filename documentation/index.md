# Documentation Work at Olist Docs

## Requirements

* Python 3.5 >=


## Set up project
1. First of all clone this project.
> git clone https://github.com/DouglasHSS/work-at-olist.git

2. Install all requirements.
>  make install_local_deps

3. Execute database migrations.
>  make migrate

4. Populate database. You can use the csv file in **csv_sample/**.
> make import_categories CHANNEL_NAME CSV_PATH

4. Finally run the server. By default PORT=8000 in case you wish omit it.
> make run_server PORT=8080

5. And have fun accesing the folowing link:
> http://localhost:8080/

## How to ensure the tests are ok?
Just run the following command:
> make coverage

## API Documentation
#### For a datailed documentation about the API just access:
> http://localhost:8080/

