import React from 'react';
import Navbar  from './Navbar';

function Vehicles() {
  return (
    <div>
        <Navbar />
        <section class="container Body-table">
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
                        <span class="action_btn" id="update-btn">
                            <a href="/updateVehicle/:vehicle.id" class="modal-btn">Update</a>
                            <a href="/deleteVehicle/:vehicle.id" class="modal-btn">Delete</a>
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