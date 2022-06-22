import React from "react";

export default function CourseCard({ title, instructor, code, branch }) {
  return (
    <div className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">{title}</h2>
        <p>Instructor: {instructor}</p>
        <p>Course code: {code}</p>
        <p>Branch: {branch}</p>
        <div className="card-actions justify-end">
          <button className="btn btn-primary">Edit</button>
        </div>
      </div>
    </div>
  );
}
