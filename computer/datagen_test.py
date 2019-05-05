import pandas as pd

mypandas = pd.read_csv("mypandas.csv")

from keras_preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator()

train_generator = datagen.flow_from_dataframe(dataframe = mypandas,
                                              x_col = "imgpaths",
                                              y_col = "steerings",
                                              directory =  "/media/martin/mydrive/sdcar/computer/lol/",
                                              class_mode = "categorical",
                                              batch_size = 100)
