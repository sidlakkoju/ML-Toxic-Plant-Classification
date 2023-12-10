# import coremltools as ct
# import tensorflow as tf

# from tensorflow.keras.applications import ResNet50
# import tensorflow as tf
# from tensorflow.keras.applications import ResNet50
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.optimizers import Adam


# IMG_SHAPE = (224, 224, 3)

# base_model = ResNet50(weights='imagenet', include_top=False, input_shape=IMG_SHAPE)

# for layer in base_model.layers:
#     layer.trainable = False



# model = Sequential()
# model.add(base_model)
# model.add(GlobalAveragePooling2D())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(0.3))
# model.add(Dense(1, activation='sigmoid'))  # Binary classification, adjust if needed

# # if platform.system() == "Darwin" and platform.processor() == "arm":
# #     opt = tf.keras.optimizers.legacy.Adam(learning_rate=0.0001)
# # else:
# # opt = tf.keras.optimizers.Adam(learning_rate=0.0001)
# opt = tf.keras.optimizers.legacy.Adam(learning_rate=0.0001)

# model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])

# model.load_weights('/Users/siddharthlakkoju/Documents/Semester 5/Machine Learning/Project/transfer_p1_virginia/')


# # Pass in `tf.keras.Model` to the Unified Conversion API
# mlmodel = ct.convert(model, convert_to="mlprogram")

# mlmodel.save('resnet.mlpackage')

from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras import layers, models

# Define your model
# Define the CNN model
IMG_SHAPE = (224, 224, 3)
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=IMG_SHAPE)
model = Sequential()
model.add(base_model)
model.add(GlobalAveragePooling2D())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(1, activation='sigmoid'))  # Binary classification, adjust if needed

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Display the model summary
model.summary()

# Plot the model
plot_model(model, to_file='model_plot_resnet.png', show_shapes=True, show_layer_names=True)

