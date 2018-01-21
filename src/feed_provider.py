import pandas as pd
import os
import feedparser


class FeedProvider:
    def __init__(self, rss_file_path):
        self.rss_file_path = rss_file_path

    def download_and_convert_rss_to_df(self, post_tags=None):
        posts = []
        with open(self.rss_file_path) as f:
            for url in f:
                feed = feedparser.parse(url)
                for post in feed.entries:
                    content = []
                    if post_tags is None:
                        posts.append(post)
                    else:
                        for tag in post_tags:
                            content.append(post[tag])
                        posts.append(content)
        return pd.DataFrame(posts, columns=post_tags)

    def get_rss_data(self, post_tags=None):
        filename = self.create_name(post_tags)
        if os.path.exists(filename):
            df = pd.read_pickle(filename)
        else:
            df = self.download_and_convert_rss_to_df(post_tags)
            df.to_pickle(filename)
        return df

    def create_name(self, post_tags):
        file_path = self.rss_file_path.replace('.txt', '')
        if post_tags is not None:
            filename = file_path + '_'.join(post_tags) + '.pkl'
        else:
            filename = file_path + '_all.pkl'
        return filename

    @staticmethod
    def get_columns_without_missing_values(df):
        return df.columns[df.notnull().all()].tolist()
