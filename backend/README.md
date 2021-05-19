# backend

## Python3.7.6 실행환경(manage.py 위치)

## Virtual Environment 생성 및 설정
```
> cd "backend설치된 경로하위"
> python -m venv venv
(Windows) .\venv\Scripts\activate.bat
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

### Admin 계정생성
```
> python manage.py createsuperuser
```

### 테스트 서버 실행 및 결과 확인
```
> python manage.py runserver

(호출결과)
http://127.0.0.1:8080/admin/
http://127.0.0.1:8080/api/videos/
http://127.0.0.1:8080/api/videos/1/
http://127.0.0.1:8080/auth/
http://127.0.0.1:8080/api/ratings/
```

### 참고
```
* 실제 실행한 sql 확인
python manage.py sqlmigrate "migrate결과ID"
```
