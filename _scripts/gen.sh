#!/bin/bash

set -euo pipefail

PROTOC_IMAGE_NAME="autokitteh/protoc"

run() {
  docker run \
    --rm \
    -it \
    -v "${PWD}/proto:/gen/proto/src" \
    -v "${PWD}/go:/gen/go/go.autokitteh.dev/idl/go" \
    -v "${PWD}/py:/gen/py" \
    -v "${PWD}/openapi:/gen/openapi" \
    -v "${PWD}/_scripts:/scripts:ro" \
    -v "${PWD}/_proto:/proto/src:ro" \
    "${PROTOC_IMAGE_NAME}" \
    "${@}"
}

run "${CMD-/scripts/_all.sh}"
