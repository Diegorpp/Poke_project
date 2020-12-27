FROM postgres

COPY ./src /src/

VOLUME /Arquivos/

EXPOSE 80

ENV POSTGRES_PASSWORD=batata123

WORKDIR /

CMD 