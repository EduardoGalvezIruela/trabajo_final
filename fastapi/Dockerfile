FROM tiangolo/uvicorn-gunicorn

RUN mkdir /fastapi

COPY requirements_backend.txt /fastapi

WORKDIR /fastapi

RUN pip install -r requirements_backend.txt

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]