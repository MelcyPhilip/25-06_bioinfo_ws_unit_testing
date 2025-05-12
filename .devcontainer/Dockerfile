FROM python:3.14.0a2-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        git \
        fish \
        silversearcher-ag \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && pip install --no-cache-dir \
        pytest==7.4.3 \
        pyyaml==6.0.2