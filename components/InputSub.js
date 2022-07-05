/* eslint-disable react/no-unknown-property */
import { Branch, Faculty } from "../lib/instituteInfo";
import { collection, addDoc, serverTimestamp } from "firebase/firestore";
import { useState } from "react";
import { useAuth } from "../lib/context";

export default function InputSub({ clickRef }) {
  const { db, currentUser } = useAuth();
  const [subValue, setSubValue] = useState({
    name: "",
    code: "",
    instructor: "Course Instructor",
    branch: "Select Branch",
    createdAt: serverTimestamp(),
  });

  const handelChange = (e) => {
    const { name, value } = e.target;
    setSubValue((prev) => {
      return {
        ...prev,
        [name]: value,
      };
    });
  };

  // pushs card values to database
  async function handelAdd() {
    try {
      const docRef = await addDoc(collection(db, "courses"), {
        ...subValue,
        userID: currentUser.uid,
        userEmail: currentUser.email,
      });
      console.log("Document written with ID: ", docRef.id);
    } catch (e) {
      console.error("Error adding document: ", e);
    }
  }

  return (
    <>
      <label
        for="my-modal-6"
        ref={clickRef}
        className="btn modal-button hidden"
      ></label>

      <input type="checkbox" id="my-modal-6" className="modal-toggle" />
      <div className="modal modal-bottom sm:modal-middle">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Add Subject!</h3>
          <form className="flex flex-col gap-2 m-4">
            <input
              onChange={handelChange}
              value={subValue.name}
              name="name"
              type="text"
              placeholder="Course Name"
              class="input input-bordered w-full "
            />
            <input
              onChange={handelChange}
              name="code"
              value={subValue.code}
              type="text"
              placeholder="Course Code"
              class="input input-bordered w-full "
            />
            <select
              value={subValue.instructor}
              name="instructor"
              onChange={handelChange}
              className="select select-bordered w-full "
            >
              <option disabled selected>
                Course Instructor
              </option>
              {/* <option value="avantika">Ms. Avantika </option>
              <option value="radhika">Ms. Radhika</option> */}
              {Faculty.map((opt, index) => (
                <option key={index} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
            <select
              value={subValue.branch}
              onChange={handelChange}
              name="branch"
              className="select select-bordered w-full "
            >
              <option disabled selected>
                Select Branch
              </option>
              {Branch.map((opt, index) => (
                <option key={index} value={opt.value}>
                  {opt.label}
                </option>
              ))}
            </select>
          </form>
          <div className="modal-action justify-start gap-4 flex-row-reverse">
            <button onClick={handelAdd}>
              <label for="my-modal-6" className="btn btn-primary px-8 ">
                Add
              </label>
            </button>
            <label for="my-modal-6" className="btn  px-4 ">
              Cancel
            </label>
          </div>
        </div>
      </div>
    </>
  );
}
