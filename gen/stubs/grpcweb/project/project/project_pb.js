// source: project/project.proto
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
var program_program_pb = require('../program/program_pb.js');
goog.object.extend(proto, program_program_pb);
var values_values_pb = require('../values/values_pb.js');
goog.object.extend(proto, values_values_pb);
goog.exportSymbol('proto.autokitteh.project.Project', null, global);
goog.exportSymbol('proto.autokitteh.project.ProjectPlugin', null, global);
goog.exportSymbol('proto.autokitteh.project.ProjectSettings', null, global);
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
proto.autokitteh.project.ProjectPlugin = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.project.ProjectPlugin, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.project.ProjectPlugin.displayName = 'proto.autokitteh.project.ProjectPlugin';
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
proto.autokitteh.project.ProjectSettings = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.autokitteh.project.ProjectSettings.repeatedFields_, null);
};
goog.inherits(proto.autokitteh.project.ProjectSettings, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.project.ProjectSettings.displayName = 'proto.autokitteh.project.ProjectSettings';
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
proto.autokitteh.project.Project = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.project.Project, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.project.Project.displayName = 'proto.autokitteh.project.Project';
}



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
proto.autokitteh.project.ProjectPlugin.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.project.ProjectPlugin.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.project.ProjectPlugin} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.ProjectPlugin.toObject = function(includeInstance, msg) {
  var f, obj = {
    pluginId: jspb.Message.getFieldWithDefault(msg, 1, ""),
    enabled: jspb.Message.getBooleanFieldWithDefault(msg, 2, false)
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
 * @return {!proto.autokitteh.project.ProjectPlugin}
 */
proto.autokitteh.project.ProjectPlugin.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.project.ProjectPlugin;
  return proto.autokitteh.project.ProjectPlugin.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.project.ProjectPlugin} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.project.ProjectPlugin}
 */
proto.autokitteh.project.ProjectPlugin.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setPluginId(value);
      break;
    case 2:
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
proto.autokitteh.project.ProjectPlugin.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.project.ProjectPlugin.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.project.ProjectPlugin} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.ProjectPlugin.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getPluginId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getEnabled();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
};


/**
 * optional string plugin_id = 1;
 * @return {string}
 */
proto.autokitteh.project.ProjectPlugin.prototype.getPluginId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.project.ProjectPlugin} returns this
 */
proto.autokitteh.project.ProjectPlugin.prototype.setPluginId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional bool enabled = 2;
 * @return {boolean}
 */
proto.autokitteh.project.ProjectPlugin.prototype.getEnabled = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 2, false));
};


/**
 * @param {boolean} value
 * @return {!proto.autokitteh.project.ProjectPlugin} returns this
 */
proto.autokitteh.project.ProjectPlugin.prototype.setEnabled = function(value) {
  return jspb.Message.setProto3BooleanField(this, 2, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.autokitteh.project.ProjectSettings.repeatedFields_ = [6];



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
proto.autokitteh.project.ProjectSettings.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.project.ProjectSettings.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.project.ProjectSettings} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.ProjectSettings.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getFieldWithDefault(msg, 1, ""),
    enabled: jspb.Message.getBooleanFieldWithDefault(msg, 2, false),
    mainPath: (f = msg.getMainPath()) && program_program_pb.Path.toObject(includeInstance, f),
    predeclsMap: (f = msg.getPredeclsMap()) ? f.toObject(includeInstance, proto.autokitteh.values.Value.toObject) : [],
    pluginsList: jspb.Message.toObjectList(msg.getPluginsList(),
    proto.autokitteh.project.ProjectPlugin.toObject, includeInstance),
    memoMap: (f = msg.getMemoMap()) ? f.toObject(includeInstance, undefined) : []
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
 * @return {!proto.autokitteh.project.ProjectSettings}
 */
proto.autokitteh.project.ProjectSettings.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.project.ProjectSettings;
  return proto.autokitteh.project.ProjectSettings.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.project.ProjectSettings} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.project.ProjectSettings}
 */
