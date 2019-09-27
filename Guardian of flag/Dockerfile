FROM python:3.7-alpine
RUN apk update && apk add --no-cache gcc musl-dev zlib-dev
RUN pip3 install flask gunicorn gevent
ADD . /code
WORKDIR /code
# RUN chmod -R o=rt /code/
# RUN chmod o=rxt /code/
# RUN chmod o=rxt -R templates
RUN rm Dockerfile
RUN rm db.sqlite3
RUN python3 generate_db.py
RUN mv /bin/rm /dev/null
RUN adduser -H -D user
RUN chmod 777 -R /code
USER user
CMD ["gunicorn", "--worker-class",  "gevent", "--worker-connections", "768", "--bind", "0.0.0.0:5000", "main:app"]
