import React, { Component } from 'react'
import axios from 'axios'

export default class CreateProduct extends Component {

    state = {
        name: '',
        expiration_date: '',
        category: false,
        price: '',
        delete: false
    }



    onChangename = e => {
        this.setState({
            name: e.target.value
        })
    }
    onChangePrice = e => {
        this.setState({
            price: e.target.value
        })
    }
    onChangeDate = e => {
        this.setState({
            expiration_date: e.target.value
        })
    }
    onSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://137.184.109.235:8082/product', {
            name: this.state.name,
            category: this.state.category,
            expiration_date: this.state.expiration_date,
            price: this.state.price,
            delete: this.state.delete
        });
        //this.setState({ name: 'kdkddk' });

    }

    render() {
        return (
            <div className="row">
                <div className="col-md-4">
                    <div className="card card-body">
                        <h3>Create New Product</h3>
                        <form onSubmit={this.onSubmit}>
                            <div className="form-group">
                                <input
                                    className="form-control"
                                    value={this.state.name}
                                    type="text"
                                    onChange={this.onChangename}
                                    placeholder='Nombre'
                                />
                                <input
                                    className="form-control"
                                    value={this.state.price}
                                    type="text"
                                    onChange={this.onChangePrice}
                                    placeholder='Precio'
                                />
                                <input
                                    className="form-control"
                                    value={this.state.expiration_date}
                                    type="text"
                                    onChange={this.onChangeDate}
                                    placeholder='yyyy-mm-dd'
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
