# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import msg_pb2 as msg__pb2


class MessageServiceStub(object):
  """Service definition
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMessage = channel.unary_unary(
        '/MessageService/GetMessage',
        request_serializer=msg__pb2.GetMessageRequest.SerializeToString,
        response_deserializer=msg__pb2.MessageResponse.FromString,
        )
    self.PutMessage = channel.unary_unary(
        '/MessageService/PutMessage',
        request_serializer=msg__pb2.PutMessageRequest.SerializeToString,
        response_deserializer=msg__pb2.Status.FromString,
        )
    self.MessageCheck = channel.unary_unary(
        '/MessageService/MessageCheck',
        request_serializer=msg__pb2.CheckRequest.SerializeToString,
        response_deserializer=msg__pb2.CheckResponse.FromString,
        )
    self.GetJob = channel.unary_unary(
        '/MessageService/GetJob',
        request_serializer=msg__pb2.GetJobRequest.SerializeToString,
        response_deserializer=msg__pb2.JobResponse.FromString,
        )
    self.PutJob = channel.unary_unary(
        '/MessageService/PutJob',
        request_serializer=msg__pb2.PutJobRequest.SerializeToString,
        response_deserializer=msg__pb2.Status.FromString,
        )
    self.JobCheck = channel.unary_unary(
        '/MessageService/JobCheck',
        request_serializer=msg__pb2.CheckRequest.SerializeToString,
        response_deserializer=msg__pb2.CheckResponse.FromString,
        )
    self.PurgeQueues = channel.unary_unary(
        '/MessageService/PurgeQueues',
        request_serializer=msg__pb2.BasicRequest.SerializeToString,
        response_deserializer=msg__pb2.Status.FromString,
        )


class MessageServiceServicer(object):
  """Service definition
  """

  def GetMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MessageCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PutJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def JobCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PurgeQueues(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMessage': grpc.unary_unary_rpc_method_handler(
          servicer.GetMessage,
          request_deserializer=msg__pb2.GetMessageRequest.FromString,
          response_serializer=msg__pb2.MessageResponse.SerializeToString,
      ),
      'PutMessage': grpc.unary_unary_rpc_method_handler(
          servicer.PutMessage,
          request_deserializer=msg__pb2.PutMessageRequest.FromString,
          response_serializer=msg__pb2.Status.SerializeToString,
      ),
      'MessageCheck': grpc.unary_unary_rpc_method_handler(
          servicer.MessageCheck,
          request_deserializer=msg__pb2.CheckRequest.FromString,
          response_serializer=msg__pb2.CheckResponse.SerializeToString,
      ),
      'GetJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=msg__pb2.GetJobRequest.FromString,
          response_serializer=msg__pb2.JobResponse.SerializeToString,
      ),
      'PutJob': grpc.unary_unary_rpc_method_handler(
          servicer.PutJob,
          request_deserializer=msg__pb2.PutJobRequest.FromString,
          response_serializer=msg__pb2.Status.SerializeToString,
      ),
      'JobCheck': grpc.unary_unary_rpc_method_handler(
          servicer.JobCheck,
          request_deserializer=msg__pb2.CheckRequest.FromString,
          response_serializer=msg__pb2.CheckResponse.SerializeToString,
      ),
      'PurgeQueues': grpc.unary_unary_rpc_method_handler(
          servicer.PurgeQueues,
          request_deserializer=msg__pb2.BasicRequest.FromString,
          response_serializer=msg__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MessageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
