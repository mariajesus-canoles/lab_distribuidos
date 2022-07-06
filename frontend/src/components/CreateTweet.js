import React, { Component } from 'react'
import axios from 'axios'

export default class CreateTweet extends Component {

    state = {
        content: '',
        retweets: '',
        favorites: ''
    }



    onChangeContent = e => {
        this.setState({
            content: e.target.value
        })
    }
    onChangeFavorites = e => {
        this.setState({
            favorites: e.target.value
        })
    }
    onChangeRetweets = e => {
        this.setState({
            retweets: e.target.value
        })
    }
    onSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://localhost:8082/tweet', {
            content: this.state.content,
            retweets: this.state.retweets,
            favorites: this.state.favorites
        });
        //this.setState({ content: 'kdkddk' });

    }

    render() {
        return (
            <div className="row">
                <div className="col-md-4">
                    <div className="card card-body">
                        <h3>Create New Tweet</h3>
                        <form onSubmit={this.onSubmit}>
                            <div className="form-group">
                                <input
                                    className="form-control"
                                    value={this.state.content}
                                    type="text"
                                    onChange={this.onChangeContent}
                                    placeholder='Contenido'
                                />
                                <input
                                    className="form-control"
                                    value={this.state.favorites}
                                    type="text"
                                    onChange={this.onChangeFavorites}
                                    placeholder='Likes'
                                />
                                <input
                                    className="form-control"
                                    value={this.state.retweets}
                                    type="text"
                                    onChange={this.onChangeRetweets}
                                    placeholder='Retweets'
                                />
                            </div>
                            <button type="submit" className="btn btn-primary">
                                Save
                    </button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}
