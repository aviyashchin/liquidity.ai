import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import Adam
from keras.layers.core import Dropout, TimeDistributedDense, Merge

from sklearn.cross_validation import train_test_split

df_clean=pd.read_csv('/home/ubuntu/data/' + 'clean_tick_data_1_min_step.csv', parse_dates=['datetime'], index_col=0)
grouped=df_clean.groupby('group')

groups=[]
for (group_number, group) in grouped:
    mat = grouped.get_group(group_number).as_matrix()
    remainder = mat.shape[0]%60
    num_slices = mat.shape[0]//60
    if remainder:
        mat = mat[:-remainder,:-1].reshape((num_slices, 60, 10))
    else:
        mat = mat[:,:-1].reshape((num_slices, 60, 10))
    groups.append(mat)
sliced_data = np.vstack(groups)

means=sliced_data.mean(axis=0).mean(axis=0)
prediction_interval=10
X=sliced_data[:,:-prediction_interval,:]-means
Y=sliced_data[:,prediction_interval:,:]-means-X
Y=Y.reshape(Y.shape[0],Y.shape[1],5,2).mean(axis=3)[:,:,:]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
X_train, X_valid, Y_train, Y_valid = train_test_split(X_train, Y_train, test_size=0.1)

pred_idx=0

adam = Adam(clipnorm=1.0)

USDJPY_model = Sequential()
USDJPY_model.add(LSTM(2, 50, return_sequences=True, activation='linear'))

USDCHF_model = Sequential()
USDCHF_model.add(LSTM(2, 50, return_sequences=True, activation='linear'))

EURUSD_model = Sequential()
EURUSD_model.add(LSTM(2, 50, return_sequences=True, activation='linear'))

USDCAD_model = Sequential()
USDCAD_model.add(LSTM(2, 50, return_sequences=True, activation='linear'))

GBPUSD_model = Sequential()
GBPUSD_model.add(LSTM(2, 50, return_sequences=True, activation='linear'))

model = Sequential()
model.add(Merge([USDJPY_model, USDCHF_model, EURUSD_model, USDCAD_model, GBPUSD_model], mode='concat'))
model.add(TimeDistributedDense(250, 1, activation='linear'))

model.compile(loss='mse', optimizer=adam)

earlystopper = EarlyStopping(monitor='val_loss', patience=5, verbose=1)
checkpointer = ModelCheckpoint(filepath="/home/ubuntu/models/weights.hdf5", verbose=1, save_best_only=True)

history = model.fit([X_train[:,:,0:2], X_train[:,:,2:4], X_train[:,:,4:6], X_train[:,:,6:8], X_train[:,:,8:]], Y_train[:,:,pred_idx,np.newaxis], batch_size=500, nb_epoch=200, validation_data=[[X_valid[:,:,0:2], X_valid[:,:,2:4], X_valid[:,:,4:6], X_valid[:,:,6:8], X_valid[:,:,8:]], Y_valid[:,:,pred_idx,np.newaxis]], callbacks=[checkpointer, earlystopper])

Y_pred = model.predict([X_test[:,:,0:2], X_test[:,:,2:4], X_test[:,:,4:6], X_test[:,:,6:8], X_test[:,:,8:]])