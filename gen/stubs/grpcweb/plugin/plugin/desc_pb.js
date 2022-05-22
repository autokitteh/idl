// source: plugin/desc.proto
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

var validate_validate_pb = require('../validate/validate_pb.js');
goog.object.extend(proto, validate_validate_pb);
goog.exportSymbol('proto.autokitteh.plugin.PluginDesc', null, global);
goog.exportSymbol('proto.autokitteh.plugin.PluginMemberDesc', null, global);
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
proto.autokitteh.plugin.PluginMemberDesc = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.autokitteh.plugin.PluginMemberDesc, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.plugin.PluginMemberDesc.displayName = 'proto.autokitteh.plugin.PluginMemberDesc';
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
proto.autokitteh.plugin.PluginDesc = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.autokitteh.plugin.PluginDesc.repeatedFields_, null);
};
goog.inherits(proto.autokitteh.plugin.PluginDesc, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.autokitteh.plugin.PluginDesc.displayName = 'proto.autokitteh.plugin.PluginDesc';
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
proto.autokitteh.plugin.PluginMemberDesc.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.plugin.PluginMemberDesc.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.plugin.PluginMemberDesc} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.plugin.PluginMemberDesc.toObject = function(includeInstance, msg) {
  var f, obj = {
    name: jspb.Message.getFieldWithDefault(msg, 1, ""),
    doc: jspb.Message.getFieldWithDefault(msg, 2, "")
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
 * @return {!proto.autokitteh.plugin.PluginMemberDesc}
 */
proto.autokitteh.plugin.PluginMemberDesc.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.plugin.PluginMemberDesc;
  return proto.autokitteh.plugin.PluginMemberDesc.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.plugin.PluginMemberDesc} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.plugin.PluginMemberDesc}
 */
proto.autokitteh.plugin.PluginMemberDesc.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = /** @type {string} */ (reader.readString());
      msg.setDoc(value);
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
proto.autokitteh.plugin.PluginMemberDesc.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.plugin.PluginMemberDesc.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.plugin.PluginMemberDesc} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.plugin.PluginMemberDesc.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getDoc();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
};


/**
 * optional string name = 1;
 * @return {string}
 */
proto.autokitteh.plugin.PluginMemberDesc.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.plugin.PluginMemberDesc} returns this
 */
proto.autokitteh.plugin.PluginMemberDesc.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional string doc = 2;
 * @return {string}
 */
proto.autokitteh.plugin.PluginMemberDesc.prototype.getDoc = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.plugin.PluginMemberDesc} returns this
 */
proto.autokitteh.plugin.PluginMemberDesc.prototype.setDoc = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.autokitteh.plugin.PluginDesc.repeatedFields_ = [2];



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
proto.autokitteh.plugin.PluginDesc.prototype.toObject = function(opt_includeInstance) {
  return proto.autokitteh.plugin.PluginDesc.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.autokitteh.plugin.PluginDesc} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.plugin.PluginDesc.toObject = function(includeInstance, msg) {
  var f, obj = {
    doc: jspb.Message.getFieldWithDefault(msg, 1, ""),
    membersList: jspb.Message.toObjectList(msg.getMembersList(),
    proto.autokitteh.plugin.PluginMemberDesc.toObject, includeInstance)
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
 * @return {!proto.autokitteh.plugin.PluginDesc}
 */
proto.autokitteh.plugin.PluginDesc.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.autokitteh.plugin.PluginDesc;
  return proto.autokitteh.plugin.PluginDesc.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.autokitteh.plugin.PluginDesc} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.autokitteh.plugin.PluginDesc}
 */
proto.autokitteh.plugin.PluginDesc.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setDoc(value);
      break;
    case 2:
      var value = new proto.autokitteh.plugin.PluginMemberDesc;
      reader.readMessage(value,proto.autokitteh.plugin.PluginMemberDesc.deserializeBinaryFromReader);
      msg.addMembers(value);
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
proto.autokitteh.plugin.PluginDesc.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.autokitteh.plugin.PluginDesc.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.autokitteh.plugin.PluginDesc} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.autokitteh.plugin.PluginDesc.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getDoc();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getMembersList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      proto.autokitteh.plugin.PluginMemberDesc.serializeBinaryToWriter
    );
  }
};


/**
 * optional string doc = 1;
 * @return {string}
 */
proto.autokitteh.plugin.PluginDesc.prototype.getDoc = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.autokitteh.plugin.PluginDesc} returns this
 */
proto.autokitteh.plugin.PluginDesc.prototype.setDoc = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * repeated PluginMemberDesc members = 2;
 * @return {!Array<!proto.autokitteh.plugin.PluginMemberDesc>}
 */
proto.autokitteh.plugin.PluginDesc.prototype.getMembersList = function() {
  return /** @type{!Array<!proto.autokitteh.plugin.PluginMemberDesc>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.autokitteh.plugin.PluginMemberDesc, 2));
};


/**
 * @param {!Array<!proto.autokitteh.plugin.PluginMemberDesc>} value
 * @return {!proto.autokitteh.plugin.PluginDesc} returns this
*/
proto.autokitteh.plugin.PluginDesc.prototype.setMembersList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.autokitteh.plugin.PluginMemberDesc=} opt_value
 * @param {number=} opt_index
 * @return {!proto.autokitteh.plugin.PluginMemberDesc}
 */
proto.autokitteh.plugin.PluginDesc.prototype.addMembers = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.autokitteh.plugin.PluginMemberDesc, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.autokitteh.plugin.PluginDesc} returns this
 */
proto.autokitteh.plugin.PluginDesc.prototype.clearMembersList = function() {
  return this.setMembersList([]);
};


goog.object.extend(exports, proto.autokitteh.plugin);
