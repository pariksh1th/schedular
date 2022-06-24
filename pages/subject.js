import DisplayCourse from "../components/DisplayCourse";
import { useAuth } from "../lib/context";

export default function Subject() {
  const { currentUser } = useAuth();
  return (
    <>{currentUser ? <DisplayCourse /> : <h1>Login access this page</h1>} </>
  );
}
