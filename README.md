# liquidity.ai - open source deep learning (LSTM's mostly) for financial instruments.  

1. The out-of-order tick data: These can happen in realtime, I would imagine. The tick data and timestamps were generated when the quote event happen and send to a central place to collect. Depending on the network delay or slight processing delay between machines, if the events happened at the borderline between seconds, then very occationally, the records can be out of chronological order by a fraction of a second when they were collected. In reality, only very very small number of records are out of order. For example, for the EURUSD data, out of the 100+ millions records, only 33 out of order records. So this should not be a big problem. We just need to keep that in mind.
2. Boris mentioned about daylight time switching when we were discussing about the out-of-order records. This got me worried a little. It looks like the time stamps are in NY time. There could be a problem when we fall back the clock as we will do next week. There could be one over-lapped hour at 2am. Fortunately, this did not affect our data. The reason is that for this FX market, Saturdays are mostly closed. Only a few Saturdays and early Sundays have some sporadic data and for vast majority of Saturdays, there was no data. (We should probably exclude Saturdays in the data cleaning procedures.) For the data appeared in Sunday morning 2am period (I only looked at EURUSD data), none of the records were on a Daylight Saving Time changing dates.
3. Regarding the gap statistics, it is not simple to get meaningful stats. Gap is defined as consecutive time difference >= 2 seconds. Gaps occurs during the normal trading hours too. Because the tick count during trading hours are much higher than off-hours, the count of the gap may not be smaller. Here I am showing some statistics of gap statistics for EURUSD. The quantities Count,Median,Mean are all applied to the time differences of consecutive records, i.e. gap. nolabel, 2 and 60 correspond to: all records, gap of >=2 (i.e. gap of more than 1s), gap of >60 (gap of more than 1min)

   Hour    Count Median   Mean  Count2 Median2  Mean2 Ratio2 Count60 Median60   Mean60      Ratio60
1     0  3444207      1  2.871 1098821       4  8.362 0.3190    6853       75  164.873 1.989718e-03
2     1  3269208      1  3.083 1076767       4  8.745 0.3294    7108       74  189.505 2.174227e-03
3     2  2650024      1  3.713  937329       5  9.947 0.3537   10900       75  134.620 4.113170e-03
4     3  2369608      1  4.135  860761       5 10.863 0.3633   13088       75  126.261 5.523276e-03
5     4  2396142      1  4.150  866065       5 10.956 0.3614   13116       76  137.243 5.473799e-03
6     5  2921109      1  3.354 1013324       5  9.081 0.3469    9320       74  135.915 3.190569e-03
7     6  4954799      1  1.984 1378812       3  6.174 0.2783    3450       73  222.957 6.962946e-04
8     7  7078363      1  1.396 1610988       3  4.882 0.2276     941       72  647.561 1.329403e-04
9     8  7610459      0  1.323 1633574       3  4.844 0.2146     804       70  984.525 1.056441e-04
10    9  6998067      1  1.430 1586151       3  5.077 0.2267    1121       70  682.887 1.601871e-04
11   10  6352533      1  1.569 1534820       3  5.359 0.2416    1445       70  519.473 2.274683e-04
12   11  6220618      1  1.558 1531010       3  5.212 0.2461    1347       70  347.757 2.165380e-04
13   12  8353094      0  1.229 1602671       3  4.990 0.1919     811       70 1225.371 9.708977e-05
14   13  9669270      0  1.052 1664676       3  4.499 0.1722     474       73 1847.580 4.902128e-05
15   14 10134352      0  1.002 1685743       3  4.320 0.1663     449       78 1902.073 4.430476e-05
16   15  8739596      0  1.379 1654531       3  5.781 0.1893     627       75 4413.490 7.174245e-05
17   16  6437828      1  2.255 1502105       3  8.503 0.2333    1746       73 3047.867 2.712095e-04
18   17  4817526      1  4.491 1334639       4 15.298 0.2770    3716       75 3388.085 7.713503e-04
19   18  4667532      1  7.093 1273762       4 25.121 0.2729    6893       80 3473.593 1.476798e-03
20   19  4045819      1  5.619 1222534       4 17.845 0.3022   10342       80 1289.061 2.556219e-03
21   20  2883602      1  4.690 1017176       5 12.760 0.3527   15661       79  283.580 5.431055e-03
22   21  1989217      1 11.307  754434       6 29.409 0.3793   20765       83  712.475 1.043878e-02
23   22  1997732      1  7.995  732138       6 21.386 0.3665   19689       82  436.478 9.855676e-03
24   23  2172875      1  4.579  813241       5 11.766 0.3743   15505       80  133.794 7.135707e-03
There are many questions can be asked about the above data, for example why are the average gap for the afternoon 12-18 is much bigger. I suspect, they are caused by the opening quotes after a long holidays or weekends. And those probably opens around those hours. I will have to dig and process the data more. But please take a look at the data and give any feedbacks. The above output is also in the attached csv file.


![KAGGLE-STRATEGY](https://s3.amazonaws.com/s3test-boxer/pub/I%27m+gonna+boost+it.jpg)
