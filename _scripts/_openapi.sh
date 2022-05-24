#!/bin/bash

set -euo pipefail

mkdir -p /gen/openapi
rm -fR /gen/openapi/*

find /gen/proto/src -mindepth 1 -type d | while read -r indir; do
  echo "openapi protoc: ${indir}"
  mkdir -p /gen/openapi/$(basename ${indir})

  /usr/bin/protoc \
    -I "/gen/proto/src" \
    -I "/proto" \
    --openapiv2_out="/gen/openapi" \
    "${indir}"/*
done
