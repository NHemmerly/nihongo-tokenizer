FROM python:3.13

WORKDIR /app

COPY requirements.txt .
COPY jlpt_all.pkl . 
COPY unidic_lite/ .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/main.py .

ENTRYPOINT ["python", "main.py"]