FROM python:3.8.12-slim 
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ["*.py",  "./"] 
EXPOSE 8000
CMD ["uvicorn", "main:app", "--port", "8000"]