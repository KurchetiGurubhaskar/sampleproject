import React, { useState } from "react";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function Register() {
  const [student, setStudent] = useState({
    no: "",
    name: "",
    phone: "",
    email: "",
    address: "",
    city: "",
    state: "",
    country: "",
    pincode: "",
    dob: "",
    doj: ""
  });

  function handleChange(e) {
    setStudent({
      ...student,
      [e.target.name]: e.target.value
    });
  }

  function save(e) {
    e.preventDefault();
    toast.error("Student not saved. Implement API next.", {
      position: toast.POSITION.TOP_CENTER
    });
  }

  return (
    <React.Fragment>
      <p className="h2 text-center text-primary">Add Students</p>

      <div className="container mt-5">
        <div className="row">
          <div className="col-md-6">
            <div className="card">
              <div className="card-header text-center bg-primary">
                <p className="h1">ADD Students</p>
              </div>

              <div className="card-body">
                <form onSubmit={save}>
                  <input className="form-control" type="number" name="no" placeholder="Student ID" onChange={handleChange} />

                  <input className="form-control" type="text" name="name" placeholder="Student Name" onChange={handleChange} />

                  <input className="form-control" type="tel" name="phone" placeholder="Phone" onChange={handleChange} />

                  <input className="form-control" type="email" name="email" placeholder="Email" onChange={handleChange} />

                  <input className="form-control" type="text" name="address" placeholder="Address" onChange={handleChange} />

                  <input className="form-control" type="text" name="city" placeholder="City" onChange={handleChange} />

                  <input className="form-control" type="text" name="state" placeholder="State" onChange={handleChange} />

                  <input className="form-control" type="text" name="country" placeholder="Country" onChange={handleChange} />

                  <input className="form-control" type="text" name="pincode" maxLength={6} placeholder="Pincode" onChange={handleChange} />

                  <input className="form-control" type="date" name="doj" placeholder="Date of Join" onChange={handleChange} />

                  <button className="btn btn-primary btn-md rounded-pill mt-3">Add</button>

                  <Link to="/" className="btn btn-danger rounded-pill float-right mt-3">
                    Back
                  </Link>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}