proto.autokitteh.project.ProjectSettings.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 2:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setEnabled(value);
      break;
    case 3:
      var value = new program_program_pb.Path;
      reader.readMessage(value,program_program_pb.Path.deserializeBinaryFromReader);
      msg.setMainPath(value);
      break;
    case 5:
      var value = msg.getPredeclsMap();
      reader.readMessage(value, function(message, reader) {
        jspb.Map.deserializeBinary(message, reader, jspb.BinaryReader.prototype.readString, jspb.BinaryReader.prototype.readMessage, proto.autokitteh.values.Value.deserializeBinaryFromReader, "", new proto.autokitteh.values.Value());
         });
      break;
    case 6:
      var value = new proto.autokitteh.project.ProjectPlugin;
      reader.readMessage(value,proto.autokitteh.project.ProjectPlugin.deserializeBinaryFromReader);
      msg.addPlugins(value);
      break;
    case 50:
      var value = msg.getMemoMap();
      reader.readMessage(value, function(message, reader) {
        jspb.Map.deserializeBinary(message, reader, jspb.BinaryReader.prototype.readString, jspb.BinaryReader.prototype.readString, null, "", "");
         });
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
proto.autokitteh.project.ProjectSettings.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.project.ProjectSettings.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.project.ProjectSettings} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.ProjectSettings.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getEnabled();
  if (f) {
    writer.writeBool(
      2,
      f
    );
  }
  f = message.getMainPath();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      program_program_pb.Path.serializeBinaryToWriter
    );
  }
  f = message.getPredeclsMap(true);
  if (f && f.getLength() > 0) {
    f.serializeBinary(5, writer, jspb.BinaryWriter.prototype.writeString, jspb.BinaryWriter.prototype.writeMessage, proto.autokitteh.values.Value.serializeBinaryToWriter);
  }
  f = message.getPluginsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      proto.autokitteh.project.ProjectPlugin.serializeBinaryToWriter
    );
  }
  f = message.getMemoMap(true);
  if (f && f.getLength() > 0) {
    f.serializeBinary(50, writer, jspb.BinaryWriter.prototype.writeString, jspb.BinaryWriter.prototype.writeString);
  }
};


/**
 * optional string name = 1;
 * @return {string}
 */
proto.autokitteh.project.ProjectSettings.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional bool enabled = 2;
 * @return {boolean}
 */
proto.autokitteh.project.ProjectSettings.prototype.getEnabled = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 2, false));
};


/**
 * @param {boolean} value
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.setEnabled = function(value) {
  return jspb.Message.setProto3BooleanField(this, 2, value);
};


/**
 * optional autokitteh.program.Path main_path = 3;
 * @return {?proto.autokitteh.program.Path}
 */
proto.autokitteh.project.ProjectSettings.prototype.getMainPath = function() {
  return /** @type{?proto.autokitteh.program.Path} */ (
    jspb.Message.getWrapperField(this, program_program_pb.Path, 3));
};


/**
 * @param {?proto.autokitteh.program.Path|undefined} value
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
*/
proto.autokitteh.project.ProjectSettings.prototype.setMainPath = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.clearMainPath = function() {
  return this.setMainPath(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.project.ProjectSettings.prototype.hasMainPath = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * map<string, autokitteh.values.Value> predecls = 5;
 * @param {boolean=} opt_noLazyCreate Do not create the map if
 * empty, instead returning `undefined`
 * @return {!jspb.Map<string,!proto.autokitteh.values.Value>}
 */
proto.autokitteh.project.ProjectSettings.prototype.getPredeclsMap = function(opt_noLazyCreate) {
  return /** @type {!jspb.Map<string,!proto.autokitteh.values.Value>} */ (
      jspb.Message.getMapField(this, 5, opt_noLazyCreate,
      proto.autokitteh.values.Value));
};


/**
 * Clears values from the map. The map will be non-null.
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.clearPredeclsMap = function() {
  this.getPredeclsMap().clear();
  return this;};


/**
 * repeated ProjectPlugin plugins = 6;
 * @return {!Array<!proto.autokitteh.project.ProjectPlugin>}
 */
proto.autokitteh.project.ProjectSettings.prototype.getPluginsList = function() {
  return /** @type{!Array<!proto.autokitteh.project.ProjectPlugin>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.autokitteh.project.ProjectPlugin, 6));
};


/**
 * @param {!Array<!proto.autokitteh.project.ProjectPlugin>} value
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
*/
proto.autokitteh.project.ProjectSettings.prototype.setPluginsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.autokitteh.project.ProjectPlugin=} opt_value
 * @param {number=} opt_index
 * @return {!proto.autokitteh.project.ProjectPlugin}
 */
proto.autokitteh.project.ProjectSettings.prototype.addPlugins = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.autokitteh.project.ProjectPlugin, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.clearPluginsList = function() {
  return this.setPluginsList([]);
};


/**
 * map<string, string> memo = 50;
 * @param {boolean=} opt_noLazyCreate Do not create the map if
 * empty, instead returning `undefined`
 * @return {!jspb.Map<string,string>}
 */
proto.autokitteh.project.ProjectSettings.prototype.getMemoMap = function(opt_noLazyCreate) {
  return /** @type {!jspb.Map<string,string>} */ (
      jspb.Message.getMapField(this, 50, opt_noLazyCreate,
      null));
};


/**
 * Clears values from the map. The map will be non-null.
 * @return {!proto.autokitteh.project.ProjectSettings} returns this
 */
proto.autokitteh.project.ProjectSettings.prototype.clearMemoMap = function() {
  this.getMemoMap().clear();
  return this;};





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
proto.autokitteh.project.Project.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.project.Project.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.project.Project} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.Project.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    accountName: jspb.Message.getFieldWithDefault(msg, 2, ""),
    settings: (f = msg.getSettings()) && proto.autokitteh.project.ProjectSettings.toObject(includeInstance, f),
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
 * @return {!proto.autokitteh.project.Project}
 */
proto.autokitteh.project.Project.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.project.Project;
  return proto.autokitteh.project.Project.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.project.Project} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.project.Project}
 */
