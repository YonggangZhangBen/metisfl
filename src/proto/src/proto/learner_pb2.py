# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/proto/learner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from src.proto import metis_pb2 as src_dot_proto_dot_metis__pb2
from src.proto import model_pb2 as src_dot_proto_dot_model__pb2
from src.proto import service_common_pb2 as src_dot_proto_dot_service__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/proto/learner.proto',
  package='projectmetis',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17src/proto/learner.proto\x12\x0cprojectmetis\x1a\x15src/proto/metis.proto\x1a\x15src/proto/model.proto\x1a\x1esrc/proto/service_common.proto\"\xb9\x02\n\x14\x45valuateModelRequest\x12)\n\x05model\x18\x01 \x01(\x0b\x32\x13.projectmetis.ModelR\x05model\x12\x1d\n\nbatch_size\x18\x02 \x01(\rR\tbatchSize\x12\x61\n\x12\x65valuation_dataset\x18\x03 \x03(\x0e\x32\x32.projectmetis.EvaluateModelRequest.dataset_to_evalR\x11\x65valuationDataset\x12\x39\n\x07metrics\x18\x04 \x01(\x0b\x32\x1f.projectmetis.EvaluationMetricsR\x07metrics\"9\n\x0f\x64\x61taset_to_eval\x12\x0c\n\x08TRAINING\x10\x00\x12\x08\n\x04TEST\x10\x01\x12\x0e\n\nVALIDATION\x10\x02\"Y\n\x15\x45valuateModelResponse\x12@\n\x0b\x65valuations\x18\x01 \x01(\x0b\x32\x1e.projectmetis.ModelEvaluationsR\x0b\x65valuations\"\xd0\x01\n\x0eRunTaskRequest\x12\x45\n\x0f\x66\x65\x64\x65rated_model\x18\x01 \x01(\x0b\x32\x1c.projectmetis.FederatedModelR\x0e\x66\x65\x64\x65ratedModel\x12.\n\x04task\x18\x02 \x01(\x0b\x32\x1a.projectmetis.LearningTaskR\x04task\x12G\n\x0fhyperparameters\x18\x03 \x01(\x0b\x32\x1d.projectmetis.HyperparametersR\x0fhyperparameters\"6\n\x0fRunTaskResponse\x12#\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x11.projectmetis.AckR\x03\x61\x63k2\xfd\x02\n\x0eLearnerService\x12Z\n\rEvaluateModel\x12\".projectmetis.EvaluateModelRequest\x1a#.projectmetis.EvaluateModelResponse\"\x00\x12x\n\x17GetServicesHealthStatus\x12,.projectmetis.GetServicesHealthStatusRequest\x1a-.projectmetis.GetServicesHealthStatusResponse\"\x00\x12H\n\x07RunTask\x12\x1c.projectmetis.RunTaskRequest\x1a\x1d.projectmetis.RunTaskResponse\"\x00\x12K\n\x08ShutDown\x12\x1d.projectmetis.ShutDownRequest\x1a\x1e.projectmetis.ShutDownResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[src_dot_proto_dot_metis__pb2.DESCRIPTOR,src_dot_proto_dot_model__pb2.DESCRIPTOR,src_dot_proto_dot_service__common__pb2.DESCRIPTOR,])



_EVALUATEMODELREQUEST_DATASET_TO_EVAL = _descriptor.EnumDescriptor(
  name='dataset_to_eval',
  full_name='projectmetis.EvaluateModelRequest.dataset_to_eval',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALIDATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=376,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_EVALUATEMODELREQUEST_DATASET_TO_EVAL)


_EVALUATEMODELREQUEST = _descriptor.Descriptor(
  name='EvaluateModelRequest',
  full_name='projectmetis.EvaluateModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='projectmetis.EvaluateModelRequest.model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='model', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='projectmetis.EvaluateModelRequest.batch_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='batchSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evaluation_dataset', full_name='projectmetis.EvaluateModelRequest.evaluation_dataset', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluationDataset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='projectmetis.EvaluateModelRequest.metrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVALUATEMODELREQUEST_DATASET_TO_EVAL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=433,
)


_EVALUATEMODELRESPONSE = _descriptor.Descriptor(
  name='EvaluateModelResponse',
  full_name='projectmetis.EvaluateModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='evaluations', full_name='projectmetis.EvaluateModelResponse.evaluations', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='evaluations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=524,
)


_RUNTASKREQUEST = _descriptor.Descriptor(
  name='RunTaskRequest',
  full_name='projectmetis.RunTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='federated_model', full_name='projectmetis.RunTaskRequest.federated_model', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='federatedModel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='projectmetis.RunTaskRequest.task', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='task', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hyperparameters', full_name='projectmetis.RunTaskRequest.hyperparameters', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hyperparameters', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=735,
)


