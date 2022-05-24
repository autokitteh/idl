#!/bin/bash

set -euo pipefail

for stage in tmpl openapi go py; do
  rm -fR gen/"${stage}"/*
  "$(dirname "$0")/_${stage}.sh"
done
