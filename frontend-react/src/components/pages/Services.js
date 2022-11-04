import React from 'react';
import { Link } from 'react-router-dom';
import Navbar  from './Navbar';

function Services() {
  return (
    <div>
        <Navbar />
        <div className="container Body-table">
        <table>
            <thead>
                <tr>
                    <th>Service Type</th>
                    <th>Description</th>
                    <th>Body type</th>
                    <th>Price</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>name</td>
                    <td>description</td>
                    <td>category</td>
                    <td>price</td>
                    <td>available</td>
                    <td>
                        <span className="action_btn" id="update-btn">
                            <Link to="{% url 'updateService' service.uid %}" className="modal-btn">Update</Link>
                            <Link to="{% url 'deleteService' service.uid %}" className="modal-btn">Delete</Link>
                        </span>
                    </td>
                </tr>
            </tbody>

        </table>
        <Link to="{% url 'createService'%}"><button className="btn-create" id="create-btn">Create</button></Link>
    </div>
    </div>
  )
}

export default Services