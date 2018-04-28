# Osiris-Judge-Core
[![Python](https://img.shields.io/badge/python-3.5.2-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-352/)




Judge core based on Docker.

## Current Support Language

+ GNU G++17
+ Clang 6.0.0
+ GNU GCC 7.3
+ Python 3.6.5
+ Java 10
+ Javascript
+ Go 1.9.2
+ Ruby 2.5.1
+ Rust 1.25.0


## Installation

+ Install `docker` first.
<pre>
    suao apt-get update
    sudo apt-get install docker.io
</pre>

+ Install requirements
<pre>
    pip3 install -r requirements/requirements.txt
</pre>

+ Install judger's image
<pre>
    cd deploy && python3 deploy.py
</pre>