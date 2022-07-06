import React, { Component } from 'react'
import axios from 'axios'

export default class ListTweets extends Component {

    state = {
        tweets: []
    }

    async componentDidMount() {
        this.getTweets();
    }

    getTweets = async () => {
        const res = await axios.get('http://localhost:8082/alltweets')
        this.setState({
            tweets: res.data
        });
    }

    render() {
        return (
            <div className="row">
                {
                    this.state.tweets.map(tweet => (
                        <div className="col-md-4 p-2" key={tweet._id}>
                            <div className="card">
                                <div className="card-header d-flex justify-content-between">
                                    <h5>{tweet.title}</h5>
                                    
                                </div>
                                <div className="card-body">
                                    <p>
                                        {tweet.content}
                                    </p>
                                    <p>
                                        Retweets: {tweet.retweets}
                                    </p>
                                    <p>
                                        Likes: {tweet.favorites}
                                    </p>
                                </div>
                            </div>
                        </div>
                    ))
                }
            </div>
        )
    }
}
