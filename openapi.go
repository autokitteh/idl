package idl

import (
	"embed"
	"io/fs"
)

var (
	//go:embed openapi
	openAPIFS embed.FS

	OpenAPIFS, _ = fs.Sub(openAPIFS, "openapi")
)
