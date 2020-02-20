# Currency converter
Simple django app running as Docker container which can convert Euro, Dollar and Yen in all directions.

API used for exchange rate: ``https://api.exchangeratesapi.io/latest``

## How to build
``docker-compose build`` 

## How to run
``docker-compose up``

Go to http://localhost:8000/currency/convert to access the app.