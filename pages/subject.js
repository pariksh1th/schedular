import BottomBar from "../components/BottomBar";
import Canvas from "../components/canvas";
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
