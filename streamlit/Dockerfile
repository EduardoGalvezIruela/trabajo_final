FROM python:3.11-slim

RUN mkdir /streamlit

COPY requirements_frontend.txt /streamlit

WORKDIR /streamlit

RUN pip install -r requirements_frontend.txt

COPY . /streamlit

EXPOSE 8501

CMD ["streamlit", "run", "Portada.py"]