import { useState, useEffect } from "react";

export default function ModelTable() {
  // const [fetchValue, setFetch] = useState({
  //   CSE3A: [],
  //   CSE3B: [],

  //   CSE5A: [],
  //   CSE5B: [],
  // });

  var fetchValue = {};

  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch("/api/data/model")
      .then((res) =>
        res.json().then((data) => {
          console.log("working");
          console.log(data);

          fetchValue = data;
          setLoading(false);
          console.log("cse3a", fetchValue.CSE3A);
          console.log("cse3b", fetchValue.CSE3B);
          console.log("cse5a", fetchValue.CSE5A);
          console.log("cse5b", fetchValue.CSE5B);
        })
      )
      .catch((e) => console.log(e));
  }, []);

  if (loading) {
    return <h1>loading</h1>;
  }

  return <TableTemplete fetchValue={fetchValue} />;
}

const TableTemplete = (fetchValue) => {
  return (
    <div className="card w-[70%]  mx-auto my-4 shadow-lg">
      <div className="overflow-x-auto">
        <table className="table table-zebra w-[95%] mx-auto my-4">
          <thead>
            <tr>
              <th>DAY | TIME</th>
              <th>9 - 10:30</th>
              <th>10:45 - 12:45</th>
              <th>1:45 - 3:15</th>
              <th>3:30: - 4:30</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              {/* <th>Monday</th>
          {fetchValue.CSE3A[0].map((val, ind) => (
            <td key={ind}>{val}</td>
          ))} */}
            </tr>

            <tr>
              {/* {fetchValue.CSE3A[0].map((val, ind) => {
                <th key={ind}>{val}</th>;
              })} */}
              {/* <td>{fetchValue.CSE3A[0][1]}</td> */}
              <td>Here</td>
              <td>MA103L</td>
            </tr>

            <tr>
              <th>Wednesday</th>
              <td>CS102L</td>
              <td>CS/EC</td>
              <td>HS102Lab</td>
              <td>PH105Tut</td>
            </tr>
            <tr>
              <th>Thursday</th>
              <td>CS102L</td>
              <td>HS102Lab</td>
              <td>CS106L</td>
              <td>CSETut</td>
            </tr>
            <tr>
              <th>Friday</th>
              <td>CS106L</td>
              <td>HS102Lab</td>
              <td>PH105L</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};
