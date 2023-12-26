""" run the pipeline """

from chickendisease import logger
from chickendisease.pipeline.data_ingestion import DataIngestionPipeline

# Stage 1: Data Ingestion
STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<')
except Exception as e:
    logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
    raise e
