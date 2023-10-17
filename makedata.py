from tensorflow.keras.applications import InceptionV3
import tensorflow as tf
import os

class MakeData:

    def __init__(self) -> None:
        self.base_model = InceptionV3() #Declaration of Base Model
        self.root_path = "dataset" #setting up the base path
    
        