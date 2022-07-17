import Link from "next/link";
import { useAuth } from "../lib/context";

export default function Navbar() {
  const { currentUser, logout } = useAuth();

  return (
    <div className="navbar bg-base-100 text-primary drop-shadow-md sticky top-0 z-20">
      <div className="flex-1">
        <Link href="/">
          <a className="btn btn-ghost normal-case text-2xl">schedular</a>
        </Link>
      </div>
      <div className="flex-none">
        {!currentUser && (
          <button className="btn btn-square btn-ghost">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              className="inline-block w-5 h-5 stroke-current"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"
              ></path>
            </svg>
          </button>
        )}

        {currentUser && (
          <button className="btn btn-primary" onClick={() => logout()}>
            Log Out
          </button>
        )}
      </div>
    </div>
  );
}
