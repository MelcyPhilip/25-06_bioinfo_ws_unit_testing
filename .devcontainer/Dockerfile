FROM python:3.14.0a2-slim
ENV http_proxy=http://proxy.ihelse.net:3128
ENV https_proxy=http://proxy.ihelse.net:3128
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        fish \
        silversearcher-ag \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && pip install --no-cache-dir pytest==7.4.3