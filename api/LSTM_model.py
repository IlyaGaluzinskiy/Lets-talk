from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

from api.loader import actions


model = Sequential()
model.add(LSTM(128, return_sequences=True, activation='relu', input_shape=(30, 84)))
model.add(LSTM(256, return_sequences=True, activation='relu'))
model.add(LSTM(128, return_sequences=False, activation='relu'))

model.add(Dense(actions.shape[0], activation='softmax'))

optim = Adam(clipnorm=0.7)

model.compile(optimizer=optim, loss='categorical_crossentropy', metrics=['categorical_accuracy'])

model.load_weights('3lstm.h5')
