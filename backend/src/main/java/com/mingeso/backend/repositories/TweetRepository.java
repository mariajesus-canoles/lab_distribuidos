package com.mingeso.backend.repositories;

import com.mingeso.backend.models.Tweet;
import java.util.List;

public interface TweetRepository {
    Tweet createTweet(Tweet TweetNew);
    List<Tweet> getAllTweets();
    List<Tweet> getTweetById(Long id);
    Long lastId();

}