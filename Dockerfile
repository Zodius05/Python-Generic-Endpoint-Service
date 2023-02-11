FROM python:3.10.8

RUN useradd --create-home --shell /bin/bash pyservice

USER pyservice
RUN pip install Flask==2.2.2 Flask-HTTPAuth==4.7.0 requests==2.25.1

COPY src/post_endpoint_service.py /home/post_endpoint_service/
COPY src/templates /home/post_endpoint_service/templates/
COPY src/static /home/post_endpoint_service/static/

# Change this to your timezone
ENV TZ=Australia/Adelaide

EXPOSE 8008
CMD [ "python3", "/home/post_endpoint_service/post_endpoint_service.py" ]