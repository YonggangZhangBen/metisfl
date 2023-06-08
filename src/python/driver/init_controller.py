import argparse

import src.proto.metis_pb2 as metis_pb2

from src.python.utils.metis_logger import MetisLogger
from src.python.utils.proto_messages_factory import MetisProtoMessages, ModelProtoMessages
from pybind.controller.controller_instance import ControllerInstance

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--controller_hostname", type=str,
                        default="[::]",
                        help="Controller binding hostname.")
    parser.add_argument("-p", "--controller_port", type=int,
                        default=50051,
                        help="Controller binding port.")
    parser.add_argument("-g", "--global_model_specs_protobuff_serialized_hexadecimal", type=str,
                        default=None,
                        help="local models aggregation_rule (i.e, merging function) to create global model.")
    parser.add_argument("-c", "--communication_specs_protobuff_serialized_hexadecimal", type=str,
                        default=None,
                        help="what is the communication protocol for aggregating local models "
                             "(i.e., synchronous, asynchronous, semi_synchronous) and its specifications.")
    parser.add_argument("-m", "--model_hyperparameters_protobuff_serialized_hexadecimal", type=str,
                        default=None,
                        help="A serialized Model Hyperparameters protobuf message.")
    parser.add_argument("-s", "--model_store_config_protobuff_serialized_hexadecimal", type=str,
                        default=None,
                        help="A serialized Model Store Config protobuf message.")
    args = parser.parse_args()

    controller_hostname = args.controller_hostname
    controller_port = args.controller_port

    # Parse serialized model hyperparameters object, 'recover' bytes object.
    # To do so, we need to convert the incoming hexadecimal representation
    # to bytes and pass it as initialization to the proto message object.
    # If the given protobuff is None then we assign it an empty bytes object.

    # Use parsed protobuff to initialize Metis.CommunicationSpecs() object.
    if args.global_model_specs_protobuff_serialized_hexadecimal is not None:
        global_model_specs_protobuff_ser = bytes.fromhex(args.global_model_specs_protobuff_serialized_hexadecimal)
        global_model_specs = metis_pb2.GlobalModelSpecs()
        global_model_specs.ParseFromString(global_model_specs_protobuff_ser)
    else:
        aggregation_rule_pb = MetisProtoMessages.construct_aggregation_rule_pb(rule_name="FEDAVG",
                                                                               scaling_factor="NUMTRAININGEXAMPLES",
                                                                               stride_length=None,
                                                                               fhe_scheme_pb=None)
        global_model_specs = MetisProtoMessages.construct_global_model_specs(aggregation_rule_pb=aggregation_rule_pb,
                                                                             learners_participation_ratio=1)

    # Use parsed protobuff to initialize Metis.CommunicationSpecs() object.
    if args.communication_specs_protobuff_serialized_hexadecimal is not None:
        communication_specs_protobuff_ser = bytes.fromhex(args.communication_specs_protobuff_serialized_hexadecimal)
        communication_specs = metis_pb2.CommunicationSpecs()
        communication_specs.ParseFromString(communication_specs_protobuff_ser)
    else:
        communication_specs = MetisProtoMessages.construct_communication_specs_pb(protocol="SYNCHRONOUS",
                                                                                  semi_sync_lambda=None,
                                                                                  semi_sync_recompute_num_updates=None)

    # Use parsed protobuff to initialize ControllerParams.ModelHyperparams() object.
    if args.model_hyperparameters_protobuff_serialized_hexadecimal is not None:
        model_hyperparameters_protobuff_ser = bytes.fromhex(args.model_hyperparameters_protobuff_serialized_hexadecimal)
        model_hyperparams = metis_pb2.ControllerParams.ModelHyperparams()
        model_hyperparams.ParseFromString(model_hyperparameters_protobuff_ser)
    else:
        model_hyperparams = MetisProtoMessages.construct_controller_modelhyperparams_pb(
            batch_size=100, epochs=5, percent_validation=0.0,
            optimizer_pb=ModelProtoMessages.construct_optimizer_config_pb(
                ModelProtoMessages.construct_vanilla_sgd_optimizer_pb(learning_rate=0.01)))

    # Use parsed protobuff to initialize Metis.ModelStoreConfig() object.
    if args.model_store_config_protobuff_serialized_hexadecimal is not None:
        model_store_config_protobuff_ser = bytes.fromhex(args.model_store_config_protobuff_serialized_hexadecimal)
        model_store_config = metis_pb2.ModelStoreConfig()
        model_store_config.ParseFromString(model_store_config_protobuff_ser)
    else:
        # Default is the in-memory store without any model eviction.
        model_store_config = MetisProtoMessages.construct_model_store_config_pb(
            name="InMemory",
            eviction_policy="NoEviction")

    controller_params = metis_pb2.ControllerParams(
        server_entity=metis_pb2.ServerEntity(
            hostname=controller_hostname,
            port=controller_port),
        global_model_specs=global_model_specs,
        communication_specs=communication_specs,
        model_store_config=model_store_config,
        model_hyperparams=model_hyperparams)

    MetisLogger.info("Controller Parameters: \"\"\"{}\"\"\"".format(controller_params))
    controller_instance = ControllerInstance()
    controller_instance.build_and_start(controller_params)

    controller_instance.wait()
