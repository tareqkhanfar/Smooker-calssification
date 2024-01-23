import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from main import Main
import pandas as pd
object = Main()
x_train=object.x_train
x_test=object.x_test
y_train=object.y_train
y_test=object.y_test



model = Sequential([
    Dense(units=3, activation='relu', input_shape=(x_train.shape[1],)),
    Dense(units=1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=500, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(x_test, y_test)
print(f'Accuracy: {accuracy}')