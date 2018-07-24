#!/usr/bin/env bash

# Settings

CONCURRENCY=50
REQUESTS=100

ab -n $REQUESTS -c $CONCURRENCY http://localhost:5000/v1/words/count

