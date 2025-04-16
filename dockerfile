FROM python:3.9-slim

WORKDIR /app

# copy everything into .app
COPY . /app

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# environment variable
ENV PYTHONUNBUFFERED 1

# expose ports
EXPOSE 5000

# run when start
CMD ["python", "main.py"]