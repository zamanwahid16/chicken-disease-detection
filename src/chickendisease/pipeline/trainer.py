""" Model Trainer """
from chickendisease import logger
from chickendisease.components.callbacks import Callbacks
from chickendisease.components.training import Training
from chickendisease.config.configuration import ConfigurationManager

STAGE_NAME = 'Training'


class ModelTrainer:
    """Model Trainer class."""

    def __init__(self):
        pass

    def main(self):
        """Main function for the training stage."""
        config = ConfigurationManager()
        callbacks_config = config.get_callbacks_config()
        callbacks = Callbacks(config=callbacks_config).get_callbacks()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train_model(callbacks=callbacks)


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
        trainer = ModelTrainer()
        trainer.main()
        logger.info(
            f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<\n\nx======================x======================x\n\n')
    except Exception as e:
        logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
        raise e
