# Store Shop

Учебный многостраничный сайт онлайн-магазина с возможностью регистрации покупателей с целью добавлять в корзину покупки и ослеживать заказы. База данных - PostgreSQL. 

## Quickstart

Run the following commands to bootstrap your environment:

    sudo apt-get install -y git python-venv python-pip
    git clone 
    cd store-shop

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    cp .env

Run the app locally:
    
    python manage.py runserver

Run the app docker-compose:

    git clone 
    cd store-shop
    docker-compose up   

При попытках развернуть приложение с помощью docker-compose возникает "OperationalError: connection to server at "localhost" (::1), port 5432 failed: Connection refused". Пытаюсь разобраться, но решение пока не найдено.
    
