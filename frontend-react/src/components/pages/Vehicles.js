import React from 'react';
import { Link } from 'react-router-dom';
import Navbar  from './Navbar';

function Vehicles() {
  return (
    <div>
        <Navbar />
        <section className="container Body-table">
        <table>
            <thead>
                <tr>
                    <th>Vehicle Category</th>
                    <th>Vehicle Registration</th>
                    <th>Created at</th>
                    <th>Updated at</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Category</td>
                    <td>registration</td>
                    <td>created</td>
                    <td>updated</td>
                    <td>
                        <span className="action_btn" id="update-btn">
                            <Link to="/updateVehicle/:vehicle.id" className="modal-btn">Update</Link>
                            <Link to="/deleteVehicle/:vehicle.id" className="modal-btn">Delete</Link>
                        </span>
                    </td>

                </tr>
            </tbody>

        </table>
    </section>
    </div>
  )
}

export default Vehicles