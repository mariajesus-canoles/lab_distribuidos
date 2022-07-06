package com.mingeso.backend.repositories;

import com.mingeso.backend.models.Tweet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.sql2o.Connection;
import org.sql2o.Sql2o;

import java.util.List;

@Repository
public class TweetRepositoryImp implements TweetRepository{
    @Autowired
    private Sql2o sql2o;

    // List all Tweets
    @Override
    public List<Tweet> getAllTweets() {
        try(Connection conn = sql2o.open()){
            return conn.createQuery("select * from Tweet")
                .executeAndFetch(Tweet.class);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    // Get Tweet by Id
    @Override
    public List<Tweet> getTweetById(Long id){
        if(lastId() < id){
            System.out.println("El id ingresado no existe.");
            return null;
        }
        try(Connection conn = sql2o.open()){
            return conn.createQuery("select * from Tweet where id = :id")
                    .addParameter("id", id)
                    .executeAndFetch(Tweet.class);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    // Create Tweet
    @Override
    public Tweet createTweet(Tweet TweetNew){
        Long idNew=lastId()+1;
        try(Connection conn=sql2o.open()){
        String sql="INSERT INTO Tweet (id, content, retweets, favorites) values (:id, :content, :retweets, :favorites)";
        Long insertedId=conn.createQuery(sql,true)
        .addParameter("id",idNew)
        .addParameter("content",TweetNew.getContent())
        .addParameter("retweets",TweetNew.getRetweets())
        .addParameter("favorites",TweetNew.getFavorites())
        .executeUpdate().getKey(Long.class);
        TweetNew.setId(insertedId);
        return TweetNew;
        }catch(Exception e){
        System.out.println(e.getMessage());
        return null;
        }
    }
    public Long lastId(){
        Long lastId;
        try(Connection conn = sql2o.open()){
            lastId = Long.parseLong(String.valueOf(conn.createQuery("select max(Tweet.id) from Tweet", true)
            .executeScalar(long.class)));
            return lastId;
        }catch(Exception e){
            System.out.println(e.getMessage());
            return Long.valueOf(0);
        }
    }
}