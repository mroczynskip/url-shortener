# url-shortener

## Requirements
Supported Python version is 3.11

Additional required Python libraries are specified in `requirements.txt` file
## Starting the app
Instructions how to start the application

### Using Docker
```
docker-compose up --build
```

### Locally
- Move to app directory:
```cd app```

- Create `.env` file:
```
cp .env.example .env
```

- Fill `SECRET_KEY` value in `.env` file and change other parameters if desired

- Run migrations
```
python app/manage.py migrate
```

- Start the app
```
python app/manage.py runserver
```

## Using the app
In both cases app should be available on http://localhost:8000

## Contributing
Before commiting install pre-commit hooks:
```
python -m pip install pre-commit
pre-commit install
```
