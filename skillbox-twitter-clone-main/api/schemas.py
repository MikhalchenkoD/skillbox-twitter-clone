from typing import List, Union

from pydantic import BaseModel


class TweetData(BaseModel):
    tweet_data: str
    tweet_media_ids: Union[int, List[int]]
