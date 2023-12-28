""" Data Ingestion Pipeline """

from chickendisease import logger
from chickendisease.components.data_ingestion import DataIngestion
from chickendisease.config.configuration import ConfigurationManager

STAGE_NAME = 'Data Ingestion'


class DataIngestionPipeline:
    """Data Ingestion Pipeline Class"""

    def __init__(self):
        pass

    def main(self):
        """Main method for Data Ingestion Pipeline"""
        config_mgr = ConfigurationManager()
        data_ingestion_config = config_mgr.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(
            f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<\n\nx======================x======================x\n\n')
    except Exception as e:
        logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
        raise e
