#!/bin/bash
apt-get update
apt-get install -y build-essential cmake libopenblas-dev liblapack-dev
pip install -r requirements.txt 