"""Configuration for the project."""

from chickendisease.constants import *
from chickendisease.entity.config_entity import (BaseModelConfig,
                                                 DataIngestionConfig)
from chickendisease.utils.common import make_dir, read_yaml


class ConfigurationManager:
    """Reads the configuration from config.yaml and params.yaml files."""

    def __init__(
            self,
            config_file_path=CONFIG_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        make_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Returns the DataIngestionConfig object."""
        config = self.config.data_ingestion
        make_dir([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file
        )
        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:
        """Returns the BaseModelConfig object."""
        config = self.config.base_model
        make_dir([config.root_dir])
        base_model_config = BaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        return base_model_config
