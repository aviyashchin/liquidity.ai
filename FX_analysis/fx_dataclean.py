import sys, getopt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d


try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'fx_dataclean.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        inputfile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

pairs = ['USDJPY', 'USDCHF', 'EURUSD', 'USDCAD', 'GBPUSD']

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%y %H:%M:%S')
max_time_gap = pd.Timedelta('2 hours')
limit=None
limit=500000

resampled_pair_dfs = []
for pair in pairs:
    print pair
    
    df=pd.read_csv('data/' + pair + inputfile, names=['datetime', pair+'_bid', pair+'_ask'], parse_dates=['datetime'], date_parser=dateparse, nrows=limit, index_col=0)
    df.sort_index(inplace=True)
    df['group'] = np.array((pd.Series(df.index).diff()>max_time_gap).apply(lambda x: 1 if x else 0).cumsum())
    grouped=df.groupby('group')

    resampled_groups = []
    for group_number, group in filter(lambda x: len(x[1])>1, grouped):
        
        ts = group.index.astype('int64')/10**9
        f_bid= interp1d(ts, group[pair+'_bid'])
        f_ask= interp1d(ts, group[pair+'_ask'])
        
        resampled_group = group.resample("1 min")
        del resampled_group['group']
        resampled_group[pair+'_bid'][1:] = f_bid(resampled_group.index.astype('int64')[1:]/10**9)
        resampled_group[pair+'_ask'][1:] = f_ask(resampled_group.index.astype('int64')[1:]/10**9)
        resampled_groups.append(resampled_group)
        
    print "num groups:", len(resampled_groups)
    resampled_df = pd.concat(resampled_groups)
    resampled_pair_dfs.append(resampled_df)
    
df_clean = pd.concat(resampled_pair_dfs, axis=1, join='inner')
df_clean['group'] = np.array((pd.Series(df_clean.index).diff()>max_time_gap).apply(lambda x: 1 if x else 0).cumsum())
grouped=df_clean.groupby('group')
for group_number, group in grouped:
    if len(group)<100:
        df_clean = df_clean.drop(grouped.get_group(group_number).index)
df_clean.to_csv('data/' + outputfile)
