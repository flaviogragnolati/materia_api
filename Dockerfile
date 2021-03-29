FROM python:3.9.1-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /materia
COPY ./materia /materia
WORKDIR /materia
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user_materia
RUN chown -R user_materia:user_materia /vol
RUN chmod -R 755 /vol/web
USER user_materia

CMD ["entrypoint.sh"]