_RUNTASKRESPONSE = _descriptor.Descriptor(
  name='RunTaskResponse',
  full_name='projectmetis.RunTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='projectmetis.RunTaskResponse.ack', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ack', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=791,
)

_EVALUATEMODELREQUEST.fields_by_name['model'].message_type = src_dot_proto_dot_model__pb2._MODEL
_EVALUATEMODELREQUEST.fields_by_name['evaluation_dataset'].enum_type = _EVALUATEMODELREQUEST_DATASET_TO_EVAL
_EVALUATEMODELREQUEST.fields_by_name['metrics'].message_type = src_dot_proto_dot_metis__pb2._EVALUATIONMETRICS
_EVALUATEMODELREQUEST_DATASET_TO_EVAL.containing_type = _EVALUATEMODELREQUEST
_EVALUATEMODELRESPONSE.fields_by_name['evaluations'].message_type = src_dot_proto_dot_metis__pb2._MODELEVALUATIONS
_RUNTASKREQUEST.fields_by_name['federated_model'].message_type = src_dot_proto_dot_model__pb2._FEDERATEDMODEL
_RUNTASKREQUEST.fields_by_name['task'].message_type = src_dot_proto_dot_metis__pb2._LEARNINGTASK
_RUNTASKREQUEST.fields_by_name['hyperparameters'].message_type = src_dot_proto_dot_metis__pb2._HYPERPARAMETERS
_RUNTASKRESPONSE.fields_by_name['ack'].message_type = src_dot_proto_dot_service__common__pb2._ACK
DESCRIPTOR.message_types_by_name['EvaluateModelRequest'] = _EVALUATEMODELREQUEST
DESCRIPTOR.message_types_by_name['EvaluateModelResponse'] = _EVALUATEMODELRESPONSE
DESCRIPTOR.message_types_by_name['RunTaskRequest'] = _RUNTASKREQUEST
DESCRIPTOR.message_types_by_name['RunTaskResponse'] = _RUNTASKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvaluateModelRequest = _reflection.GeneratedProtocolMessageType('EvaluateModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEMODELREQUEST,
  '__module__' : 'src.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:projectmetis.EvaluateModelRequest)
  })
_sym_db.RegisterMessage(EvaluateModelRequest)

EvaluateModelResponse = _reflection.GeneratedProtocolMessageType('EvaluateModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVALUATEMODELRESPONSE,
  '__module__' : 'src.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:projectmetis.EvaluateModelResponse)
  })
_sym_db.RegisterMessage(EvaluateModelResponse)

RunTaskRequest = _reflection.GeneratedProtocolMessageType('RunTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNTASKREQUEST,
  '__module__' : 'src.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:projectmetis.RunTaskRequest)
  })
_sym_db.RegisterMessage(RunTaskRequest)

RunTaskResponse = _reflection.GeneratedProtocolMessageType('RunTaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTASKRESPONSE,
  '__module__' : 'src.proto.learner_pb2'
  # @@protoc_insertion_point(class_scope:projectmetis.RunTaskResponse)
  })
_sym_db.RegisterMessage(RunTaskResponse)



_LEARNERSERVICE = _descriptor.ServiceDescriptor(
  name='LearnerService',
  full_name='projectmetis.LearnerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=794,
  serialized_end=1175,
  methods=[
  _descriptor.MethodDescriptor(
    name='EvaluateModel',
    full_name='projectmetis.LearnerService.EvaluateModel',
    index=0,
    containing_service=None,
    input_type=_EVALUATEMODELREQUEST,
    output_type=_EVALUATEMODELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServicesHealthStatus',
    full_name='projectmetis.LearnerService.GetServicesHealthStatus',
    index=1,
    containing_service=None,
    input_type=src_dot_proto_dot_service__common__pb2._GETSERVICESHEALTHSTATUSREQUEST,
    output_type=src_dot_proto_dot_service__common__pb2._GETSERVICESHEALTHSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunTask',
    full_name='projectmetis.LearnerService.RunTask',
    index=2,
    containing_service=None,
    input_type=_RUNTASKREQUEST,
    output_type=_RUNTASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ShutDown',
    full_name='projectmetis.LearnerService.ShutDown',
    index=3,
    containing_service=None,
    input_type=src_dot_proto_dot_service__common__pb2._SHUTDOWNREQUEST,
    output_type=src_dot_proto_dot_service__common__pb2._SHUTDOWNRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEARNERSERVICE)

DESCRIPTOR.services_by_name['LearnerService'] = _LEARNERSERVICE

# @@protoc_insertion_point(module_scope)
