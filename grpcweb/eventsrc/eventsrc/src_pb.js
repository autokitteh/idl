// source: eventsrc/src.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
goog.object.extend(proto, google_protobuf_timestamp_pb);
var validate_validate_pb = require('../validate/validate_pb.js');
goog.object.extend(proto, validate_validate_pb);
goog.exportSymbol('proto.autokitteh.eventsrc.EventSource', null, global);
goog.exportSymbol('proto.autokitteh.eventsrc.EventSourceProjectBinding', null, global);
goog.exportSymbol('proto.autokitteh.eventsrc.EventSourceProjectBindingSettings', null, global);
goog.exportSymbol('proto.autokitteh.eventsrc.EventSourceSettings', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.autokitteh.eventsrc.EventSourceSettings = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.autokitteh.eventsrc.EventSourceSettings.repeatedFields_, null);
};
goog.inherits(proto.autokitteh.eventsrc.EventSourceSettings, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.eventsrc.EventSourceSettings.displayName = 'proto.autokitteh.eventsrc.EventSourceSettings';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.autokitteh.eventsrc.EventSource = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.eventsrc.EventSource, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.eventsrc.EventSource.displayName = 'proto.autokitteh.eventsrc.EventSource';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.eventsrc.EventSourceProjectBindingSettings, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.displayName = 'proto.autokitteh.eventsrc.EventSourceProjectBindingSettings';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.eventsrc.EventSourceProjectBinding, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.eventsrc.EventSourceProjectBinding.displayName = 'proto.autokitteh.eventsrc.EventSourceProjectBinding';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.autokitteh.eventsrc.EventSourceSettings.repeatedFields_ = [2];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.eventsrc.EventSourceSettings.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.eventsrc.EventSourceSettings} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceSettings.toObject = function(includeInstance, msg) {
  var f, obj = {
    enabled: jspb.Message.getBooleanFieldWithDefault(msg, 1, false),
    typesList: (f = jspb.Message.getRepeatedField(msg, 2)) == null ? undefined : f
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings}
 */
proto.autokitteh.eventsrc.EventSourceSettings.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.eventsrc.EventSourceSettings;
  return proto.autokitteh.eventsrc.EventSourceSettings.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.eventsrc.EventSourceSettings} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings}
 */
proto.autokitteh.eventsrc.EventSourceSettings.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setEnabled(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.addTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.eventsrc.EventSourceSettings.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.eventsrc.EventSourceSettings} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceSettings.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnabled();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
  f = message.getTypesList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      2,
      f
    );
  }
};


/**
 * optional bool enabled = 1;
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.getEnabled = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 1, false));
};


/**
 * @param {boolean} value
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings} returns this
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.setEnabled = function(value) {
  return jspb.Message.setProto3BooleanField(this, 1, value);
};


/**
 * repeated string types = 2;
 * @return {!Array<string>}
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.getTypesList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 2));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings} returns this
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.setTypesList = function(value) {
  return jspb.Message.setField(this, 2, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings} returns this
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.addTypes = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 2, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.autokitteh.eventsrc.EventSourceSettings} returns this
 */
proto.autokitteh.eventsrc.EventSourceSettings.prototype.clearTypesList = function() {
  return this.setTypesList([]);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.autokitteh.eventsrc.EventSource.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.eventsrc.EventSource.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.eventsrc.EventSource} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSource.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    settings: (f = msg.getSettings()) && proto.autokitteh.eventsrc.EventSourceSettings.toObject(includeInstance, f),
    createdAt: (f = msg.getCreatedAt()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    updatedAt: (f = msg.getUpdatedAt()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.autokitteh.eventsrc.EventSource}
 */
proto.autokitteh.eventsrc.EventSource.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.eventsrc.EventSource;
  return proto.autokitteh.eventsrc.EventSource.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.eventsrc.EventSource} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.eventsrc.EventSource}
 */
