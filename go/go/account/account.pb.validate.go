// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: account/account.proto

package account

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

// Validate checks the field values on AccountSettings with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *AccountSettings) Validate() error {
	if m == nil {
		return nil
	}

	// no validation rules for Enabled

	for key, val := range m.GetMemo() {
		_ = val

		if utf8.RuneCountInString(key) < 1 {
			return AccountSettingsValidationError{
				field:  fmt.Sprintf("Memo[%v]", key),
				reason: "value length must be at least 1 runes",
			}
		}

		// no validation rules for Memo[key]
	}

	return nil
}

// AccountSettingsValidationError is the validation error returned by
// AccountSettings.Validate if the designated constraints aren't met.
type AccountSettingsValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountSettingsValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountSettingsValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountSettingsValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountSettingsValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountSettingsValidationError) ErrorName() string { return "AccountSettingsValidationError" }

// Error satisfies the builtin error interface
func (e AccountSettingsValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccountSettings.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountSettingsValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountSettingsValidationError{}

// Validate checks the field values on Account with the rules defined in the
// proto definition for this message. If any rules are violated, an error is returned.
func (m *Account) Validate() error {
	if m == nil {
		return nil
	}

	if !_Account_Name_Pattern.MatchString(m.GetName()) {
		return AccountValidationError{
			field:  "Name",
			reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+$\"",
		}
	}

	if v, ok := interface{}(m.GetSettings()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AccountValidationError{
				field:  "Settings",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetCreatedAt()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AccountValidationError{
				field:  "CreatedAt",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetUpdatedAt()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return AccountValidationError{
				field:  "UpdatedAt",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// AccountValidationError is the validation error returned by Account.Validate
// if the designated constraints aren't met.
type AccountValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e AccountValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e AccountValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e AccountValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e AccountValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e AccountValidationError) ErrorName() string { return "AccountValidationError" }

// Error satisfies the builtin error interface
func (e AccountValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sAccount.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = AccountValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = AccountValidationError{}

var _Account_Name_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+$")