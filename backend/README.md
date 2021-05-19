# backend

## Python3.7.6 실행환경(manage.py 위치)

## Virtual Environment 생성 및 설정
```
> cd "backend설치된 경로하위"
> python -m venv venv
(Windows) .\venv\bin\activate.bat
(Linux) source ./venv/bin/activate
```

### 필요 라이브러리 설치
```
> pip install -r requirements.txt
```

### Model 생성 및 DB반영
```
> python manage.py makemigrations youtubeapi
> python manage.py migrate
```

### 테스트 서버 실행 및 결과 확인
```
> python manage.py makemigrations youtubeapi
> python manage.py migrate
```

### 참고
```
* 실제 실행한 sql 확인
python manage.py sqlmigrate "migrate결과ID"
```