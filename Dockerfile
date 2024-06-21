FROM python:3.10.2

WORKDIR /app

# Копирование файлов requirements.txt и установка зависимостей
COPY requirements.txt requirements.txt
RUN python -m venv /app/.venv
RUN /app/.venv/bin/pip install --upgrade pip
RUN /app/.venv/bin/pip install -r requirements.txt

# Копирование всех файлов в рабочую директорию
COPY . .

# Установка cron и supervisord
RUN apt-get update && apt-get install -y cron supervisor

# Указание таймзоны
ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Копирование расписания cron и установка прав доступа
COPY cron_schedule /etc/cron.d/cron_schedule
RUN chmod 0644 /etc/cron.d/cron_schedule

# Установка crontab
RUN crontab /etc/cron.d/cron_schedule

# Копирование и установка конфигурации для supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Запуск supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
