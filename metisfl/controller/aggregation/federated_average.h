
#ifndef METISFL_METISFL_CONTROLLER_AGGREGATION_FEDERATED_AVERAGE_H_
#define METISFL_METISFL_CONTROLLER_AGGREGATION_FEDERATED_AVERAGE_H_

#include "metisfl/controller/aggregation/aggregation_function.h"
#include "metisfl/proto/model.pb.h"

namespace metisfl::controller {

class FederatedAverage : public AggregationFunction {
 public:
  FederatedModel Aggregate(std::vector<std::vector<std::pair<const Model*, double>>>& pairs) override;

  [[nodiscard]] inline std::string Name() const override {
    return "FedAvg";
  }

  [[nodiscard]] inline int RequiredLearnerLineageLength() const override {
    return 1;
  }

  void Reset() override;

};

} // namespace metisfl::controller

#endif //METISFL_METISFL_CONTROLLER_AGGREGATION_FEDERATED_AVERAGE_H_
