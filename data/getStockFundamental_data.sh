#!/bin/bash
#python fx_lstm1.py -i data/clean_tick_data_1_min_step.csv -o output.csv
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/SF1_20160305.csv.zip
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/companylist-AMEX.csv
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/companylist-NASDAQ.csv
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/companylist-NYSE.csv
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/indicators.csv
wget https://s3.amazonaws.com/liquidity.ai/Stock-Data/timeperiods.csv
unzip SF1_20160305.csv.zip
rm SF1_20160305.csv.zip
