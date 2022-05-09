import hydra
import logging
import logging.config
import yaml
from predictor.entities.config import Config, register_configs

register_configs()


def setup_logging(logging_yaml_config_fpath):
    """setup logging via YAML if it is provided"""
    if logging_yaml_config_fpath:
        with open(logging_yaml_config_fpath) as config_fin:
            logging.config.dictConfig(yaml.safe_load(config_fin))


@hydra.main(config_path="configs/", config_name="train.yaml")
def main(config: Config):
    from predictor.engine.trainer import train
    setup_logging(config.default_logger)
    return train(config)


if __name__ == "__main__":
    main()
