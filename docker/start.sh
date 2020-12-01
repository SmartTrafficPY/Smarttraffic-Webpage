#!/usr/bin/env bash

set -e

export DOCKER_HOST=$(ip route show | grep 'default via' | awk '{print $3}')
export PYTHONPATH=/home/app/code

# mkdir -p /home/app/code/smwebsite/media
# chown user /home/app/code/smwebsite/media
# chmod 700 /home/app/code/smwebsite/media

exec $@
