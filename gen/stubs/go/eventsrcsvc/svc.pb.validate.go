// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: eventsrcsvc/svc.proto

package eventsrcsvc

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

// Validate checks the field values on AddEventSourceRequest with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *AddEventSourceRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_AddEventSourceRequest_Id_Pattern.MatchString(m.GetId()) {
		return AddEventSourceRequestValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	if v, ok := interface{}(m.GetSettings()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AddEventSourceRequestValidationError{
				field:  "Settings",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// AddEventSourceRequestValidationError is the validation error returned by
// AddEventSourceRequest.Validate if the designated constraints aren't met.
type AddEventSourceRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AddEventSourceRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AddEventSourceRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AddEventSourceRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AddEventSourceRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AddEventSourceRequestValidationError) ErrorName() string {
	return "AddEventSourceRequestValidationError"
}

// Error satisfies the builtin error interface
func (e AddEventSourceRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAddEventSourceRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AddEventSourceRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AddEventSourceRequestValidationError{}

var _AddEventSourceRequest_Id_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

// Validate checks the field values on AddEventSourceResponse with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *AddEventSourceResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// AddEventSourceResponseValidationError is the validation error returned by
// AddEventSourceResponse.Validate if the designated constraints aren't met.
type AddEventSourceResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AddEventSourceResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AddEventSourceResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AddEventSourceResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AddEventSourceResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AddEventSourceResponseValidationError) ErrorName() string {
	return "AddEventSourceResponseValidationError"
}

// Error satisfies the builtin error interface
func (e AddEventSourceResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAddEventSourceResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AddEventSourceResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AddEventSourceResponseValidationError{}

// Validate checks the field values on UpdateEventSourceRequest with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *UpdateEventSourceRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_UpdateEventSourceRequest_Id_Pattern.MatchString(m.GetId()) {
		return UpdateEventSourceRequestValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	if m.GetSettings() == nil {
		return UpdateEventSourceRequestValidationError{
			field:  "Settings",
			reason: "value is required",
		}
	}

	if v, ok := interface{}(m.GetSettings()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return UpdateEventSourceRequestValidationError{
				field:  "Settings",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// UpdateEventSourceRequestValidationError is the validation error returned by
// UpdateEventSourceRequest.Validate if the designated constraints aren't met.
type UpdateEventSourceRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UpdateEventSourceRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UpdateEventSourceRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UpdateEventSourceRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UpdateEventSourceRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UpdateEventSourceRequestValidationError) ErrorName() string {
	return "UpdateEventSourceRequestValidationError"
}

// Error satisfies the builtin error interface
func (e UpdateEventSourceRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUpdateEventSourceRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UpdateEventSourceRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UpdateEventSourceRequestValidationError{}

var _UpdateEventSourceRequest_Id_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

// Validate checks the field values on UpdateEventSourceResponse with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *UpdateEventSourceResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// UpdateEventSourceResponseValidationError is the validation error returned by
// UpdateEventSourceResponse.Validate if the designated constraints aren't met.
type UpdateEventSourceResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UpdateEventSourceResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UpdateEventSourceResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UpdateEventSourceResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UpdateEventSourceResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UpdateEventSourceResponseValidationError) ErrorName() string {
	return "UpdateEventSourceResponseValidationError"
}

// Error satisfies the builtin error interface
func (e UpdateEventSourceResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUpdateEventSourceResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UpdateEventSourceResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UpdateEventSourceResponseValidationError{}

// Validate checks the field values on GetEventSourceRequest with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *GetEventSourceRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_GetEventSourceRequest_Id_Pattern.MatchString(m.GetId()) {
		return GetEventSourceRequestValidationError{
			field:  "Id",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	return nil
}

// GetEventSourceRequestValidationError is the validation error returned by
// GetEventSourceRequest.Validate if the designated constraints aren't met.
type GetEventSourceRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e GetEventSourceRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e GetEventSourceRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e GetEventSourceRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e GetEventSourceRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e GetEventSourceRequestValidationError) ErrorName() string {
	return "GetEventSourceRequestValidationError"
}

// Error satisfies the builtin error interface
func (e GetEventSourceRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sGetEventSourceRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = GetEventSourceRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = GetEventSourceRequestValidationError{}

var _GetEventSourceRequest_Id_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

// Validate checks the field values on GetEventSourceResponse with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *GetEventSourceResponse) Validate() error {
	if m == nil {
		return nil
	}

	if m.GetSrc() == nil {
		return GetEventSourceResponseValidationError{
			field:  "Src",
			reason: "value is required",
		}
	}

	if v, ok := interface{}(m.GetSrc()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return GetEventSourceResponseValidationError{
				field:  "Src",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// GetEventSourceResponseValidationError is the validation error returned by
// GetEventSourceResponse.Validate if the designated constraints aren't met.
type GetEventSourceResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e GetEventSourceResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e GetEventSourceResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e GetEventSourceResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e GetEventSourceResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e GetEventSourceResponseValidationError) ErrorName() string {
	return "GetEventSourceResponseValidationError"
}

// Error satisfies the builtin error interface
func (e GetEventSourceResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sGetEventSourceResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = GetEventSourceResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = GetEventSourceResponseValidationError{}

// Validate checks the field values on ListEventSourcesRequest with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *ListEventSourcesRequest) Validate() error {
	if m == nil {
		return nil
	}

	if m.GetAccountName() != "" {

		if !_ListEventSourcesRequest_AccountName_Pattern.MatchString(m.GetAccountName()) {
			return ListEventSourcesRequestValidationError{
				field:  "AccountName",
				reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+$\"",
			}
		}

	}

	return nil
}

// ListEventSourcesRequestValidationError is the validation error returned by
// ListEventSourcesRequest.Validate if the designated constraints aren't met.
type ListEventSourcesRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ListEventSourcesRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ListEventSourcesRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ListEventSourcesRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ListEventSourcesRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ListEventSourcesRequestValidationError) ErrorName() string {
	return "ListEventSourcesRequestValidationError"
}

// Error satisfies the builtin error interface
func (e ListEventSourcesRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sListEventSourcesRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ListEventSourcesRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ListEventSourcesRequestValidationError{}

var _ListEventSourcesRequest_AccountName_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+$")

// Validate checks the field values on ListEventSourcesResponse with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *ListEventSourcesResponse) Validate() error {
	if m == nil {
		return nil
	}

	for idx, item := range m.GetIds() {
		_, _ = idx, item

		if !_ListEventSourcesResponse_Ids_Pattern.MatchString(item) {
			return ListEventSourcesResponseValidationError{
				field:  fmt.Sprintf("Ids[%v]", idx),
				reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
			}
		}

	}

	return nil
}

// ListEventSourcesResponseValidationError is the validation error returned by
// ListEventSourcesResponse.Validate if the designated constraints aren't met.
type ListEventSourcesResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e ListEventSourcesResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e ListEventSourcesResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e ListEventSourcesResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e ListEventSourcesResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e ListEventSourcesResponseValidationError) ErrorName() string {
	return "ListEventSourcesResponseValidationError"
}

// Error satisfies the builtin error interface
func (e ListEventSourcesResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sListEventSourcesResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = ListEventSourcesResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = ListEventSourcesResponseValidationError{}

var _ListEventSourcesResponse_Ids_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

// Validate checks the field values on GetEventSourceProjectBindingsRequest
// with the rules defined in the proto definition for this message. If any
// rules are violated, an error is returned.
func (m *GetEventSourceProjectBindingsRequest) Validate() error {
	if m == nil {
		return nil
	}

	if m.GetId() != "" {

		if !_GetEventSourceProjectBindingsRequest_Id_Pattern.MatchString(m.GetId()) {
			return GetEventSourceProjectBindingsRequestValidationError{
				field:  "Id",
				reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
			}
		}

	}

	if m.GetProjectId() != "" {

		if !_GetEventSourceProjectBindingsRequest_ProjectId_Pattern.MatchString(m.GetProjectId()) {
			return GetEventSourceProjectBindingsRequestValidationError{
				field:  "ProjectId",
				reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
			}
		}

	}

	if m.GetName() != "" {

		if !_GetEventSourceProjectBindingsRequest_Name_Pattern.MatchString(m.GetName()) {
			return GetEventSourceProjectBindingsRequestValidationError{
				field:  "Name",
				reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
			}
		}

	}

	// no validation rules for AssociationToken

	// no validation rules for IncludeUnapproved

	return nil
}

// GetEventSourceProjectBindingsRequestValidationError is the validation error
// returned by GetEventSourceProjectBindingsRequest.Validate if the designated
// constraints aren't met.
type GetEventSourceProjectBindingsRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e GetEventSourceProjectBindingsRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e GetEventSourceProjectBindingsRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e GetEventSourceProjectBindingsRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e GetEventSourceProjectBindingsRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e GetEventSourceProjectBindingsRequestValidationError) ErrorName() string {
	return "GetEventSourceProjectBindingsRequestValidationError"
}

// Error satisfies the builtin error interface
func (e GetEventSourceProjectBindingsRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sGetEventSourceProjectBindingsRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = GetEventSourceProjectBindingsRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = GetEventSourceProjectBindingsRequestValidationError{}

var _GetEventSourceProjectBindingsRequest_Id_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

var _GetEventSourceProjectBindingsRequest_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")

var _GetEventSourceProjectBindingsRequest_Name_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on GetEventSourceProjectBindingsResponse
// with the rules defined in the proto definition for this message. If any
// rules are violated, an error is returned.
func (m *GetEventSourceProjectBindingsResponse) Validate() error {
	if m == nil {
		return nil
	}

	for idx, item := range m.GetBindings() {
		_, _ = idx, item

		if item == nil {
			return GetEventSourceProjectBindingsResponseValidationError{
				field:  fmt.Sprintf("Bindings[%v]", idx),
				reason: "value is required",
			}
		}

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return GetEventSourceProjectBindingsResponseValidationError{
					field:  fmt.Sprintf("Bindings[%v]", idx),
					reason: "embedded message failed validation",
					cause:  err,
				}
			}
		}

	}

	return nil
}

// GetEventSourceProjectBindingsResponseValidationError is the validation error
// returned by GetEventSourceProjectBindingsResponse.Validate if the
// designated constraints aren't met.
type GetEventSourceProjectBindingsResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e GetEventSourceProjectBindingsResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e GetEventSourceProjectBindingsResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e GetEventSourceProjectBindingsResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e GetEventSourceProjectBindingsResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e GetEventSourceProjectBindingsResponseValidationError) ErrorName() string {
	return "GetEventSourceProjectBindingsResponseValidationError"
}

// Error satisfies the builtin error interface
func (e GetEventSourceProjectBindingsResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sGetEventSourceProjectBindingsResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = GetEventSourceProjectBindingsResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = GetEventSourceProjectBindingsResponseValidationError{}

// Validate checks the field values on AddEventSourceProjectBindingRequest with
// the rules defined in the proto definition for this message. If any rules
// are violated, an error is returned.
func (m *AddEventSourceProjectBindingRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_AddEventSourceProjectBindingRequest_SrcId_Pattern.MatchString(m.GetSrcId()) {
		return AddEventSourceProjectBindingRequestValidationError{
			field:  "SrcId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	if !_AddEventSourceProjectBindingRequest_ProjectId_Pattern.MatchString(m.GetProjectId()) {
		return AddEventSourceProjectBindingRequestValidationError{
			field:  "ProjectId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
		}
	}

	if m.GetName() != "" {

		if !_AddEventSourceProjectBindingRequest_Name_Pattern.MatchString(m.GetName()) {
			return AddEventSourceProjectBindingRequestValidationError{
				field:  "Name",
				reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
			}
		}

	}

	// no validation rules for AssociationToken

	if v, ok := interface{}(m.GetSettings()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AddEventSourceProjectBindingRequestValidationError{
				field:  "Settings",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	// no validation rules for SourceConfig

	// no validation rules for Approved

	return nil
}

// AddEventSourceProjectBindingRequestValidationError is the validation error
// returned by AddEventSourceProjectBindingRequest.Validate if the designated
// constraints aren't met.
type AddEventSourceProjectBindingRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AddEventSourceProjectBindingRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AddEventSourceProjectBindingRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AddEventSourceProjectBindingRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AddEventSourceProjectBindingRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AddEventSourceProjectBindingRequestValidationError) ErrorName() string {
	return "AddEventSourceProjectBindingRequestValidationError"
}

// Error satisfies the builtin error interface
func (e AddEventSourceProjectBindingRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAddEventSourceProjectBindingRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AddEventSourceProjectBindingRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AddEventSourceProjectBindingRequestValidationError{}

var _AddEventSourceProjectBindingRequest_SrcId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

var _AddEventSourceProjectBindingRequest_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")

var _AddEventSourceProjectBindingRequest_Name_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on AddEventSourceProjectBindingResponse
// with the rules defined in the proto definition for this message. If any
// rules are violated, an error is returned.
func (m *AddEventSourceProjectBindingResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// AddEventSourceProjectBindingResponseValidationError is the validation error
// returned by AddEventSourceProjectBindingResponse.Validate if the designated
// constraints aren't met.
type AddEventSourceProjectBindingResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AddEventSourceProjectBindingResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AddEventSourceProjectBindingResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AddEventSourceProjectBindingResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AddEventSourceProjectBindingResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AddEventSourceProjectBindingResponseValidationError) ErrorName() string {
	return "AddEventSourceProjectBindingResponseValidationError"
}

// Error satisfies the builtin error interface
func (e AddEventSourceProjectBindingResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAddEventSourceProjectBindingResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AddEventSourceProjectBindingResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AddEventSourceProjectBindingResponseValidationError{}

// Validate checks the field values on UpdateEventSourceProjectBindingRequest
// with the rules defined in the proto definition for this message. If any
// rules are violated, an error is returned.
func (m *UpdateEventSourceProjectBindingRequest) Validate() error {
	if m == nil {
		return nil
	}

	if !_UpdateEventSourceProjectBindingRequest_SrcId_Pattern.MatchString(m.GetSrcId()) {
		return UpdateEventSourceProjectBindingRequestValidationError{
			field:  "SrcId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	if !_UpdateEventSourceProjectBindingRequest_ProjectId_Pattern.MatchString(m.GetProjectId()) {
		return UpdateEventSourceProjectBindingRequestValidationError{
			field:  "ProjectId",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
		}
	}

	if !_UpdateEventSourceProjectBindingRequest_Name_Pattern.MatchString(m.GetName()) {
		return UpdateEventSourceProjectBindingRequestValidationError{
			field:  "Name",
			reason: "value does not match regex pattern \"^[a-zA-Z_][a-zA-Z0-9_]*$\"",
		}
	}

	// no validation rules for Approved

	if v, ok := interface{}(m.GetSettings()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return UpdateEventSourceProjectBindingRequestValidationError{
				field:  "Settings",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// UpdateEventSourceProjectBindingRequestValidationError is the validation
// error returned by UpdateEventSourceProjectBindingRequest.Validate if the
// designated constraints aren't met.
type UpdateEventSourceProjectBindingRequestValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UpdateEventSourceProjectBindingRequestValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UpdateEventSourceProjectBindingRequestValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UpdateEventSourceProjectBindingRequestValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UpdateEventSourceProjectBindingRequestValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UpdateEventSourceProjectBindingRequestValidationError) ErrorName() string {
	return "UpdateEventSourceProjectBindingRequestValidationError"
}

// Error satisfies the builtin error interface
func (e UpdateEventSourceProjectBindingRequestValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUpdateEventSourceProjectBindingRequest.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UpdateEventSourceProjectBindingRequestValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UpdateEventSourceProjectBindingRequestValidationError{}

var _UpdateEventSourceProjectBindingRequest_SrcId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z][0-9a-zA-Z_-]+$")

var _UpdateEventSourceProjectBindingRequest_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")

var _UpdateEventSourceProjectBindingRequest_Name_Pattern = regexp.MustCompile("^[a-zA-Z_][a-zA-Z0-9_]*$")

// Validate checks the field values on UpdateEventSourceProjectBindingResponse
// with the rules defined in the proto definition for this message. If any
// rules are violated, an error is returned.
func (m *UpdateEventSourceProjectBindingResponse) Validate() error {
	if m == nil {
		return nil
	}

	return nil
}

// UpdateEventSourceProjectBindingResponseValidationError is the validation
// error returned by UpdateEventSourceProjectBindingResponse.Validate if the
// designated constraints aren't met.
type UpdateEventSourceProjectBindingResponseValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e UpdateEventSourceProjectBindingResponseValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e UpdateEventSourceProjectBindingResponseValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e UpdateEventSourceProjectBindingResponseValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e UpdateEventSourceProjectBindingResponseValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e UpdateEventSourceProjectBindingResponseValidationError) ErrorName() string {
	return "UpdateEventSourceProjectBindingResponseValidationError"
}

// Error satisfies the builtin error interface
func (e UpdateEventSourceProjectBindingResponseValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sUpdateEventSourceProjectBindingResponse.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = UpdateEventSourceProjectBindingResponseValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = UpdateEventSourceProjectBindingResponseValidationError{}
