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
 *   !proto.autokitteh.litterbox.SetupRequest,
 *   !proto.autokitteh.litterbox.SetupResponse>}
 */
const methodDescriptor_LitterBox_Setup = new grpc.web.MethodDescriptor(
  '/autokitteh.litterbox.LitterBox/Setup',
  grpc.web.MethodType.UNARY,
  proto.autokitteh.litterbox.SetupRequest,
  proto.autokitteh.litterbox.SetupResponse,
  /**
   * @param {!proto.autokitteh.litterbox.SetupRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.autokitteh.litterbox.SetupResponse.deserializeBinary
);


/**
 * @param {!proto.autokitteh.litterbox.SetupRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.autokitteh.litterbox.SetupResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.autokitteh.litterbox.SetupResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.autokitteh.litterbox.LitterBoxClient.prototype.setup =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Setup',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Setup,
      callback);
};


/**
 * @param {!proto.autokitteh.litterbox.SetupRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.autokitteh.litterbox.SetupResponse>}
 *     Promise that resolves to the response
 */
proto.autokitteh.litterbox.LitterBoxPromiseClient.prototype.setup =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Setup',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Setup);
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


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.autokitteh.litterbox.ScoopRequest,
 *   !proto.autokitteh.litterbox.ScoopResponse>}
 */
const methodDescriptor_LitterBox_Scoop = new grpc.web.MethodDescriptor(
  '/autokitteh.litterbox.LitterBox/Scoop',
  grpc.web.MethodType.UNARY,
  proto.autokitteh.litterbox.ScoopRequest,
  proto.autokitteh.litterbox.ScoopResponse,
  /**
   * @param {!proto.autokitteh.litterbox.ScoopRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.autokitteh.litterbox.ScoopResponse.deserializeBinary
);


/**
 * @param {!proto.autokitteh.litterbox.ScoopRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.autokitteh.litterbox.ScoopResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.autokitteh.litterbox.ScoopResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.autokitteh.litterbox.LitterBoxClient.prototype.scoop =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Scoop',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Scoop,
      callback);
};


/**
 * @param {!proto.autokitteh.litterbox.ScoopRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.autokitteh.litterbox.ScoopResponse>}
 *     Promise that resolves to the response
 */
proto.autokitteh.litterbox.LitterBoxPromiseClient.prototype.scoop =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/autokitteh.litterbox.LitterBox/Scoop',
      request,
      metadata || {},
      methodDescriptor_LitterBox_Scoop);
};


module.exports = proto.autokitteh.litterbox;

