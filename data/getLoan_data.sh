#!/bin/bash
#python fx_lstm1.py -i data/clean_tick_data_1_min_step.csv -o output.csv
wget https://s3.amazonaws.com/liquidity.ai/Loan-Data/loan-data.zip
unzip loan-data.zip
rm loan-data.zip
