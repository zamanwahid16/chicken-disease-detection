"""Evaulation component"""
import os
from pathlib import Path

import tensorflow as tf

from chickendisease.entity.config_entity import EvaluationConfig
from chickendisease.utils.common import save_json


class Evaluation:
    """Evaluation Class"""

    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self) -> None:
        """Validation generator."""
        data_generator_kwargs = dict(
            rescale=1. / 255,
            validation_split=.30
        )
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )
        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )
        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset='validation',
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        """Load the model.
        :param path: Path to the model
        :return: tf.keras.Model
        """
        return tf.keras.models.load_model(path)

    def evaluate(self) -> None:
        """Evaluate the model."""
        model = self.load_model(self.config.trained_model_path)
        self._valid_generator()
        self.scores = model.evaluate(self.valid_generator)

    def save_scores(self) -> None:
        """Save the scores."""
        scores = {'loss': self.scores[0], 'accuracy': self.scores[1]}
        path = Path(os.path.join(self.config.root_dir, 'scores.json'))
        save_json(path=path, data=scores)
