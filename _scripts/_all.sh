#!/bin/bash

set -euo pipefail

rm -fR gen/proto
mkdir -p gen/proto/src

for stage in tmpl openapi grpcweb go py; do
  rm -fR gen/"${stage}"/*
  "$(dirname "$0")/_${stage}.sh"
done
