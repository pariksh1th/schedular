// Importing modules
import React, { useState, useEffect } from "react";

export function Api({ userId }) {
  // usestate for setting a javascript
  // object for storing and using data
  const [va, setVa] = useState({ name: "", email: "", lab: "" });

  // Using useEffect for single rendering
  useEffect(() => {
    // Using fetch to fetch the api from
    // flask server it will be redirected to proxy
    console.log(userId);
    fetch("/api/data/" + userId).then((res) =>
      res.json().then((data) => {
        // Setting a data from api
        setVa({
          name: data.name,
          lab: data.lab,
          email: data.userEmail,
        });
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>React and flask</h1>
        <p>{va.name}</p>
        <p>{va.email}</p>
        <p>{va.lab}</p>
      </header>
    </div>
  );
}

export default Api;
