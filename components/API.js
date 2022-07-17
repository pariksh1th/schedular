// Importing modules
import React, { useState, useEffect } from "react";

export function Api({ userId }) {
  const [va, setVa] = useState({ name: "", email: "", lab: "" });
  useEffect(() => {
    console.log(userId);
    fetch("/api/data/" + userId).then((res) =>
      res.json().then((data) => {
        console.log(data["Section 1"]);

        setVa({
          name: data["Section 1"][0].name,
          lab: data["Section 2"][0].lab,
          email: data["Section 3"][0].useEmail,
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
