import BottomBar from "../components/BottomBar";
import Canvas from "../components/Canvas";
import { useAuth } from "../lib/context";

import { collection, query, where, onSnapshot } from "firebase/firestore";
import { useEffect, useState } from "react";
import CourseCard from "../components/CourseCard";

export default function Subject() {
  const { currentUser, db } = useAuth();
  const [courses, setCourses] = useState([]);
  if (!currentUser) {
    return (
      <h1 className="text-3xl text-primary text-center">
        Login To Access this page
      </h1>
    );
  }

  // fetching subject data from firestore
  const q = query(
    collection(db, "courses"),
    where("userID", "==", currentUser.uid)
  );

  const unsubscribe = onSnapshot(q, (querySnapshot) => {
    const temp = [];
    querySnapshot.forEach((doc) => {
      temp.push(doc.data());
    });
    setCourses(temp);
  });

  return (
    <>
      {courses.length == 0 && <Canvas />}
      <div className="flex flex-wrap gap-2 justify-center my-4 pb-12">
        {courses.map((sub, index) => {
          return (
            <CourseCard
              key={index}
              title={sub.name}
              instructor={sub.instructor}
              code={sub.code}
              branch={sub.branch}
            />
          );
        })}
      </div>

      <BottomBar />
    </>
  );
}
