/**
 * @fileoverview gRPC-Web generated client stub for autokitteh.litterbox
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');


var google_api_annotations_pb = require('../google/api/annotations_pb.js')

var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js')

var validate_validate_pb = require('../validate/validate_pb.js')

var lang_run_pb = require('../lang/run_pb.js')

var values_values_pb = require('../values/values_pb.js')
const proto = {};
proto.autokitteh = {};
proto.autokitteh.litterbox = require('./svc_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.autokitteh.litterbox.LitterBoxClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.autokitteh.litterbox.LitterBoxPromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname;

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.autokitteh.litterbox.RunRequest,
 *   !proto.autokitteh.litterbox.RunUpdate>}
 */
const methodDescriptor_LitterBox_Run = new grpc.web.MethodDescriptor(
  '/autokitteh.litterbox.LitterBox/Run',
  grpc.web.MethodType.SERVER_STREAMING,
  proto.autokitteh.litterbox.RunRequest,
  proto.autokitteh.litterbox.RunUpdate,
  /**
   * @param {!proto.autokitteh.litterbox.RunRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.autokitteh.litterbox.RunUpdate.deserializeBinary
);


/**
 * @param {!proto.autokitteh.litterbox.RunRequest} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.autokitteh.litterbox.RunUpdate>}
 *     The XHR Node Readable Stream
 */
proto.autokitteh.litterbox.LitterBoxClient.prototype.run =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Run',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Run);
};


/**
 * @param {!proto.autokitteh.litterbox.RunRequest} request The request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!grpc.web.ClientReadableStream<!proto.autokitteh.litterbox.RunUpdate>}
 *     The XHR Node Readable Stream
 */
proto.autokitteh.litterbox.LitterBoxPromiseClient.prototype.run =
    function(request, metadata) {
  return this.client_.serverStreaming(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Run',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Run);
};


module.exports = proto.autokitteh.litterbox;

