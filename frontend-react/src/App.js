import "./App.css";
import Home from "./components/Home";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Carwash from "./components/pages/Carwash";
import Bodytype from "./components/pages/Bodytype";
import Services from "./components/pages/Services";
import Vehicles from "./components/pages/Vehicles";
import Users from "./components/pages/Users";
import UnpaidVehicles from "./components/pages/UnpaidVehicles";
function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/carwash" element={<Carwash />} />
          <Route path="/bodytype" element={<Bodytype />} />
          <Route path="/services" element={<Services />} />
          <Route path="/vehicles" element={<Vehicles />} />
          <Route path="/users" element={<Users />} />
          <Route path="/unpaidvehicles" element={<UnpaidVehicles />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
