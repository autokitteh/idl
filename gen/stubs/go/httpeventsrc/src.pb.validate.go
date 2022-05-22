// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: httpeventsrc/src.proto

package httpeventsrc

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

// Validate checks the field values on Route with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *Route) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Name

	// no validation rules for Path

	return nil
}

// RouteValidationError is the validation error returned by Route.Validate if
// the designated constraints aren't met.
type RouteValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e RouteValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e RouteValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e RouteValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e RouteValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e RouteValidationError) ErrorName() string { return "RouteValidationError" }

// Error satisfies the builtin error interface
func (e RouteValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sRoute.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = RouteValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = RouteValidationError{}

// Validate checks the field values on BindRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *BindRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_BindRequest_ProjectId_Pattern.MatchString(m.GetProjectId()) {
		return BindRequestValidationError{
			field:  "ProjectId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
		}
	}

	if !_BindRequest_Name_Pattern.MatchString(m.GetName()) {
		return BindRequestValidationError{
			field:  "Name",
			reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
		}
	}

	for idx, item := range m.GetRoutes() {
		_, _ = idx, item

		if item == nil {
			return BindRequestValidationError{
				field:  fmt.Sprintf("Routes[%v]", idx),
				reason: "value is required",
			}
		}

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return BindRequestValidationError{
					field:  fmt.Sprintf("Routes[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// BindRequestValidationError is the validation error returned by
// BindRequest.Validate if the designated constraints aren't met.
type BindRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e BindRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e BindRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e BindRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e BindRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e BindRequestValidationError) ErrorName() string { return "BindRequestValidationError" }

// Error satisfies the builtin error interface
func (e BindRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sBindRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = BindRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = BindRequestValidationError{}

var _BindRequest_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")

var _BindRequest_Name_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on BindResponse with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *BindResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// BindResponseValidationError is the validation error returned by
// BindResponse.Validate if the designated constraints aren't met.
type BindResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e BindResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e BindResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e BindResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e BindResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e BindResponseValidationError) ErrorName() string { return "BindResponseValidationError" }

// Error satisfies the builtin error interface
func (e BindResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sBindResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = BindResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = BindResponseValidationError{}

// Validate checks the field values on UnbindRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *UnbindRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_UnbindRequest_ProjectId_Pattern.MatchString(m.GetProjectId()) {
		return UnbindRequestValidationError{
			field:  "ProjectId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
		}
	}

	if !_UnbindRequest_Name_Pattern.MatchString(m.GetName()) {
		return UnbindRequestValidationError{
			field:  "Name",
			reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
		}
	}

	return nil
}

// UnbindRequestValidationError is the validation error returned by
// UnbindRequest.Validate if the designated constraints aren't met.
type UnbindRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UnbindRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UnbindRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UnbindRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UnbindRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UnbindRequestValidationError) ErrorName() string { return "UnbindRequestValidationError" }

// Error satisfies the builtin error interface
func (e UnbindRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUnbindRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UnbindRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UnbindRequestValidationError{}

var _UnbindRequest_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")

var _UnbindRequest_Name_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on UnbindResponse with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *UnbindResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// UnbindResponseValidationError is the validation error returned by
// UnbindResponse.Validate if the designated constraints aren't met.
type UnbindResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UnbindResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UnbindResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UnbindResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UnbindResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UnbindResponseValidationError) ErrorName() string { return "UnbindResponseValidationError" }

// Error satisfies the builtin error interface
func (e UnbindResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUnbindResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UnbindResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UnbindResponseValidationError{}
