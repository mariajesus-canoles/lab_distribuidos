package com.mingeso.backend.models;
import java.sql.Date;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Tweet {
    private Long id;
    private String content;
    private Long retweets;
    private Long favorites;

    @JsonCreator
    public Tweet(@JsonProperty("id") Long id,
    @JsonProperty("content") String content, 
    @JsonProperty("retweets") Long retweets, 
    @JsonProperty("favorites") Long favorites) {
        this.id = id;
        this.content = content;
        this.retweets = retweets;
        this.favorites = favorites;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public Long getRetweets() {
        return retweets;
    }

    public void setRetweets(Long retweets) {
        this.retweets = retweets;
    }

    public Long getFavorites() {
        return favorites;
    }

    public void setFavorites(Long favorites) {
        this.favorites = favorites;
    }
}



