import React from 'react';
import { Link } from 'react-router-dom';
import Navbar  from './pages/Navbar';


function Home() {
  return (
      <div>
      <Navbar />
      <div className="container functions">
        <h2>Carwash Management System</h2>
            <div className="row">
              <h2>Services</h2>
              <div className="col-md-3"><button type="button" className="btn1 btn-primary"><Link to='/carwash'>Carwash</Link></button></div>
              <div className="col-md-3"><button type="button" className="btn4 btn-primary">CARPET CLEANING</button></div>
              <div className="col-md-3"><button type="button" className="btn2 btn-primary">TOILET</button></div>
              <div className="col-md-3"><button type="button" className="btn3 btn-primary">WATER SALE</button></div>

            </div>
            <hr />
            {/* <Routes>
              <Route path='/carwash' element={<Carwash />}/>
            </Routes> */}
            <h2>Key Functions</h2>
            <div className="row updates">

                <div className="col-md-3"><Link to="/bodytype"><button>Body Type</button></Link></div>
                <div className="col-md-3"><Link to="/services"><button>Services</button></Link></div>
                <div className="col-md-3"><Link to="/vehicles"><button>Vehicles</button></Link></div>
                <div className="col-md-3"><Link to="/users"><button>Users</button></Link></div>
            </div>


        </div>

      </div>
  )
}

export default Home
