FROM python:3.9-slim

ENV FORWARDED_ALLOW_IPS=* \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-dev && \
    rm -rf ~/.cache/pypoetry 

COPY src /src

CMD ['python', '-m', 'src']
