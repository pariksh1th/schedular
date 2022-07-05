import { deleteDoc, doc } from "firebase/firestore";
import { AiFillDelete } from "react-icons/ai";
import { useAuth } from "../lib/context";

export default function CourseCard({ title, instructor, code, branch, id }) {
  const { db, courses, setCourses } = useAuth();

  function handelClick() {
    setCourses((prev) => {
      return prev.filter((fish) => fish.id !== id);
    });
    const docRef = doc(db, "courses", id);
    deleteDoc(docRef)
      .then(() => {
        console.log("deleted");
      })
      .catch((err) => console.log(err));
  }

  return (
    <div className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">{title}</h2>
        <p>Instructor: {instructor}</p>
        <p>Course code: {code}</p>
        <p>Branch: {branch}</p>
        <div className="card-actions  flex-row-reverse">
          <button className="btn btn-primary">Edit</button>
          <button className="btn btn-outline text-primary ">
            <AiFillDelete size="20" onClick={handelClick} />
          </button>
        </div>
      </div>
    </div>
  );
}
