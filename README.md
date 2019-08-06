# Docker in AWS Todo Application

This repository provides a sample application based upon the **Todo Project**.

Docker Container NAme | Description
------------ | -------------
APP | Alpine, Django 
DB | Mariadb server 
API | Alpine, GeoLite2-City based on **workivate/geoip-api** image


## Requirements

- Docker 17.09 or higher
- Docker Compose 1.18 or higher
- Brew package manager (recommended for MacOS)
- GNU Make 3.82 or higher (note that MacOS ships with version 3.81)
- jq
- AWS CLI

## Quick Start

To Build test and release the application stack please run the below:

- To Run the test stage:
`make test`


- To Run the release stage:
`make release`

- To Clean up:
`make clean`

## Deployment 

- Configure AWS Account & IAM 
- Deployment using AWS CloudFormation aws folder 
- Documentation Swagger UI 


## Disclaimer

Please note that this app is not production ready and must not be used in production envirment.