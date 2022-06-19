import BottomBar from "../components/BottomBar";
import Canvas from "../components/Canvas";
import { useAuth } from "../lib/context";

import { addDoc, collection } from "firebase/firestore";

export default function Subject() {
  const { currentUser } = useAuth();

  if (!currentUser) {
    return (
      <h1 className="text-3xl text-primary text-center">
        Login To Access this page
      </h1>
    );
  }

  return (
    <>
      <Canvas />

      <BottomBar />
    </>
  );
}
