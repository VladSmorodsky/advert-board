# Advert Board
## Description
It's a pet project written by Django.

## Project Setup
1. Clone the repo
2. Change working dir to project root: 
```shell
cd board
```
3. Copy `board/.env.example` file and enter values into `board/.env` file:
- **PROJECT_SECRET_KEY** - project secret key
4. Run migrations
```shell
python manage.py migrate
```
5. Run server:
```shell
python manage.py runserver
```