proto.autokitteh.project.Project.deserializeBinaryFromReader = function(msg, reader) {
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
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setAccountName(value);
      break;
    case 3:
      var value = new proto.autokitteh.project.ProjectSettings;
      reader.readMessage(value,proto.autokitteh.project.ProjectSettings.deserializeBinaryFromReader);
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
proto.autokitteh.project.Project.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.project.Project.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.project.Project} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.project.Project.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getAccountName();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getSettings();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      proto.autokitteh.project.ProjectSettings.serializeBinaryToWriter
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
proto.autokitteh.project.Project.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.project.Project} returns this
 */
proto.autokitteh.project.Project.prototype.setId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string account_name = 2;
 * @return {string}
 */
proto.autokitteh.project.Project.prototype.getAccountName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.project.Project} returns this
 */
proto.autokitteh.project.Project.prototype.setAccountName = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional ProjectSettings settings = 3;
 * @return {?proto.autokitteh.project.ProjectSettings}
 */
proto.autokitteh.project.Project.prototype.getSettings = function() {
  return /** @type{?proto.autokitteh.project.ProjectSettings} */ (
    jspb.Message.getWrapperField(this, proto.autokitteh.project.ProjectSettings, 3));
};


/**
 * @param {?proto.autokitteh.project.ProjectSettings|undefined} value
 * @return {!proto.autokitteh.project.Project} returns this
*/
proto.autokitteh.project.Project.prototype.setSettings = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.project.Project} returns this
 */
proto.autokitteh.project.Project.prototype.clearSettings = function() {
  return this.setSettings(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.project.Project.prototype.hasSettings = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp created_at = 100;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.project.Project.prototype.getCreatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 100));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.project.Project} returns this
*/
proto.autokitteh.project.Project.prototype.setCreatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 100, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.project.Project} returns this
 */
proto.autokitteh.project.Project.prototype.clearCreatedAt = function() {
  return this.setCreatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.project.Project.prototype.hasCreatedAt = function() {
  return jspb.Message.getField(this, 100) != null;
};


/**
 * optional google.protobuf.Timestamp updated_at = 101;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.autokitteh.project.Project.prototype.getUpdatedAt = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 101));
};


/**
 * @param {?proto.google.protobuf.Timestamp|undefined} value
 * @return {!proto.autokitteh.project.Project} returns this
*/
proto.autokitteh.project.Project.prototype.setUpdatedAt = function(value) {
  return jspb.Message.setWrapperField(this, 101, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.autokitteh.project.Project} returns this
 */
proto.autokitteh.project.Project.prototype.clearUpdatedAt = function() {
  return this.setUpdatedAt(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.autokitteh.project.Project.prototype.hasUpdatedAt = function() {
  return jspb.Message.getField(this, 101) != null;
};


goog.object.extend(exports, proto.autokitteh.project);
