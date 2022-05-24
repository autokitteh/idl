#!/bin/bash

set -euo pipefail

mkdir -p /gen/go/go.autokitteh.dev/idl/go
rm -fR /gen/go/go.autokitteh.dev/idl/go/*

find /gen/proto/src -mindepth 1 -type d | while read -r indir; do
  echo "go protoc: ${indir}"

  /usr/bin/protoc \
    -I "/gen/proto/src" \
    -I "/proto" \
    --go_out="/gen/go" \
    --go-grpc_out="/gen/go" \
    --grpc-gateway_out="/gen/go" \
    --validate_out="lang=go:/gen/go" \
    "${indir}"/*
done