proto.autokitteh.eventsrc.EventSource.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setId(value);
      break;
    case 3:
      var value = new proto.autokitteh.eventsrc.EventSourceSettings;
      reader.readMessage(value,proto.autokitteh.eventsrc.EventSourceSettings.deserializeBinaryFromReader);
      msg.setSettings(value);
      break;
    case 100:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setCreatedAt(value);
      break;
    case 101:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setUpdatedAt(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.autokitteh.eventsrc.EventSource.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.eventsrc.EventSource.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.eventsrc.EventSource} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSource.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getSettings();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      proto.autokitteh.eventsrc.EventSourceSettings.serializeBinaryToWriter
    );
  }
  f = message.getCreatedAt();
  if (f != null) {
    writer.writeMessage(
      100,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getUpdatedAt();
  if (f != null) {
    writer.writeMessage(
      101,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional string id = 1;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSource.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
 */
proto.autokitteh.eventsrc.EventSource.prototype.setId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional EventSourceSettings settings = 3;
 * @return {?proto.autokitteh.eventsrc.EventSourceSettings}
 */
proto.autokitteh.eventsrc.EventSource.prototype.getSettings = function() {
  return /** @type{?proto.autokitteh.eventsrc.EventSourceSettings} */ (
    jspb.Message.getWrapperField(this, proto.autokitteh.eventsrc.EventSourceSettings, 3));
};


/**
 * @param {?proto.autokitteh.eventsrc.EventSourceSettings|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
*/
proto.autokitteh.eventsrc.EventSource.prototype.setSettings = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
 */
proto.autokitteh.eventsrc.EventSource.prototype.clearSettings = function() {
  return this.setSettings(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSource.prototype.hasSettings = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp created_at = 100;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.eventsrc.EventSource.prototype.getCreatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 100));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
*/
proto.autokitteh.eventsrc.EventSource.prototype.setCreatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 100, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
 */
proto.autokitteh.eventsrc.EventSource.prototype.clearCreatedAt = function() {
  return this.setCreatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSource.prototype.hasCreatedAt = function() {
  return jspb.Message.getField(this, 100) != null;
};


/**
 * optional google.protobuf.Timestamp updated_at = 101;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.eventsrc.EventSource.prototype.getUpdatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 101));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
*/
proto.autokitteh.eventsrc.EventSource.prototype.setUpdatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 101, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSource} returns this
 */
proto.autokitteh.eventsrc.EventSource.prototype.clearUpdatedAt = function() {
  return this.setUpdatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSource.prototype.hasUpdatedAt = function() {
  return jspb.Message.getField(this, 101) != null;
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.toObject = function(includeInstance, msg) {
  var f, obj = {
    enabled: jspb.Message.getBooleanFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings}
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.eventsrc.EventSourceProjectBindingSettings;
  return proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings}
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setEnabled(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getEnabled();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool enabled = 1;
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.prototype.getEnabled = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 1, false));
};


/**
 * @param {boolean} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBindingSettings} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.prototype.setEnabled = function(value) {
  return jspb.Message.setProto3BooleanField(this, 1, value);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.eventsrc.EventSourceProjectBinding.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBinding} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.toObject = function(includeInstance, msg) {
  var f, obj = {
    srcId: jspb.Message.getFieldWithDefault(msg, 1, ""),
    projectId: jspb.Message.getFieldWithDefault(msg, 2, ""),
    name: jspb.Message.getFieldWithDefault(msg, 3, ""),
    associationToken: jspb.Message.getFieldWithDefault(msg, 4, ""),
    sourceConfig: jspb.Message.getFieldWithDefault(msg, 5, ""),
    approved: jspb.Message.getBooleanFieldWithDefault(msg, 6, false),
    settings: (f = msg.getSettings()) && proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.toObject(includeInstance, f),
    createdAt: (f = msg.getCreatedAt()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    updatedAt: (f = msg.getUpdatedAt()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.eventsrc.EventSourceProjectBinding;
  return proto.autokitteh.eventsrc.EventSourceProjectBinding.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBinding} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setSrcId(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setProjectId(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.setAssociationToken(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setSourceConfig(value);
      break;
    case 6:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setApproved(value);
      break;
    case 10:
      var value = new proto.autokitteh.eventsrc.EventSourceProjectBindingSettings;
      reader.readMessage(value,proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.deserializeBinaryFromReader);
      msg.setSettings(value);
      break;
    case 100:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setCreatedAt(value);
      break;
    case 101:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setUpdatedAt(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.eventsrc.EventSourceProjectBinding.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.eventsrc.EventSourceProjectBinding} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSrcId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getProjectId();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getAssociationToken();
  if (f.length > 0) {
    writer.writeString(
      4,
      f
    );
  }
  f = message.getSourceConfig();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getApproved();
  if (f) {
    writer.writeBool(
      6,
      f
    );
  }
  f = message.getSettings();
  if (f != null) {
    writer.writeMessage(
      10,
      f,
      proto.autokitteh.eventsrc.EventSourceProjectBindingSettings.serializeBinaryToWriter
    );
  }
  f = message.getCreatedAt();
  if (f != null) {
    writer.writeMessage(
      100,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getUpdatedAt();
  if (f != null) {
    writer.writeMessage(
      101,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional string src_id = 1;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getSrcId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setSrcId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string project_id = 2;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getProjectId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setProjectId = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string name = 3;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional string association_token = 4;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getAssociationToken = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 4, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setAssociationToken = function(value) {
  return jspb.Message.setProto3StringField(this, 4, value);
};


/**
 * optional string source_config = 5;
 * @return {string}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getSourceConfig = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setSourceConfig = function(value) {
  return jspb.Message.setProto3StringField(this, 5, value);
};


/**
 * optional bool approved = 6;
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getApproved = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 6, false));
};


/**
 * @param {boolean} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setApproved = function(value) {
  return jspb.Message.setProto3BooleanField(this, 6, value);
};


/**
 * optional EventSourceProjectBindingSettings settings = 10;
 * @return {?proto.autokitteh.eventsrc.EventSourceProjectBindingSettings}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getSettings = function() {
  return /** @type{?proto.autokitteh.eventsrc.EventSourceProjectBindingSettings} */ (
    jspb.Message.getWrapperField(this, proto.autokitteh.eventsrc.EventSourceProjectBindingSettings, 10));
};


/**
 * @param {?proto.autokitteh.eventsrc.EventSourceProjectBindingSettings|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
*/
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setSettings = function(value) {
  return jspb.Message.setWrapperField(this, 10, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.clearSettings = function() {
  return this.setSettings(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.hasSettings = function() {
  return jspb.Message.getField(this, 10) != null;
};


/**
 * optional google.protobuf.Timestamp created_at = 100;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getCreatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 100));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
*/
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setCreatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 100, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.clearCreatedAt = function() {
  return this.setCreatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.hasCreatedAt = function() {
  return jspb.Message.getField(this, 100) != null;
};


/**
 * optional google.protobuf.Timestamp updated_at = 101;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.getUpdatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 101));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
*/
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.setUpdatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 101, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.eventsrc.EventSourceProjectBinding} returns this
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.clearUpdatedAt = function() {
  return this.setUpdatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.eventsrc.EventSourceProjectBinding.prototype.hasUpdatedAt = function() {
  return jspb.Message.getField(this, 101) != null;
};


goog.object.extend(exports, proto.autokitteh.eventsrc);