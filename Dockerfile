FROM python:3.8
MAINTAINER Boris Asapov <asapovboris@gmail.com>

# Install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY code/ /usr/src/app/
COPY __init__.py /usr/src/app/restapi/

# Workdir
WORKDIR /usr/src/app

# Exposing Flask port to host
EXPOSE 5000

CMD [ "python", "./app.py" ]