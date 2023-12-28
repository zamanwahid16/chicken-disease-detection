""" Module for training Component """
from pathlib import Path

import tensorflow as tf

from chickendisease.entity.config_entity import TrainingConfig


class Training:
    """Training Class"""

    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self) -> None:
        """Returns the base model."""
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self) -> None:
        """train and validation generators."""
        data_generator_kwargs = dict(
            rescale=1. / 255,
            validation_split=.20
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
        if self.config.params_is_augment:
            train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs
            )
        else:
            train_datagen = valid_datagen

        self.train_generator = train_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model) -> None:
        """Save the model."""
        model.save(path)

    def train_model(self, callbacks: list) -> None:
        """Train the model."""
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            callbacks=callbacks,
            validation_data=self.valid_generator,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps
        )
        self.save_model(path=self.config.trained_model_path, model=self.model)
