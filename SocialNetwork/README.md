# Social Network

Social Network site for create posts.

## Work flow

- Logs: Server logs that need to be analyzed are identified.

### API Endpoints

#### Post API :
1. Get all post API- http://127.0.0.1:8000/api/post </br>
Request Header: 
``
Authorization Bearer <token>
``
2. Create Post API - http://127.0.0.1:8000/api/post </br>

## Test case
```
python manage.py test
```

## Usage

1. Docker & Docker-compose install (Ubuntu)

2. Docker-compose up command
```
docker-compose up --build
```
3. Service runs on (http://localhost:8000)

## Bot
1. Run Bot with command `python bot.py`
