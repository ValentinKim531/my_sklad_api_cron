FROM python:3.10.2

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y cron supervisor

# Указание таймзоны
ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY cron_schedule /etc/cron.d/cron_schedule
RUN chmod 0644 /etc/cron.d/cron_schedule

RUN crontab /etc/cron.d/cron_schedule

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
