import React from 'react';
import Navbar  from './Navbar';

function Services() {
  return (
    <div>
        <Navbar />
        <div class="container Body-table">
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
                        <span class="action_btn" id="update-btn">
                            <a href="{% url 'updateService' service.uid %}" class="modal-btn">Update</a>
                            <a href="{% url 'deleteService' service.uid %}" class="modal-btn">Delete</a>
                        </span>
                    </td>
                </tr>
            </tbody>

        </table>
        <a href="{% url 'createService'%}"><button class="btn-create" id="create-btn">Create</button></a>
    </div>
    </div>
  )
}

export default Services