FROM python:3.11-slim

RUN apt-get update && apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && apt-get install -y \
    tzdata \
    gcc \
    python3-dev \
    libffi-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    git openssh-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.ssh && \
    ssh-keyscan -p 22 www.gitlab-smbh.webtm.ru >> /root/.ssh/known_hosts

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install poetry
COPY . .
RUN --mount=type=ssh poetry lock
RUN poetry config virtualenvs.in-project false
RUN --mount=type=ssh poetry install --no-root --only main
