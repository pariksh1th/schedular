import { BsPlusLg } from "react-icons/bs";
import InputSub from "./InputSub";
import { useRef } from "react";
import { useAuth } from "../lib/context";

export default function BottomBar() {
  const clickRef = useRef();

  const { courses } = useAuth();
  return (
    <>
      <div className="navbar min-h-[5rem] bottom-0 justify-center  px-16 fixed bg-base-100 shadow-inner">
        <div
          onClick={() => {
            clickRef.current.click();
            console.log("click");
          }}
          className="absolute top-[-1.6rem]  btn btn-primary rounded-3xl w-24 h-14 "
        >
          <BsPlusLg size="34" />
        </div>
        <div className="flex justify-end w-full">
          <button
            className="btn btn-secondary"
            onClick={() => console.log(courses)}
          >
            Generate
          </button>
        </div>
      </div>
      <InputSub clickRef={clickRef} />
    </>
  );
}

// toggle btn-active on click
