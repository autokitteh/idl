Directories:
- **_proto**: Source .proto files. [p2](https://github.com/wrouesnel/p2cli) is used to template some repeating definitions.
- **_scripts**: Scripts (entrypoint is `scripts/gen.sh`) that generate **gen** using [autokitteh/protoc](https://hub.docker.com/r/autokitteh/protoc) docker image.
- **All others**: Generated stubs. `proto` are the post-p2 actual proto files. These are committed to the repository.
