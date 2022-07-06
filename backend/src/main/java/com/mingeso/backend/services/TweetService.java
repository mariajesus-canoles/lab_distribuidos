package com.mingeso.backend.services;

import com.mingeso.backend.models.Tweet;
import com.mingeso.backend.repositories.TweetRepository;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@CrossOrigin
@RestController
public class TweetService {
    private final TweetRepository tweetRepository;

    TweetService(TweetRepository tweetRepository) {
        this.tweetRepository = tweetRepository;
    }

    @PostMapping("/tweet")
    public Tweet createTweet(@RequestBody Tweet tweetNew){
        return tweetRepository.createTweet(tweetNew);
    }

    @GetMapping("/alltweets")
    public List<Tweet> getAllTweets() {
        return tweetRepository.getAllTweets();
    }
    @GetMapping("/tweet/{id}")
    public List<Tweet> getTweetById(@PathVariable Long id) {
        return tweetRepository.getTweetById(id);
    }
}