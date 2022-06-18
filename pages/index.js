import Link from "next/link";
import { useRef, useState } from "react";
import { useAuth } from "../lib/context";

import toast from "react-hot-toast";
import { useRouter } from "next/router";

export default function Home() {
  const emailRef = useRef();
  const router = useRouter();
  const passwordRef = useRef();
  const { currentUser, login } = useAuth();
  const [error, setEroor] = useState("");
  const [loading, setLoading] = useState(false);
  const notify = () => toast.error(error);

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      setEroor("");
      setLoading(true);
      await login(emailRef.current.value, passwordRef.current.value);
      toast.success("Login successful🎉");
      router.push("/subject");
    } catch {
      setEroor("Failed to login");
    }

    setLoading(false);
  }

  return (
    <div className="hero min-h-[90vh]  px-12 bg-base-200">
      {error != "" && notify()}
      <div className="hero-content flex-col lg:flex-row-reverse px-24 lg:gap-[2rem]">
        <div className="text-center lg:text-left">
          <h1 className="text-5xl font-bold">Login now!</h1>
          <p className="py-6">
            Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda
            excepturi exercitationem quasi. In deleniti eaque aut repudiandae et
            a id nisi.
          </p>
        </div>
        <div className="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
          <form onSubmit={handleSubmit} className="card-body">
            <div className="form-control">
              <label className="label">
                <span className="label-text">Email</span>
              </label>
              <input
                ref={emailRef}
                type="text"
                placeholder="email"
                className="input input-bordered"
              />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Password</span>
              </label>
              <input
                ref={passwordRef}
                type="password"
                placeholder="password"
                className="input input-bordered"
              />
              <label className="label">
                <Link href="forgot">
                  <a className="label-text-alt link link-hover">
                    Forgot password?
                  </a>
                </Link>
                <Link href="/signUp">
                  <a className="label-text-alt link link-hover">SignUp</a>
                </Link>
              </label>
            </div>
            <div className="form-control mt-6">
              <button
                disabled={loading}
                type="submit"
                className="btn btn-primary"
              >
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
