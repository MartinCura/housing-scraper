FROM python:3.8

WORKDIR /code

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --dev --system
# RUN pipenv install --dev --system --deploy --ignore-pipfile

COPY app ./app
COPY main.py smoke_test.py ./
COPY configuration.yml setup.sh ./

# Should run this somehow
# RUN bash setup.sh

# CMD ["python", "smoke_test.py"]
CMD ["python", "main.py"]

# VOLUME ./data/:/code/data/
