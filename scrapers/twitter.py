import os
from dotenv import load_dotenv

import tweepy

load_dotenv()
twitter_client = tweepy.Client(
    bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
    consumer_key=os.environ["TWITTER_API_KEY"],
    consumer_secret=os.environ["TWITTER_API_KEY_SECRET"],
    access_token=os.environ["TWITTER_ACCESS_TOKEN"],
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
)


def scrape_user_tweets(username: str, num_tweets=1, mock: bool = False):
    """
    Scrape the latest tweets from a user's Twitter profile.
    """
    tweet_list = []

    if mock:
        # Mock data for testing
        return [
            {
                "tweet": "This is a mock tweet 1",
                "date": "2023-10-01",
                "likes": 10,
                "retweets": 2,
            },
            {
                "tweet": "This is a mock tweet 2",
                "date": "2023-10-02",
                "likes": 20,
                "retweets": 5,
            },
        ]
    else:
        print("Scraping tweets...")
        print(username)
        user_id = twitter_client.get_user(username=username).data.id
        tweets = twitter_client.get_users_tweets(
            id=user_id, max_results=num_tweets, exclude=["retweets", "replies"]
        )
        tweets = tweets.data

        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)
        return None


if __name__ == "__main__":
    tweets = scrape_user_tweets(username="BinodKaflle")
    print(tweets)
