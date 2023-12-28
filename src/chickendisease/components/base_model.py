""" Module for base model class """
import urllib.request as request
from pathlib import Path

import tensorflow as tf

from chickendisease.entity.config_entity import BaseModelConfig


class BaseModel:
    """Base Model Class"""

    def __init__(self, config: BaseModelConfig):
        self.config = config

    def get_base_model(self) -> tf.keras.Model:
        """Returns the base model."""
        self.model = tf.keras.applications.VGG16(
            include_top=self.config.params_include_top,
            weights=self.config.params_weights,
            input_shape=self.config.params_image_size
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model) -> None:
        """Save the model.

        :param path: Path to save the model
        :param model: Model to save
        """
        model.save(path)

    @staticmethod
    def _prepare_full_model(model: tf.keras.Model, classes: int, freeze_all: bool, freeze_till, learning_rate: float) -> tf.keras.Model:
        """Prepare the full model.

        :param model: Base model
        :param classes: Number of classes
        :param freeze_all: Freeze all layers
        :param freeze_till: Freeze till this layer
        :param learning_rate: Learning rate

        :return: Full model
        """
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten_input = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation='softmax')(flatten_input)
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        full_model.compile(
            loss='categorical_crossentropy',
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            metrics=['accuracy']
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        """Update the base model and save it."""
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
