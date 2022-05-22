#!/bin/bash

set -euo pipefail

PROTOC_IMAGE_NAME="autokitteh/protoc"

rm -fR gen
mkdir -p gen

run() {
  docker run \
    --rm \
    -it \
    -v "${PWD}/proto:/proto/src:ro" \
    -v "${PWD}/gen/src:/gen/proto/src" \
    -v "${PWD}/gen/stubs/go:/gen/go/go.autokitteh.dev/idl" \
    -v "${PWD}/gen/stubs/py:/gen/py" \
    -v "${PWD}/gen/openapi:/gen/openapi" \
    -v "${PWD}/gen/stubs/grpcweb:/gen/grpcweb" \
    -v "${PWD}/scripts:/scripts:ro" \
    "${PROTOC_IMAGE_NAME}" \
    "${@}"
}

run "${CMD-/scripts/_all.sh}"
