""" run the pipeline """

from chickendisease import logger
from chickendisease.pipeline.base_model import BaseModelPipeline
from chickendisease.pipeline.data_ingestion import DataIngestionPipeline
from chickendisease.pipeline.trainer import ModelTrainer

# Stage 1: Data Ingestion
STAGE_NAME = 'Data Ingestion'
try:
    logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
    data_pipeline = DataIngestionPipeline()
    data_pipeline.main()
    logger.info(
        f'>>>>> Completed pipeline for {STAGE_NAME}<<<<<\n\nx======================x======================x\n\n')
except Exception as e:
    logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
    raise e

# Stage 2: Prepare Base Model
STAGE_NAME = 'Base Model'
try:
    logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
    model_pipeline = BaseModelPipeline()
    model_pipeline.main()
    logger.info(
        f'>>>>> Completed pipeline for {STAGE_NAME}<<<<<\n\nx======================x======================x\n\n')
except Exception as e:
    logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
    raise e

# Stage 3: Training the Model
STAGE_NAME = 'Training'
try:
    logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
    trainer = ModelTrainer()
    trainer.main()
    logger.info(
        f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<\n\nx======================x======================x\n\n')
except Exception as e:
    logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
    raise e
