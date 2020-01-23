from django.apps import AppConfig
import tensorflow as tf

class GeneralConfig(AppConfig):
    name = 'general'

    def ready(self):
        # tf.logging.set_verbosity(tf.logging.FATAL) deprecatedなので書き換え。
        tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)