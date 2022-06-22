import { useAuth } from "../lib/context";
import { collection, query, where, getDocs } from "firebase/firestore";

export default function Testpage() {
  const { currentUser, db } = useAuth();

  async function makeQuery() {
    console.log("ckick");
    const q = query(
      collection(db, "courses"),
      where("userId", "==", currentUser.uid)
    );

    const querySnapshot = await getDocs(q);
    querySnapshot.forEach((doc) => {
      // doc.data() is never undefined for query doc snapshots

      //   console.log(doc.id, " => ", doc.data());
      console.log("test");
    });
  }

  if (!currentUser) {
    return <h1>Login First </h1>;
  }

  return (
    <button className="btn btn-primary" onClick={makeQuery}>
      query
    </button>
  );
}
