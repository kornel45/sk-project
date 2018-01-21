import pandas as pd
from src.feed_provider import FeedProvider
import os

print(os.getcwd())

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_columns', 400)


rss_filename = 'result_files/rss_sources.txt'
post_tag_list = ['title', 'link', 'summary']
feed_provider = FeedProvider(rss_filename)
rss_df = feed_provider.get_rss_data()
print(rss_df.head())
