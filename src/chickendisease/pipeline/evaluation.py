""" Module for evaluation pipeline"""

from chickendisease import logger
from chickendisease.components.evaluation import Evaluation
from chickendisease.config.configuration import ConfigurationManager

STAGE_NAME = 'Evaluation'


class EvaluationPipeline:
    """Evaluation Pipeline Class"""

    def __init__(self):
        pass

    def main(self) -> None:
        """Run the evaluation pipeline."""
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluate()
        evaluation.save_scores()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> Running pipeline for {STAGE_NAME} <<<<<')
        evaluate = Evaluation()
        evaluate.main()
        logger.info(
            f'>>>>> Completed pipeline for {STAGE_NAME} <<<<<\n\nx======================x======================x\n\n')
    except Exception as e:
        logger.error(f'Failed to run the pipeline for {STAGE_NAME} with exception: {e}')
        raise e
