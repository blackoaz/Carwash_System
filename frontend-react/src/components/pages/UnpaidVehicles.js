import React,{ useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Navbar from "./Navbar";


function UnpaidVehicles() {
    const [sales, setSales] = useState([]);

    useEffect(() => {
        fetch("http://demo.localhost:8000/carwash/sales/", {
            method: "GET",
            headers: {
            "Content-Type": "application/json",
            Authorization: "Token 6b41e0fde56e76ccd6ab347e5fc56b74e5806298",
            },
        })
            .then((resp) => resp.json())
            .then((resp) => setSales(resp))
            .catch((error) => console.log(error));
        }, []);
  return (
    <div>
        <Navbar/>
        <div>
        <div class="wrapper">
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Service</th>
                    <th>Registration</th>
                    <th>Body Type</th>
                    <th>Attendant</th>
                    <th>Price</th>
                    <th>Commision</th>
                    <th>Payment</th>
                </tr>
            </thead>
            <tbody>
            {sales.map((sale,index)=>{
                        return(
                        <tr key={index}>
                        <td>{sale.created}</td>
                        <td>{sale.service.name}</td>
                        <td>{sale.vehicle}</td>
                        <td>{sale.body_type}</td>
                        <td>{sale.staff}</td>
                        <td>{sale.service.price}</td>
                        <td>{sale.commision}</td>
                        <td>
                          <span className="action_btn">
                            <a href="{% url 'Payment' sale.uid %}">PAY</a>
                          </span>
                        </td>
                      </tr>
                    )})}
                <tr>
                    <td colspan="5"><b>Total of Unpaid Vehicles</b></td>
                    <td  id="saletotal"></td>
                    <td  id="commisiontotal"></td>
                </tr>
            </tbody>

        </table>
    </div>
    <div class="row">
        <center>
            <Link to="/carwash"><button ><i class="fa fa-chevron-left"></i> Carwash</button></Link>
        </center>
    </div>

        </div>

    </div>
  )
}

export default UnpaidVehicles