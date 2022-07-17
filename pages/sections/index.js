import Link from "next/link";

export const sections = [
  { name: "Section 1" },
  { name: "Section 2" },
  { name: "Section 3" },
  { name: "Section 4" },
  { name: "Section 5" },
  { name: "Section 6" },
];

// context = paths

export default function Index() {
  return (
    <>
      <h1 className="text-5xl font-bold text-center my-2">Sections</h1>
      <div className="flex flex-wrap gap-4 justify-center m-4">
        {sections.map((val, ind) => {
          return (
            <div key={ind} className="card w-96 bg-base-100 shadow-xl ">
              <div className="card-body">
                <h2 className="card-title">{val.name}</h2>
                <p>If a dog chews shoes whose shoes does he choose?</p>
                <div className="card-actions justify-end">
                  <Link href={"/sections/" + val.name}>
                    <button className="btn btn-secondary btn-outline">
                      Add Subjects
                    </button>
                  </Link>
                </div>
              </div>
            </div>
          );
        })}
      </div>
      <div className="flex w-full justify-center">
        <Link href="/tables">
          <button className="btn btn-success btn-lg">Generate Timetable</button>
        </Link>
      </div>
    </>
  );
}
