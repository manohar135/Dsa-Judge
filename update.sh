#!/bin/sh
# Get the newest problems (your saved code and history are not touched)
cd "$(dirname "$0")" || exit 1
git pull --ff-only
