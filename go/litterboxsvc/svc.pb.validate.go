// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: litterboxsvc/svc.proto

package litterboxsvc

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

// Validate checks the field values on SetupRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *SetupRequest) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// SetupRequestValidationError is the validation error returned by
// SetupRequest.Validate if the designated constraints aren't met.
type SetupRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SetupRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SetupRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SetupRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SetupRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SetupRequestValidationError) ErrorName() string { return "SetupRequestValidationError" }

// Error satisfies the builtin error interface
func (e SetupRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSetupRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SetupRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SetupRequestValidationError{}

// Validate checks the field values on SetupResponse with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *SetupResponse) Validate() error {
	if m == nil {
		return nil
	}

	if !_SetupResponse_Id_Pattern.MatchString(m.GetId()) {
		return SetupResponseValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^B[0-9a-f]+$\"",
		}
	}

	return nil
}

// SetupResponseValidationError is the validation error returned by
// SetupResponse.Validate if the designated constraints aren't met.
type SetupResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SetupResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SetupResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SetupResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SetupResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SetupResponseValidationError) ErrorName() string { return "SetupResponseValidationError" }

// Error satisfies the builtin error interface
func (e SetupResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSetupResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SetupResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SetupResponseValidationError{}

var _SetupResponse_Id_Pattern = regexp.MustCompile("^B[0-9a-f]+$")

// Validate checks the field values on ScoopRequest with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *ScoopRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_ScoopRequest_Id_Pattern.MatchString(m.GetId()) {
		return ScoopRequestValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^B[0-9a-f]+$\"",
		}
	}

	return nil
}

// ScoopRequestValidationError is the validation error returned by
// ScoopRequest.Validate if the designated constraints aren't met.
type ScoopRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ScoopRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ScoopRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ScoopRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ScoopRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ScoopRequestValidationError) ErrorName() string { return "ScoopRequestValidationError" }

// Error satisfies the builtin error interface
func (e ScoopRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sScoopRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ScoopRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ScoopRequestValidationError{}

var _ScoopRequest_Id_Pattern = regexp.MustCompile("^B[0-9a-f]+$")

// Validate checks the field values on ScoopResponse with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *ScoopResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// ScoopResponseValidationError is the validation error returned by
// ScoopResponse.Validate if the designated constraints aren't met.
type ScoopResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ScoopResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ScoopResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ScoopResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ScoopResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ScoopResponseValidationError) ErrorName() string { return "ScoopResponseValidationError" }

// Error satisfies the builtin error interface
func (e ScoopResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sScoopResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ScoopResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ScoopResponseValidationError{}

// Validate checks the field values on SyntheticEvent with the rules defined in
// the proto definition for this message. If any rules are violated, an error
// is returned.
func (m *SyntheticEvent) Validate() error {
	if m == nil {
		return nil
	}

	if !_SyntheticEvent_SrcBinding_Pattern.MatchString(m.GetSrcBinding()) {
		return SyntheticEventValidationError{
			field:  "SrcBinding",
			reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
		}
	}

	// no validation rules for Type

	for key, val := range m.GetData() {
		_ = val

		if val == nil {
			return SyntheticEventValidationError{
				field:  fmt.Sprintf("Data[%v]", key),
				reason: "value cannot be sparse, all pairs must be non-nil",
			}
		}

		if !_SyntheticEvent_Data_Pattern.MatchString(key) {
			return SyntheticEventValidationError{
				field:  fmt.Sprintf("Data[%v]", key),
				reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
			}
		}

		if v, ok := interface{}(val).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return SyntheticEventValidationError{
					field:  fmt.Sprintf("Data[%v]", key),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	// no validation rules for OriginalId

	return nil
}

// SyntheticEventValidationError is the validation error returned by
// SyntheticEvent.Validate if the designated constraints aren't met.
type SyntheticEventValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e SyntheticEventValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e SyntheticEventValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e SyntheticEventValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e SyntheticEventValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e SyntheticEventValidationError) ErrorName() string { return "SyntheticEventValidationError" }

// Error satisfies the builtin error interface
func (e SyntheticEventValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sSyntheticEvent.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = SyntheticEventValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = SyntheticEventValidationError{}

var _SyntheticEvent_SrcBinding_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

var _SyntheticEvent_Data_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on RunRequest with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *RunRequest) Validate() error {
	if m == nil {
		return nil
	}

	if m.GetId() != "" {

		if !_RunRequest_Id_Pattern.MatchString(m.GetId()) {
			return RunRequestValidationError{
				field:  "Id",
				reason: "value does not match regex pattern \"^B[0-9a-f]+$\"",
			}
		}

	}

	if m.GetEvent() == nil {
		return RunRequestValidationError{
			field:  "Event",
			reason: "value is required",
		}
	}

	if v, ok := interface{}(m.GetEvent()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return RunRequestValidationError{
				field:  "Event",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// RunRequestValidationError is the validation error returned by
// RunRequest.Validate if the designated constraints aren't met.
type RunRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e RunRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e RunRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e RunRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e RunRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e RunRequestValidationError) ErrorName() string { return "RunRequestValidationError" }

// Error satisfies the builtin error interface
func (e RunRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sRunRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = RunRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = RunRequestValidationError{}

var _RunRequest_Id_Pattern = regexp.MustCompile("^B[0-9a-f]+$")

// Validate checks the field values on RunUpdate with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *RunUpdate) Validate() error {
	if m == nil {
		return nil
	}

	if m.GetT() == nil {
		return RunUpdateValidationError{
			field:  "T",
			reason: "value is required",
		}
	}

	if !_RunUpdate_Id_Pattern.MatchString(m.GetId()) {
		return RunUpdateValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^B[0-9a-f]+$\"",
		}
	}

	if m.GetState() == nil {
		return RunUpdateValidationError{
			field:  "State",
			reason: "value is required",
		}
	}

	if v, ok := interface{}(m.GetState()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return RunUpdateValidationError{
				field:  "State",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// RunUpdateValidationError is the validation error returned by
// RunUpdate.Validate if the designated constraints aren't met.
type RunUpdateValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e RunUpdateValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e RunUpdateValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e RunUpdateValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e RunUpdateValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e RunUpdateValidationError) ErrorName() string { return "RunUpdateValidationError" }

// Error satisfies the builtin error interface
func (e RunUpdateValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sRunUpdate.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = RunUpdateValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = RunUpdateValidationError{}

var _RunUpdate_Id_Pattern = regexp.MustCompile("^B[0-9a-f]+$")
