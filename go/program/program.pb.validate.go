// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: program/program.proto

package program

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"google.golang.org/protobuf/types/known/anypb"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = anypb.Any{}
)

// Validate checks the field values on Path with the rules defined in the proto
// definition for this message. If any rules are violated, an error is returned.
func (m *Path) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Scheme

	if utf8.RuneCountInString(m.GetPath()) < 1 {
		return PathValidationError{
			field:  "Path",
			reason: "value length must be at least 1 runes",
		}
	}

	// no validation rules for Version

	return nil
}

// PathValidationError is the validation error returned by Path.Validate if the
// designated constraints aren't met.
type PathValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e PathValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e PathValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e PathValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e PathValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e PathValidationError) ErrorName() string { return "PathValidationError" }

// Error satisfies the builtin error interface
func (e PathValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sPath.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = PathValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = PathValidationError{}

// Validate checks the field values on Location with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *Location) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetPath()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return LocationValidationError{
				field:  "Path",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	// no validation rules for Line

	// no validation rules for Column

	return nil
}

// LocationValidationError is the validation error returned by
// Location.Validate if the designated constraints aren't met.
type LocationValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e LocationValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e LocationValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e LocationValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e LocationValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e LocationValidationError) ErrorName() string { return "LocationValidationError" }

// Error satisfies the builtin error interface
func (e LocationValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sLocation.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = LocationValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = LocationValidationError{}

// Validate checks the field values on Module with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *Module) Validate() error {
	if m == nil {
		return nil
	}

	if !_Module_Lang_Pattern.MatchString(m.GetLang()) {
		return ModuleValidationError{
			field:  "Lang",
			reason: "value does not match regex pattern \"^[0-9a-zA-Z_-]+$\"",
		}
	}

	for idx, item := range m.GetPredecls() {
		_, _ = idx, item

		if !_Module_Predecls_Pattern.MatchString(item) {
			return ModuleValidationError{
				field:  fmt.Sprintf("Predecls[%v]", idx),
				reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
			}
		}

	}

	// no validation rules for CompilerVersion

	if m.GetSourcePath() == nil {
		return ModuleValidationError{
			field:  "SourcePath",
			reason: "value is required",
		}
	}

	if v, ok := interface{}(m.GetSourcePath()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return ModuleValidationError{
				field:  "SourcePath",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	// no validation rules for CompiledCode

	return nil
}

// ModuleValidationError is the validation error returned by Module.Validate if
// the designated constraints aren't met.
type ModuleValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ModuleValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ModuleValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ModuleValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ModuleValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ModuleValidationError) ErrorName() string { return "ModuleValidationError" }

// Error satisfies the builtin error interface
func (e ModuleValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sModule.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ModuleValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ModuleValidationError{}

var _Module_Lang_Pattern = regexp.MustCompile("^[0-9a-zA-Z_-]+$")

var _Module_Predecls_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")
