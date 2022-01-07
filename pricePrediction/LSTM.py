import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import time
from datetime import *
from pathlib import Path
import myUtils #historicalData
def myCall():
	epoch_count=#REMOVED FOR PRIVACY
	split_perctg=#REMOVED FOR PRIVACY
	interval=#REMOVED FOR PRIVACY
	out_path=#REMOVED FOR PRIVACY
	Path(out_path).mkdir(parents=True, exist_ok=True)
	pair_name="BTCUSDT"
	DL=True
	frame=myUtils.getHistorical(pair_name,DL,out_path,interval,"","")
	df=frame
	df.set_index("date", drop=True, inplace=True)
	df = #REMOVED FOR PRIVACY
	df["#REMOVED FOR PRIVACY"] = df.#REMOVED FOR PRIVACY
	#########################################
	#########################################
	########### REMOVED FOR PRIVACY #########
	#########################################
	#########################################
	X = scaler.transform(X)
	y = [x[0] for x in X]
	y_backup = [x[0] for x in X_backup]
	split = int(len(X) * split_perctg)
	X_train = X[:split]
	X_test = X[split : len(X)]
	y_train = y[:split]
	y_test = y[split : len(y)]
	y_train_backup = y_backup[:split]
	y_test_backup = y_backup[split : len(y)]
	n = #REMOVED FOR PRIVACY
	Xtrain = []
	ytrain = []
	Xtest = []
	ytest = []
	for i in range(n, len(X_train)):
	    Xtrain.append(X_train[i - n : i, : X_train.shape[1]])
	    ytrain.append(y_train[i])  # predict next record
	for i in range(n, len(X_test)):
	    Xtest.append(X_test[i - n : i, : X_test.shape[1]])
	    ytest.append(y_test[i])  # predict next record

	val = np.array(ytrain[0])
	val = np.c_[val, np.zeros(val.shape)]
	scaler.inverse_transform(val)
	Xtrain, ytrain = (np.array(Xtrain), np.array(ytrain))
	Xtrain = np.reshape(Xtrain, (Xtrain.shape[0], Xtrain.shape[1], Xtrain.shape[2]))
	Xtest, ytest = (np.array(Xtest), np.array(ytest))
	Xtest = np.reshape(Xtest, (Xtest.shape[0], Xtest.shape[1], Xtest.shape[2]))


	##############LSTM MODEL###############
	from keras.models import Sequential
	from keras.layers import LSTM, Dense, Dropout
	from tensorflow.keras.optimizers import Adam
	from keras.callbacks import EarlyStopping
	callback = EarlyStopping(monitor='val_loss', patience=80)
	model = Sequential()
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.add(#REMOVED FOR PRIVACY
	model.compile(loss="mean_squared_error", optimizer=Adam(1e-3))
	history=model.fit(
	    Xtrain, ytrain, epochs=epoch_count, validation_data=(Xtest, ytest), 
	    batch_size=16, verbose=1, callbacks=[callback]
	)
	model.summary()

	############TRAINING PLOT####################
	fig, ax1 = plt.subplots(constrained_layout=True)
	ax2 = ax1.twinx()
	ax1.plot(history.history['loss'], label='train')
	ax1.set_xlabel('epoch')
	ax1.set_ylabel('loss')
	ax2.plot(history.history['val_loss'],color='green', label='val')
	ax2.set_ylabel('val loss')
	# plt.show()
	plt.savefig(out_path+"/training"+pair_name+".png")

	trainPredict = model.predict(Xtrain)
	testPredict = model.predict(Xtest)
	trainPredict = np.c_[trainPredict, np.zeros(trainPredict.shape)]
	testPredict = np.c_[testPredict, np.zeros(testPredict.shape)]
	trainPredict = scaler.inverse_transform(trainPredict)
	trainPredict = [x[0] for x in trainPredict]
	testPredict = scaler.inverse_transform(testPredict)
	testPredict = [x[0] for x in testPredict]
	real_test=y_test_backup
	# real_test.append(0)
	d = {"real":real_test,"pred":(list(np.zeros(n))+testPredict)}
	out=pd.DataFrame(data=d)
	out.to_csv("vamoa.csv")

	#########COMPLETE PLOT###############
	fig, ax = plt.subplots(figsize=(15,10))
	plt.plot(df.close,color='red', label="real")
	plt.plot(list(np.zeros(n))+(trainPredict),color='green', label="Predicted Train")
	ax.plot(range(len(trainPredict)+n,
		      len(trainPredict)+len(testPredict)+n),
		      testPredict,
		      color='blue',
		      label='Predicted Test')
	plt.savefig(out_path+"/complete_plot"+pair_name+".png")

	#############TEST PLOT###############
	fig, ax = plt.subplots(figsize=(15,10))
	plt.plot(real_test,color='red', label="real")
	plt.plot((list(np.zeros(n))+testPredict),color='green', label="Predicted Test")
	# plt.legend()
	plt.savefig(out_path+"/test"+pair_name+".png")

	from sklearn.metrics import mean_squared_error
	from sklearn import preprocessing
	real_train=y_train_backup
	trainScore = mean_squared_error(real_train[n:], trainPredict, squared=False)
	print("train Score: %.2f RMSE" % (trainScore))
	testScore = mean_squared_error(real_test[n:], testPredict, squared=False)
	print("Test Score: %.2f RMSE" % (testScore))
	

	############# GUESSING TOMORROW ###############
	tomorrow=[]
	tomorrow.append(X[-n:len(X),:X.shape[1]])
	tomorrow=np.array(tomorrow)
	tomorrow = np.reshape(tomorrow, (tomorrow.shape[0], tomorrow.shape[1], tomorrow.shape[2]))
	#########################################
	#########################################
	########### REMOVED FOR PRIVACY #########
	#########################################
	#########################################

	#########################################
	#########################################
	########### SECONDARY PREDICT ###########
	#########################################
	#########################################
	pair_name2="ETHUSDT"
	DL=True
	# out_path="mydata"
	frame2=myUtils.getHistorical(pair_name2,DL,out_path,interval,"","")

	#########################################
	#########################################
	########### REMOVED FOR PRIVACY #########
	#########################################
	#########################################
	y2 = [x[0] for x in X2]
	y_backup2 = [x[0] for x in X_backup2]
	#DATA SEPARATION
	Xtest2 = []
	ytest2 = []
	for i in range(n, len(X2)):
	    Xtest2.append(X2[i - n : i, : X2.shape[1]])
	    ytest2.append(y2[i])  # predict next record
	Xtest2, ytest2 = (np.array(Xtest2), np.array(ytest2))
	Xtest2 = np.reshape(Xtest2, (Xtest2.shape[0], Xtest2.shape[1], Xtest2.shape[2]))
	Predict2 = model.predict(Xtest2)
	Predict2 = np.c_[Predict2, np.zeros(Predict2.shape)]
	Predict2 = scaler2.inverse_transform(Predict2)
	Predict2 = [x[0] for x in Predict2]
	tomorrow2=[]
	#########################################
	#########################################
	########### REMOVED FOR PRIVACY #########
	#########################################
	#########################################
	real_test2=y_backup2
	d2 = {"real":real_test2[n:],"pred":Predict2}
	out2=pd.DataFrame(data=d2)
	out2.to_csv("vamoa2.csv")
	print("BTC Train Score: %.2f RMSE" % (trainScore))
	print("BTC Test Score: %.2f RMSE" % (testScore))
	testScoreEth = mean_squared_error(real_test2[n:], Predict2, squared=False)
	print("ETH Test Score: %.2f RMSE" % (testScoreEth))
	fig, ax = plt.subplots(figsize=(15,10))
	plt.plot(real_test2,color='red', label="real")
	plt.plot((list(np.zeros(n))+Predict2),color='green', label="Predicted ETH")
	plt.savefig(out_path+"/secondary.png")#TODO secondary name, more options
	
	print(frame2.head)
	frame2.to_csv("temp.csv")
	hour=int(datetime.now().hour)
	if hour<21:
		today=datetime.now() - timedelta(days=1) 
	else:
		today=datetime.now()
	data=[[str(frame.index[-1]),str(today.strftime("%Y-%m-%d")), str(pair_name), str(frame.iloc[-1,frame.columns.get_loc("close")]), str(pred_tomorrow[0][0])]]
	data.append([str(frame2.index[-1]),str(today.strftime("%Y-%m-%d")), str(pair_name2), str(frame2.iloc[-1,frame2.columns.get_loc("close")]), str(pred_tomorrow2[0][0])])
	ret=pd.DataFrame(data)
	print(ret.head)
	return ret
	
