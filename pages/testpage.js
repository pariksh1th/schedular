import { useAuth } from "../lib/context";
import { collection, query, where, onSnapshot } from "firebase/firestore";

export default function Testpage() {
  const { currentUser, db } = useAuth();

  // fetching subject data from firestore
  async function getCourseData() {
    const q = query(
      collection(db, "courses"),
      where("userID", "==", currentUser.uid)
    );
    const unsubscribe = onSnapshot(q, (querySnapshot) => {
      const courses = [];
      querySnapshot.forEach((doc) => {
        courses.push(doc.data());
      });
      console.log(courses);
    });
  }

  if (!currentUser) {
    return <h1>Login First </h1>;
  }

  return (
    <button className="btn btn-primary" onClick={getCourseData}>
      query
    </button>
  );
}
