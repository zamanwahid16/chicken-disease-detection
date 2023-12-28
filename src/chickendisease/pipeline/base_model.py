""" Pipeline module for preparing modified base model """
from chickendisease import logger
from chickendisease.components.base_model import BaseModel
from chickendisease.config.configuration import ConfigurationManager

STAGE_NAME = 'Base Model'


class BaseModelPipeline:
    """Base Model Pipeline Class"""

    def __init__(self):
        pass

    def main(self):
        """Main method for Base Model Pipeline"""
        config_mgr = ConfigurationManager()
        base_model_config = config_mgr.get_base_model_config()
        base_model = BaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
        pipeline = BaseModelPipeline()
        pipeline.main()
        logger.info(
            f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<\n\nx======================x======================x\n\n')
    except Exception as e:
        logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
        raise e
