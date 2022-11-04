import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Navbar from "./Navbar";
import "./Carwash.css";

function Carwash() {
  const [staffs, setStaffs] = useState([]);
  const [categories, setCategories] = useState([]);
  const [sales, setSales] = useState([]);
  //const [registrations, setRegistration] = useState('')
  const [plate, setPlate] = useState("");
  const [vehicle, setVehicle] = useState("");
  const [body, setBody] = useState("");
  const [staff, setStaff] = useState("");
  const [service, setService] = useState("");

  const plateSubmit = (event) => {
    event.preventDefault();
    let Nump = document.getElementById('numberPlate').value
    document.getElementById('numbplate').value = Nump;
  };
  let bodybtns = document.getElementsByClassName('body-btn1')

for(var i = 0; i < bodybtns.length; i++){
    bodybtns[i].addEventListener('click', function() {

       var categoryId= this.dataset.category
       var action = this.dataset.action
       console.log('categoryId:',categoryId, 'Action:',action)
       document.getElementById('bodyType').value = categoryId
    })
  }
  useEffect(() => {
    fetch("http://demo.localhost:8000/carwash/staffs/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 6b41e0fde56e76ccd6ab347e5fc56b74e5806298",
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setStaffs(resp))
      .catch((error) => console.log(error));
  }, []);
  useEffect(() => {
    fetch("http://demo.localhost:8000/carwash/categories/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Token 6b41e0fde56e76ccd6ab347e5fc56b74e5806298",
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setCategories(resp))
      .catch((error) => console.log(error));
  }, []);
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
  // useEffect(() => {
  //   fetch("http://demo.localhost:8000/carwash/sales/", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //       Authorization: "Token 6b41e0fde56e76ccd6ab347e5fc56b74e5806298",
  //     },
  //   })
  //     .then((resp) => resp.json())
  //     .then((resp) => setRegistration(resp))
  //     .catch((error) => console.log(error));
  // }, []);

  return (
    <div className="carwash-body">
      <Navbar />
      <div className="row navigation">
        <center>
          <Link to="/">
            <button className="menu-link">
              <i className="fa fa-chevron-left"></i> Main Menu
            </button>
          </Link>
          <Link to="{% url 'paidVehicles' %}">
            <button className="menu-sales">
              Sales <i className="fa fa-chevron-right"></i>
            </button>
          </Link>
        </center>
      </div>
      <div className="container-md border">
        <div className="row">
          <div className="col-md-8 border">
            <h3>Register Vehicle Details</h3>
            <div>
              <form>
                <input
                  className="search-enter"
                  type="text"
                  value={plate}
                  onChange={(e) => setPlate(e.target.value)}
                  placeholder="Enter Vehicle Number Plate"
                  id="numberPlate"
                />
                <input
                  type="submit"
                  value="Enter"
                  onClick={plateSubmit}
                  className="btn-enter"
                  id="submit-btn"
                />
              </form>
            </div>
            <div className="row wrapper1">
              {categories.map((category, index) => {
                return (
                  <div className="col-md-3 body-btn" key={index}>
                    <button className="body-btn1" data-category={ category.name } data-action="add" id="bodyinput">{category.name}</button>
                  </div>
                );
              })}
            </div>
            <div className="wrapper3">
              {staffs.map((staff, index) => {
                return (
                  <div className="washer" key={index}>
                    <button id="operator-btn">{staff.first_name}</button>
                  </div>
                );
              })}
            </div>

            <div className="wrapper4">
              <table className="table table-bordered">
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Service</th>
                    <th>Registration</th>
                    <th>Body Type</th>
                    <th>Price</th>
                    <th>Attendant</th>
                    <th>Commision</th>
                    <th>Payment</th>
                  </tr>
                </thead>
                <tbody>
                  {sales.slice(0, 2).map((sale, index) => {
                    return (
                      <tr key={index}>
                        <td>{sale.created}</td>
                        <td>{sale.service.name}</td>
                        <td>{sale.vehicle}</td>
                        <td>{sale.body_type}</td>
                        <td>{sale.service.price}</td>
                        <td>{sale.staff}</td>
                        <td>{sale.commision}</td>
                        <td>
                          <span className="action_btn">
                            <Link to="{% url 'Payment' sale.uid %}">PAY</Link>
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
            <div className="row wrapper5">
              <div className="N-page">
                <Link to="/unpaidvehicles">
                  <button>more</button>
                </Link>
              </div>
            </div>
          </div>

          <div className="col-md-4 border">
            <div className="wrapper6">
              <h3>Customer Details</h3>
              <form action="{% url 'register_sale' %}" method="POST">
                <div className="vhcl">
                  <label>Vehicle: </label>
                  <input type="text"
                  id="numbplate"
                  value={vehicle}
                  onChange={(e) => setVehicle(e.target.value)}
                  />
                </div>
                <br />
                <div className="vhcl">
                  <label htmlFor="Category">Body Type: </label>
                  <input type="text"
                  id="bodyType"
                  value={body}
                  onChange={(e) => setBody(e.target.value)}
                  />
                </div>
                <br />
                <div className="srvc">
                  <label htmlFor="Staff">Staff: </label>
                  <input type="text"
                  id="staff-washing"
                  value={staff}
                  onChange={(e) => setStaff(e.target.value)}
                  />
                </div>
                <br />

                <div className="srvc">
                  <label htmlFor="Service">Service: </label>
                  <input type="text"
                  value={service}
                  onChange={(e) => setService(e.target.value)}
                  />
                </div>
                <br />
                {/* <!-- <div class="vhcl">
                      <label for="Payment_status">Payment Status: </label>
                      {% render_field form.Payment_status id="staff-washing" %}
                  </div><br> --> */}

                <div class="wrapper7">
                  <div className="pay-sec">
                    <Link to="#">
                      <button>Cash</button>
                    </Link>
                  </div>
                  <div className="pay-sec">
                    <button>Mpesa</button>
                  </div>
                  <div className="pay-sec">
                    <button>Card</button>
                  </div>
                </div>
                <br />
                <div className="wrapper8">
                  <div className="p-btn">
                    <input type="submit" value="Add Sale" />
                  </div>
                  <div className="c-btn">
                    <input type="reset" value="clear" />
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Carwash;
