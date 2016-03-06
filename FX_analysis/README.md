# liquidity.ai - open source deep learning (LSTM's mostly) for financial instruments.  

1. The data set is huge. To read the complete file of one currency pair, it takes 10+GB. To manipulate the data, I used at peak 50+GB.
2. I used a AWS 64GB instance with k520 GPU.
3. However, we can still deal with the data on a more common machine (>8GB) by breaking the data into chunks.
4. There are some records (A couple of dozens of data points for each pair.), where the time stamp is earlier than the record before. That means the record is out of order. We will need to re-sort it before we process the data. Going forward, if this happens in real time, we will have to think of a way to deal with this in real time if we implement a trading system.
5. There are many points where there are time gaps between ticks. This can happen during quiet period, I imagine. If I look at the big gaps, defined as more than a day.  Then the only big gap periods are: a. The day after new year. b. Sunday night (Saturday market is closed.)  c. Chrismas day (or the day after) night.
6. Attached python code to read and extract one year of data from the csv file. Then resample it to 1-Minute bar data. The code, as is, requires about 1G memory to run. However, it can be tuned to use less memory by changing the size of the chunk to read into memory. I calculated many fields for the 1-Minute bar (Average, open, high, low, close, std etc. We don't need to use them all. But it is better to collect them and preserver more information than to discard them. We can just pick what we will need.
7. Code assumes there is a directory for the project. And there are directories 'code' and 'data' under the project home. This code resides in the 'code' folder. It assumes the .csv files extracted from the zip files are in data folder.
8. Fill the missing data, if we assume the gap is not a data error, i.e. the gap will happen in real time, then we can not fill the data with interpolation. Because, using interpolation means we are using future data. So, here in the code, I use the backfill, i.e. using the last known quote, to fill the missing value. (In the BidFill, AskFill etc. fields, not Bid, Ask fields. Bid, Ask fields are NaN when there is no data in the time period.

#data cleaning algorithm:
1. For each pair, find the breaks in the tick data that exceed 2 hrs (arbitrary interval. could be changed). 
2. Group the data between the breaks into segments.
3. For each segment use linear interpolation to regularize the data to 1 minute time intervals (again an arbitrary value)
4. Line up the data from all 5 pairs and throw away data points that do not have values for all 5 pairs
5. Find the gaps that exceed 2 hrs in this new combined data set
6. Slice the data at the gaps to produce a list of sequences with irregular lengths
7. Split each sequence into smaller 6 hr (or 360 min) sequences. Throw away left over data.
8. Line up all the sequences into a single 3 dimensional matrix with the following dimensions 

#to do items:
# Data pre-processing
- How do we hand gaps in the data? If we do regularize the data what time interval should we use? Do we interpolate to fill in gaps? If so what method do we use? We will need to verify that the method we use will allow us to deploy the model in real time (e.g. we can't use future information for interpolation etc.).
- Given that we are building a classification model, we need to define the classes we will be using. What does it mean for a data point to be labeled as a "buy", "sell", or "hold". This needs to be expressed mathematically so we can simply pass any sequence of Forex data to a labeling function which will return a sequence of labels with a the same length as the input sequence.
- As part of this work we should look analyze the raw data and draw on the experience of trading experience. For example, the pre-processing and labeling should highlight the important events in the data set. Exactly what is "important" needs to be studied and defined.

#Model building and training
- Given the preprocessed data and class labels from the above step experiment with various model architectures, objective functions, optimizers etc.
-The exact tasks here are somewhat hard to define at this point. Basically we need to do a lot of experimentation and see what works.

#Model evaluation and strategy development
- A trained RNN model will output 3 probabilities at each time step; one for each class ("buy", "sell", "hold"). How do we evaluate to quality of these predictions? The real test of this model is whether it can be used to make money. What is our strategy for using these probabilities for trading?
- That this might not be the strategy we ultimately use when we deploy the model (for example we might merge the model's predictions with other information or predictions from other models). Nevertheless it seems to me that we need to define how we will take action on probabilities in order to say whether a model has a chance of making money.
- This step is potentially related to the definition of the objective function used for model training. Depending how this work proceeds we might want to merge this strategy stage directly into the model. However at the moment it seems easier to approach it independently.

![KAGGLE-STRATEGY](https://s3.amazonaws.com/s3test-boxer/pub/I%27m+gonna+boost+it.jpg)
