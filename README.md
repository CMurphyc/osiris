# Osiris-Judge-Core
[![Python](https://img.shields.io/badge/python-3.5.4-orange.svg?style=flat-square)](https://www.python.org/downloads/release/python-354/)
[![License](https://img.shields.io/badge/License-GPLv3-ff69b4.svg?style=flat-square)](https://www.gnu.org/licenses/gpl.html)



Judge core based on Celery and Docker.

## Current Support Language

+ GNU G++17
+ Clang 6.0.0
+ GNU GCC 7.3
+ Python 3.6.5
+ Java 10(OpenJDK Runtime Environment (build 10.0.1+10-Debian-4)
+ Go 1.10.2
+ Ruby 2.5.1
+ Rust 1.25.0

## Upcoming Update

Use Linux Control Groups limit the run-time resrouce

New Language Support
+ Javascript
+ Matlab

## Installation

+ Install submodule
    ```
    git submodule init
    git submodule update
    ```

+ Install [`docker-ce`](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)

+ Install requirements
    ```
    pip3 install -r requirements/requirements.txt
    ```

+ Install judger's image
    ```
    cd deploy && python3 deploy.py
    ```

+ Build checker from testlib and compile core
    ```
    python3 build.py
    ```

+ Install rabbitmq-server
    ```
    sudo apt-get update
    sudo apt-get install rabbitmq-server
    sudo systemctl enable rabbitmq-server
    sudo systemctl start rabbitmq-server
    sudo systemctl status rabbitmq-server
    ```

## Config

+ Edit util/settings.py
    ```
    cp util/settings.py.template util/settings.py
    FETCH_DATA_ADDR = Lutece.address
    FETCH_DATA_AUTHKEY = Lutece.data_server.authkey
    ! You may pay attention to http or https
    ```

+ Edit settings.py
    ```
    cp settings.py.template settings.py
    MAX_JUDGE_PROCESS = the number of worker process
    ```

+ Edit celeryconfig.py
    ```
    cp celeryconfig.py.template celeryconfig.py
    rabbitmq_ip = Lutece.address
    rabbitmq_pwd = Lutece.rabbitmq.judge_user.password
    ```

## Run:
    sh run_worker.sh

## Close
    Press Ctrl + c close worker