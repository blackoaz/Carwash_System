import React from 'react'
import { Link } from 'react-router-dom';
import Navbar  from './Navbar';

function Users() {
  return (
    <div>
        <Navbar/>
        <section className="container Body-table">
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>User type</th>
                    <th>Phone Number</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>first_name</td>
                    <td>last_name</td>
                    <td>user_type</td>
                    <td>phone_number</td>
                    <td>
                        <span className="action_btn" id="update-btn">
                            <Link to="/updateUser/: user.id" class="modal-btn">Update</Link>
                            <Link to="/deleteUser/: user.id" class="modal-btn">Delete</Link>
                        </span>
                    </td>

                </tr>
            </tbody>
        </table>
        <Link to="createUser"><button className="btn-create" id="create-btn">Create</button> </Link>
    </section>

    </div>
  )
}

export default Users