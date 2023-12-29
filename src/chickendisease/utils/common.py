"""module for common utility functions"""

import base64
import json
import os
from pathlib import Path
from typing import Any

import joblib
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from chickendisease import logger


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Read YAML file and return a Box object.

    :param path: Path to YAML file.
    :return: Box object.
    """

    try:
        with open(path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Loaded YAML file from {path}')
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f'Error reading YAML file from {path}')
    except Exception as e:
        raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save data as JSON file.

    :param path: Path to save JSON file.
    :param data: Data to save.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f'Saved JSON file to {path}')
    except Exception as e:
        raise e


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON file.

    :param path: Path to JSON file.
    :return: Loaded JSON file as ConfigBox class.
    """

    try:
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f'Loaded JSON file from {path}')
            return ConfigBox(data)
    except Exception as e:
        raise e


@ensure_annotations
def save_binary(path: Path, data: Any) -> None:
    """
    Save data as binary file.

    :param path: Path to save binary file.
    :param data: Data to save.
    """

    try:
        with open(path, 'wb') as binary_file:
            joblib.dump(data, binary_file)
            logger.info(f'Saved binary file to {path}')
    except Exception as e:
        raise e


@ensure_annotations
def load_binary(path: Path) -> Any:
    """
    Load binary file.

    :param path: Path to binary file.
    :return: Loaded binary file.
    """

    try:
        data = joblib.load(path)
        logger.info(f'Loaded binary file from {path}')
        return data
    except Exception as e:
        raise e


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get file size in KB.

    :param path: Path to file.
    :return: File size in KB.
    """

    try:
        size = round(os.path.getsize(path) / 1000)
        return f'~ {size} KB'
    except Exception as e:
        raise e


def decode_image(img_string: str, file_name: str) -> None:
    """
    Decode image string and save as image file.

    :param img_string: Image string.
    :param file_name: Name of image file.
    """

    try:
        img_data = base64.b64decode(img_string)
        with open(file_name, 'wb') as f:
            f.write(img_data)
            f.close()
    except Exception as e:
        raise e


def encode_image(file_name: str) -> str:
    """
    Encode image file as string.

    :param file_name: Name of image file.
    :return: Image string.
    """

    try:
        with open(file_name, 'rb') as f:
            img_string = base64.b64encode(f.read())
            f.close()
            return img_string
    except Exception as e:
        raise e


def make_dir(dirs_path_list: list, verbose=True) -> None:
    """
    Make directories.

    :param dirs: List of directories to make.
    """

    try:
        for dir in dirs_path_list:
            os.makedirs(dir, exist_ok=True)
            if verbose:
                logger.info(f'Created directory at {dir}')
    except Exception as e:
        raise e
