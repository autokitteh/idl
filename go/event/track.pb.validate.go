// Code generated by protoc-gen-validate. DO NOT EDIT.
// source: event/track.proto

package event

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

// Validate checks the field values on TrackIngestEventUpdate with the rules
// defined in the proto definition for this message. If any rules are
// violated, an error is returned.
func (m *TrackIngestEventUpdate) Validate() error {
	if m == nil {
		return nil
	}

	if !_TrackIngestEventUpdate_EventId_Pattern.MatchString(m.GetEventId()) {
		return TrackIngestEventUpdateValidationError{
			field:  "EventId",
			reason: "value does not match regex pattern \"^E[0-9a-f]+$\"",
		}
	}

	if v, ok := interface{}(m.GetEventState()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TrackIngestEventUpdateValidationError{
				field:  "EventState",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if m.GetProjectId() != "" {

		if !_TrackIngestEventUpdate_ProjectId_Pattern.MatchString(m.GetProjectId()) {
			return TrackIngestEventUpdateValidationError{
				field:  "ProjectId",
				reason: "value does not match regex pattern \"^[a-zA-Z][0-9a-zA-Z_-]+\\\\.[a-zA-Z0-9_-]+$\"",
			}
		}

	}

	if v, ok := interface{}(m.GetProjectEventState()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TrackIngestEventUpdateValidationError{
				field:  "ProjectEventState",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	if v, ok := interface{}(m.GetFlattenedRunSummary()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return TrackIngestEventUpdateValidationError{
				field:  "FlattenedRunSummary",
				reason: "embedded message failed validation",
				cause:  err,
			}
		}
	}

	return nil
}

// TrackIngestEventUpdateValidationError is the validation error returned by
// TrackIngestEventUpdate.Validate if the designated constraints aren't met.
type TrackIngestEventUpdateValidationError struct {
	field  string
	reason string
	cause  error
	key    bool
}

// Field function returns field value.
func (e TrackIngestEventUpdateValidationError) Field() string { return e.field }

// Reason function returns reason value.
func (e TrackIngestEventUpdateValidationError) Reason() string { return e.reason }

// Cause function returns cause value.
func (e TrackIngestEventUpdateValidationError) Cause() error { return e.cause }

// Key function returns key value.
func (e TrackIngestEventUpdateValidationError) Key() bool { return e.key }

// ErrorName returns error name.
func (e TrackIngestEventUpdateValidationError) ErrorName() string {
	return "TrackIngestEventUpdateValidationError"
}

// Error satisfies the builtin error interface
func (e TrackIngestEventUpdateValidationError) Error() string {
	cause := ""
	if e.cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.cause)
	}

	key := ""
	if e.key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sTrackIngestEventUpdate.%s: %s%s",
		key,
		e.field,
		e.reason,
		cause)
}

var _ error = TrackIngestEventUpdateValidationError{}

var _ interface {
	Field() string
	Reason() string
	Key() bool
	Cause() error
	ErrorName() string
} = TrackIngestEventUpdateValidationError{}

var _TrackIngestEventUpdate_EventId_Pattern = regexp.MustCompile("^E[0-9a-f]+$")

var _TrackIngestEventUpdate_ProjectId_Pattern = regexp.MustCompile("^[a-zA-Z][0-9a-zA-Z_-]+\\.[a-zA-Z0-9_-]+$")
