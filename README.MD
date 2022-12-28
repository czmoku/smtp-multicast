# SMTP Reverse proxy with multicast

## What it is
This application multicast single email to two other smtp servers.

Could be used, for example, during migration from Mailhog to Maildev.

## Envs
SMTP_MULTICAST_PORT - proxy server port, default 1025
FIRST_DESTINATION_HOSTNAME - first destination smtp server hostname, default localhost. 
FIRST_DESTINATION_PORT - first destination smtp server port, default localhost. 
SECOND_DESTINATION_HOSTNAME - second destination smtp server hostname, default localhost. 
SECOND_DESTINATION_PORT - second destination smtp server port, default localhost. 

## Docker

https://hub.docker.com/repository/docker/czmoku/smtp-multicast