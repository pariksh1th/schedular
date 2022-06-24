import { useAuth } from "../lib/context";
import {
  collection,
  query,
  where,
  onSnapshot,
  deleteDoc,
} from "firebase/firestore";

export default function Testpage() {
  const { currentUser, db } = useAuth();

  // fetching subject data from firestore
  async function getCourseData() {}

  if (!currentUser) {
    return <h1>Login First </h1>;
  }

  return (
    <button className="btn btn-primary" onClick={getCourseData}>
      query
    </button>
  );
}
