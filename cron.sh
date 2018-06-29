#!/bin/bash

# bash script for a crontab to run the Custom Django Management Command off_api

cd /home/jfsubrini/project10_pur_beurre_deploy
source env/bin/activate
./manage.py off_api
