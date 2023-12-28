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
