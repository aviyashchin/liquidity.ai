I have also attached IPython Notebooks (in HTML format) to this email for a credit project which I recently worked on. I did this project pretty quickly (in a few days) and would have gone much more in detail but did not have sufficient time.

I made two data sets. (1) One in which I extracted individual features from date datatypes, dealt with missing data, either by imputing it (typically zero or the mean) or removed the observations. There were a couple of ordinal data types which I converted to integer datatypes. Also, there were several categorical data types which I "dummified". I created a new feature which represented the delay between when the credit was pulled and when it was listed. I also removed a couple of outliers and imputed that a couple of negative observations were most likely positive instead of negative. (2) The other data set which I extracted was designed to be used by H2O (a parallelized machine learning platform). H2O internally deals with missing data and can treat categorical data as factors. 

I then split the data set into a training and test set and quickly ran some algorithms to get an idea of the performance of each algorithm. I should note that I scaled the appropriate data types. The algorithms (using Scikit-Learn) which I ran included: 
Logistic Regression with ElasticNet Regularization with stochastic gradient descent (SGD)
Logistic Regression with L1 Regularization
Random Forest
Gradient Boosting
Naive Bayes
k-Nearest Neighbors
I then looked at the most promising algorithms and used 10-folds cross validation and observed the ROC AUC of these algorithms. 

I used an ensemble majority-voting method to come up with an ensemble model. On a separate machine, I tuned the hyperparameters using a grid search and a randomized grid search. 

I then did the majority voting ensemble again and then computed the AUC and plotted the results of the different methods. 

It does appear that it is challenging to get a well-performing classifier for this data set. 

I also utilized H2o within Python 2.7 to see if I could improve upon the results. Rather than use cross-validation, I split up the data set into training, test, and validation set. H20 also has internal n-folds cross-validation but I didn't use this.

I ran Random Forest, Gradient Boosting and Deep Learning using H2O. I should note that H2O does seem to run considerably faster than Scikit-Learn. The performance of these do not seem to be that much better than those generated using Scikit-Learn. I tried a couple of different hyperparameter changes but I didn't really have enough time to properly tune them. Also, I tried running GBM with only the top 30 most important features but it did not seem to improve the performance that much. One of the nice features about H2O is that it gives a wealth of information about a particular model in nice format.

For future work, I would go back to the original data set and see if I can engineer any more features or look for external data which might improve the model. For instance, I include the median income, unemployment rate, and other socio-economic data for a particular city. I would also spend more time tuning the models. 
