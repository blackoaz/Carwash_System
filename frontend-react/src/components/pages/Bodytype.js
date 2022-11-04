import React from 'react';
import { Link } from 'react-router-dom';
import Navbar  from './Navbar';

function Bodytype() {
  return (
    <div>
        <Navbar />
        <div className="container Body-table">
            <table>
                <thead>
                    <tr>
                        <th>Body Type</th>
                        <th>Created at</th>
                        <th>Updated at</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <td>name</td>
                        <td>created</td>
                        <td>updated</td>
                        <td>
                            <span className="action_btn" id="update-btn">
                                <Link to="{% url 'update_body' category.id %}" className="modal-btn">Update</Link>
                                <Link to="{% url 'delete_body' category.id %}" className="modal-btn">Delete</Link>
                            </span>
                        </td>

                    </tr>
                </tbody>

            </table>
            <Link to="{% url 'create_body' %}"><button className="btn-create" id="create-btn">Create</button> </Link>
        </div>



</div>
  )
}

export default Bodytype
