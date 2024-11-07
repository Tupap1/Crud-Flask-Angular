import React from "react";
import Form from "./components/Form";
import Boton from "./components/Boton";
import "../src/app.css";

function App() {
  return (
    <div>
      <div className="row justify-content-center">
        <div className="col" id="hola">
          <h1>Bienvenido al Crud React + Flask</h1>
        </div>
      </div>

      <div className="row justify-content-center">
        <div className="col-3"  id="btn">
          <Boton text={"Registrar Datos"}></Boton>
        </div>
        <div className="col-3" id="btn">
          <Boton text={"Ver Datos"}></Boton>
        </div>
      </div>
    </div>
  );
}

export default App;
