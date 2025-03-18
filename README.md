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
- **EMAIL_BACKEND** - provide Django mail backend. You can
  use [console](https://docs.djangoproject.com/en/dev/topics/email/#console-backend]) for debugging and test purpose
- **EMAIL_HOST** - email host domain
- **EMAIL_PORT** - email host domain port
- **EMAIL_USE_TLS** - use TLS for emails
- **EMAIL_HOST_USER** - email host domain user
- **EMAIL_HOST_PASSWORD** - email host domain user password
- **DEFAULT_FROM_EMAIL** - set default site user email

4. Run migrations

```shell
python manage.py migrate
```

5. Run server:

```shell
python manage.py runserver
```

## Email Configuration

For testing email view, you can use different emil service.
For example, you can create [MailTrap account](https://mailtrap.io/) and test with it.