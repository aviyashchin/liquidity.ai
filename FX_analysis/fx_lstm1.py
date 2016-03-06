import sys, getopt, datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
from keras.models import Sequential
from keras.layers.recurrent import LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint

from sklearn.cross_validation import train_test_split


try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'fx_lstm1.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg


df_clean = pd.read_csv(inputfile)


grouped=df_clean.groupby('group')

 
groups=[]
for (group_number, group) in grouped:
    mat = grouped.get_group(group_number).as_matrix()
    remainder = mat.shape[0]%360
    num_slices = mat.shape[0]//360
    if remainder:
        mat = mat[:-remainder,1:-1].reshape((num_slices, 360, 10))
    else:
        mat = mat[:,1:-1].reshape((num_slices, 360, 10))
    groups.append(mat)
sliced_data = np.vstack(groups)
 
prediction_interval=10
X=sliced_data[:,:-prediction_interval,:]
Y=sliced_data.reshape(sliced_data.shape[0],sliced_data.shape[1],5,2).mean(axis=3)[:,prediction_interval:,:]
 
X_means = X.mean(axis=0).mean(axis=0)
Y_means = Y.mean(axis=0).mean(axis=0)
 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
 
pred_idx=0
 
print "Creating the LSTM " + str(datetime.datetime.now())
model = Sequential()
model.add(LSTM(1, return_sequences=True, activation='linear', input_dim=10))
#model.add(LSTM(2, 1, return_sequences=True, activation='linear', input_dim=10))

print "Compiling " + str(datetime.datetime.now())
model.compile(loss='mean_squared_logarithmic_error', optimizer='adam')
 
earlystopper = EarlyStopping(monitor='val_loss', patience=1, verbose=1)
checkpointer = ModelCheckpoint(filepath="models/weights.hdf5", verbose=1, save_best_only=True)
 
print "Training " + str(datetime.datetime.now())
history = model.fit(X_train[:,:,:10]-X_means[:10], Y_train[:,:,pred_idx,np.newaxis]-Y_means[pred_idx], batch_size=5, nb_epoch=10, validation_split=.15, callbacks=[checkpointer, earlystopper])

print "Done training " + str(datetime.datetime.now())
plt.plot(history.epoch, history.history['loss'],history.epoch, history.history['val_loss'])
plt.legend(['train','validation'])

plt.savefig(outputfile + '.png')

print "Predicting " + str(datetime.datetime.now())
Y_pred = model.predict(X_test[:,:,:10]-X_means[:10],batch_size=5)

print "Saving result " + str(datetime.datetime.now())

np.savetxt(outputfile+'.csv', Y_pred, delimiter=",")

