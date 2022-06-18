import BottomBar from "../Components/BottomBar";
import Canvas from "../Components/Canvas";
import { useAuth } from "../lib/context";

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
