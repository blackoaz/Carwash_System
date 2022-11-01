import React from 'react';
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
                            <span class="action_btn" id="update-btn">
                                <a href="{% url 'update_body' category.id %}" class="modal-btn">Update</a>
                                <a href="{% url 'delete_body' category.id %}" class="modal-btn">Delete</a>
                            </span>
                        </td>

                    </tr>
                </tbody>

            </table>
            <a href="{% url 'create_body' %}"><button class="btn-create" id="create-btn">Create</button> </a>
        </div>



</div>
  )
}

export default Bodytype
