#!/bin/sh
docker run --name for_twenty -d -p 8000:5000 --rm -e SECRET_KEY=new-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=$EMAIL -e MAIL_PASSWORD=$EMAIL_PASS \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://for_twenty:$TEST_PASS@dbserver/for_twenty \
    for_twenty:latest \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    for_twenty:latest
