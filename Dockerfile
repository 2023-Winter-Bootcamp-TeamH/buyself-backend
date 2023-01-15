FROM python:3.9

# python .pyc 파일 생성하지 않도록 / 로그가 버퍼링없이 즉각 출력되도록
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 개발용
COPY . /app
WORKDIR /app

# mac os 버전일 경우 -> pip3로 변경 / 디펜던시 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]