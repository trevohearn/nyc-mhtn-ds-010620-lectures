
In this current day and age there is always a lot of misinformation floating around
and since we are learning to become data scientists I decided I'd try to look at
some gleaned data off of Kaggle.com about this virus. The best thing about this data
set is that whoever is finding the information is continually updating it as new
cases arise.

import pandas as pd
df = pd.read_csv("covid_19_data.csv")
df.shape
#(4513, 8)

df.isna().sum() #province/state only column with problems

df['Confirmed'].describe()
count     4513.000000
mean       577.460891
std       4989.693765
min          0.000000
25%          1.000000
50%          8.000000
75%         93.000000
max      67743.000000
#13

country_sums = df.groupby('Country/Region').sum()
country_sums['Deaths']['US']


Beware of the virus as it continues to spread, and know what you can do to help
yourself not get it while you are out and about doing the mandatory walk of life.
Simply, wash your hands. If you touch common metal, like holding the metal rods on
the subway, the virus can survive there for a minimum of two hours. Also, the best
practice is to try and maintain a one meter radius from people as often as you can.
That mindset will help you from getting accidentally coughed/sneezed on.
