import pytest
from fastapi.methods import generate_error_response, generate_good_response, generate_tweet_data, generate_user_data


def test_generate_error_response():
    error_type = 'Test error'
    error_message = 'Test error message'
    response = generate_error_response(error_type, error_message)
    expected_response = {
        "result": False,
        "error_type": error_type,
        "error_message": error_message
    }
    assert response == expected_response


def test_generate_good_response():
    obj = 'user_id'
    data = 1
    response = generate_good_response(obj, data)
    expected_response = {
        "result": True,
        obj: data
    }
    assert response == expected_response


def test_generate_tweet_data():
    # Создаем заглушки для tweet и like
    class Tweet:
        def __init__(self, id, content, author, liked_by_users):
            self.id = id
            self.content = content
            self.author = author
            self.liked_by_users = liked_by_users

    class User:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    tweet_id = 123
    tweet_content = "This is a tweet"
    author = User(id=456, name="John Doe")
    like1 = User(id=789, name="Alice")
    like2 = User(id=890, name="Bob")
    liked_by_users = [like1, like2]

    # Создаем объекты tweet и вызываем функцию generate_tweet_data
    tweet = Tweet(id=tweet_id, content=tweet_content, author=author, liked_by_users=liked_by_users)
    tweet_data = generate_tweet_data(tweet)

    # Проверяем, что функция возвращает ожидаемый результат
    expected_result = {
        "id": tweet_id,
        "content": tweet_content,
        "author": {
            "id": author.id,
            "name": author.name
        },
        "likes": [
            {"user_id": like1.id, "name": like1.name},
            {"user_id": like2.id, "name": like2.name}
        ]
    }
    assert tweet_data == expected_result


def test_generate_user_data():
    # Создаем заглушки для user, follower и following
    class User:
        def __init__(self, id, name, followers, following):
            self.id = id
            self.name = name
            self.followers = followers
            self.following = following

    class Follower:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    class Following:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    # Создаем объекты user, follower и following и вызываем функцию generate_user_data
    follower1 = Follower(id=111, name="Follower 1")
    follower2 = Follower(id=222, name="Follower 2")
    followers = [follower1, follower2]

    following1 = Following(id=333, name="Following 1")
    following2 = Following(id=444, name="Following 2")
    following = [following1, following2]

    user_id = 123
    user_name = "John Doe"
    user = User(id=user_id, name=user_name, followers=followers, following=following)

    user_data = generate_user_data(user)

    # Проверяем, что функция возвращает ожидаемый результат
    expected_result = {
        "id": user_id,
        "name": user_name,
        "followers": [
            {"id": follower.id, "name": follower.name} for follower in followers
        ],
        "following": [
            {"id": follow.id, "name": follow.name} for follow in following
        ]
    }
    assert user_data == expected_result
