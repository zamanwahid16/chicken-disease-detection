"""Entity module for config."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """Data Ingestion Config Entity Class"""
    root_dir: Path
    source_URL: str
    local_data_file: Path


@dataclass(frozen=True)
class BaseModelConfig:
    """Base Model Config Entity Class"""
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class CallbacksConfig:
    """Callbacks Config Entity Class"""
    root_dir: Path
    tensorboard_logs_dir: Path
    checkpoint_model_path: Path


@dataclass(frozen=True)
class TrainingConfig:
    """Training Config Entity Class"""
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augment: bool
    params_image_size: list
