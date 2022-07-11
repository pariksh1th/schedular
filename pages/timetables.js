export default function timetables() {
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
              <th>Monday</th>
              <td>HS102L</td>
              <td>MA102Tut</td>

              <td>MA103L</td>
            </tr>

            <tr>
              <th>Tuesday</th>
              <td>PH105L</td>
              <td>CS/EC</td>
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
}
