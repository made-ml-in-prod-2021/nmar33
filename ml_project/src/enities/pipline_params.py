from dataclasses import dataclass, MISSING
from marshmallow_dataclass import class_schema
import yaml



@dataclass
class PathsConfig:
    raw_dataset_path: str = MISSING
    train_dataset_path: str = MISSING
    test_dataset_path: str = MISSING
    predict_dataset_path: str = MISSING
    output_model_path: str = MISSING
    metric_path: str = MISSING
    predict_path: str = MISSING
    log_path: str = MISSING


@dataclass
class TrainConfig:
    model_type: str = MISSING
    test_size: float = MISSING
    random_state: int = MISSING


@dataclass
class LogConfig:
    formatter_config: dict = MISSING
    logging_level: int = MISSING


@dataclass
class PiplineParams:
    paths: PathsConfig
    train_config: TrainConfig
    log_config: LogConfig


PipelineParamsSchema = class_schema(PiplineParams)


def read_configs(path: str) -> PiplineParams:
    with open(path, 'r') as config_file:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(config_file))


def main():
    pass


if __name__ == 'main':
    main()