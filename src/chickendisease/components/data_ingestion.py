"""Data Ingestion Component"""

import os
import urllib.request as request
import zipfile
from pathlib import Path

from chickendisease import logger
from chickendisease.entity.config_entity import DataIngestionConfig
from chickendisease.utils.common import get_size


class DataIngestion:
    """Data Ingestion Class"""

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> None:
        """
        Download data from source URL.
        """

        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(url=self.config.source_URL, filename=self.config.local_data_file)
            logger.info(f'downloaded data: {file_name} with the following info: {headers}')
        else:
            logger.info(f'data already exists of size {get_size(Path(self.config.local_data_file))}')

    def unzip_data(self) -> None:
        """
        Unzip data.
        """

        unzip_path = self.config.root_dir
        if not os.path.exists(unzip_path):
            os.makedirs(unzip_path)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'unzipped data to {unzip_path}')
