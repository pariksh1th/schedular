import { BsPlusLg } from "react-icons/bs";
import { RiBookMarkFill } from "react-icons/ri";
import { BiTable } from "react-icons/bi";
import Link from "next/link";

export default function BottomBar() {
  return (
    <div className="navbar min-h-[5rem] bottom-0 justify-around px-16 fixed bg-base-100 shadow-inner">
      <div className="tooltip" data-tip="Subjects">
        <Link href="subject">
          <button className="btn btn-accent w-20 h-16 hover:rounded-2xl transition-all duration-500">
            <RiBookMarkFill size="40" />
          </button>
        </Link>
      </div>
      <div className="absolute top-[-1.6rem] btn btn-primary rounded-3xl w-24 h-14 ">
        <BsPlusLg size="34" />
      </div>
      <div className="tooltip" data-tip="Timetable">
        <Link href="timetable">
          <button className="btn btn-accent  w-20 h-16 hover:rounded-2xl transition-all duration-500">
            <BiTable size="40" />
          </button>
        </Link>
      </div>
    </div>
  );
}

// toggle btn-active on click
