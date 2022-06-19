import { db } from "./firebase";
import { addDoc, collection, getDoc } from "firebase/firestore";

export async function addUser(email) {
  try {
    const docRef = await addDoc(collection(db, "users"), {
      email: email,
      subjectList: [],
      timetableList: [],
    });

    console.log("Document written with ID: ", docRef.id);
  } catch (e) {
    console.error("Error adding document: ", e);
  }
}
