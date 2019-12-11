#!/bin/sh
docker run --name for_twenty -d -p 8000:5000 --rm -e SECRET_KEY=new-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=radomirduoistin@gmail.com -e MAIL_PASSWORD=duoshpereinsem \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://for_twenty:hihogo88@dbserver/for_twenty \
    for_twenty:latest \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    for_twenty:latest