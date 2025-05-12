import pandas as pd
try:
  df_old = pd.read_csv('leaderboard/leaderboard_recsys.csv')
except:
  df_old = pd.read_html('https://luksiensyner.github.io/', index_col=0)[0]
#df_old=df_old[['Username', 'Submits', 'Top Score', 'Last Submit']]
#df_old.to_csv('leaderboard/leaderboard_old.csv', index=None)
df_last=pd.read_html('https://luksiensyner.github.io/', index_col=0)[0]
df_last=df_last.join(df_old.set_index('Username'), on='Username', rsuffix='old')
#df_last['Top Score'] = df_last.apply(lambda x: x['Score'] if (x['Score']>x['Scoreold']) else x['Scoreold'], axis=1)
#df_last['Top Score']=df_last.apply(lambda x: x['Top Score'] if x['Top Score']<x['Score'] else x['Score'], axis=1)
#df_last=df_last.sort_values('Top Score')

df_last.to_csv('leaderboard/leaderboard_recsys.csv', index=None)

print('Done')
