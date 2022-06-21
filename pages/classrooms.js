import BottomBar from "../components/BottomBar";
import TableCanvas from "../components/TableCanvas";
import { useAuth } from "../lib/context";

export default function Timetable() {
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
      <TableCanvas />
      <BottomBar />
    </>
  );
}
