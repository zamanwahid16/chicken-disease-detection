""" Module for Callsback Component """
import os
import time

import tensorflow as tf

from chickendisease.entity.config_entity import CallbacksConfig


class Callbacks:
    """Callbacks Class"""

    def __init__(self, config: CallbacksConfig):
        self.callbacks_config = callbacks_config

    @property
    def _create_tb_callback(self):
        """Returns the TensorBoard callback."""
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
        tb_logs_dir = os.path.join(
            self.callbacks_config.tensorboard_logs_dir,
            f'tb_logs_at_{timestamp}',
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_logs_dir)

    @property
    def _create_ckpt_callback(self):
        """Returns the Model Checkpoint callback."""
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.callbacks_config.checkpoint_model_path,
            save_best_only=True,
        )

    def get_callbacks(self):
        """Returns the list of callbacks."""
        return [
            self._create_tb_callback,
            self._create_ckpt_callback,
        ]
