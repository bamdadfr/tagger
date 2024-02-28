#!/bin/bash
docker run -it -rm --mount type=bind,source=/home/bamdad/git/tagger/config.yaml,target=/app/config.yaml --mount type=bind,source=/,target=/mount tagger
