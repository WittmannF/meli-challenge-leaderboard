import pandas as pd
try:
  df_old = pd.read_csv('leaderboard/leaderboard_recsys.csv')
except:
  df_old = pd.read_html('https://luksiensyner.github.io/', index_col=0)[0]

cols = [c for c in df_old.columns if 'old' not in c]

df_old=df_old[cols]
#df_old.to_csv('leaderboard/leaderboard_old.csv', index=None)
df_last=pd.read_html('https://luksiensyner.github.io/', index_col=0)[0]
df_last=df_last.join(df_old.set_index('Username'), on='Username', rsuffix='old')

#score_col = 'sum of scores'
score_col = 'borda count'
old_score_col = score_col+'old'
top_score_col = 'top '+score_col
df_last[top_score_col] = df_last.apply(lambda x: x[score_col] if (x[score_col]>x[old_score_col]) else x[old_score_col], axis=1)
df_last=df_last.sort_values(top_score_col, ascending=False)

score_col = 'sum of scores'
old_score_col = score_col+'old'
top_score_col = 'Top Score'
df_last[top_score_col] = df_last.apply(lambda x: x[score_col] if (x[score_col]>x[old_score_col]) else x[old_score_col], axis=1)

df_last.to_csv('leaderboard/leaderboard_recsys.csv', index=None)

print(df_last)
print('Done!')
