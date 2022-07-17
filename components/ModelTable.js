import { useState, useEffect } from "react";

const VALUES = {
  CSE3A: [
    ["EC105L", "CS207tut", "MA201tut", "HS206L", "t"],
    ["CS201L", "CS207l/EC105l", "CS207L", "MA201L"],
    ["CS202L", "CS202l", "L", "CS202tut"],
    ["CS201L", "CS202l", "CS207L", "EC105L"],
    ["MA201L", "CS207l/EC105l", "CS202L", "L"],
  ],
  CSE3B: [
    ["HS206L", "MA201tut", "CS202tut", "EC105L", "t"],
    ["HS206L", "CS202l", "CS201L", "L"],
    ["MA201L", "CS207l/EC105l", "CS202L", "L"],
    ["CS201L", "CS207l/EC105l", "MA201L", "L"],
    ["CS202L", "CS202l", "EC105L", "t"],
  ],
  CSE5A: [
    ["CS303l", "ElectiveL", "CS304L", "ElectiveTut"],
    ["CS303l", "BasketL", "CS304L", "CS309tut"],
    ["CS304tut", "ElectiveL", "CS309L", "L"],
    ["L", "BasketL", "CS309L", "BasketTut"],
    ["CS303tut", "CS303L", "CS303L", "t"],
  ],
  CSE5B: [
    ["Cloutut", "ElectiveL", "ClouL", "ElectiveTut"],
    ["t", "BasketL", "Com desiL", "Com gratut"],
    ["CS303l", "ElectiveL", "Com graL", "L"],
    ["Com desiL", "BasketL", "ClouL", "BasketTut"],
    ["CS303l", "Com graL", "L", "Com desitut"],
  ],
};

export default function ModelTable() {
  const [fetchValue, setFetch] = useState(VALUES);

  const [loading, setLoading] = useState(true);

  async function fetchData() {
    await fetch("/api/data/model")
      .then((res) =>
        res.json().then((data) => {
          console.log("working");
          console.log("data", data);
          setFetch({
            CSE3A: data["CSE3A"],
            CSE3B: data["CSE3B"],
            CSE5A: data["CSE5A"],
            CSE5B: data["CSE5B"],
          });
          console.log(fetchValue);
          setLoading(false);
        })
      )
      .catch((e) => console.log(e));
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      {loading ? (
        <h1>loading</h1>
      ) : (
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
                {fetchValue.CSE3A.map((val, ind) => {
                  console.log("valtop", val);
                  return (
                    <tr key={ind}>
                      {val.map((lec, i) => {
                        console.log("lec", lec);
                        return <th key={i}>{lec}</th>;
                      })}
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </>
  );
}
