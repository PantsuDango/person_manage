#!/bin/bash

git pull
path=$PWD

cd $path/server
num=$(netstat -nlpt | grep ":::6666" | grep -v "grep" | wc -l)
if [ $num -eq 1 ]; then
    kill -9 $(ps -ef | grep "person_manage" | grep -v "grep" | awk '{print $2}')
    sleep 3
fi
nohup python3 person_manage.py &
sleep 3

num=$(netstat -nlpt | grep ":::6666" | grep -v "grep" | wc -l)
if [ $num -eq 1 ]; then
    echo "run person_manage success"
else
    cd $path/app
    tail -n 10 nohup.out
    echo "run person_manage fail"
fi