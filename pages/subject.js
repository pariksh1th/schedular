import BottomBar from "../components/BottomBar";
import Canvas from "../components/canvas";
import { useAuth } from "../lib/context";

export default function Subject() {
  const { currentUser } = useAuth;
  return (
    <>
      <Canvas />
      <BottomBar />
    </>
  );
}
