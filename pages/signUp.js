import Link from "next/link";
import { useRef, useState } from "react";
import { useAuth } from "../lib/context";
import toast from "react-hot-toast";
import { useRouter } from "next/router";
import { FcGoogle } from "react-icons/fc";
import { addUser } from "../lib/addUser";

export default function SignUP() {
  const emailRef = useRef();
  const passwordRef = useRef();
  const passwordConfirmRef = useRef();
  const { signUp, googleLogin } = useAuth();
  const [error, setEroor] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();
  const notify = () => toast.error(error);

  async function handleSubmit(e) {
    e.preventDefault();
    if (passwordRef.current.value !== passwordConfirmRef.current.value) {
      return setEroor("Passwords do not match");
    }
    try {
      setEroor("");
      setLoading(true);
      await signUp(emailRef.current.value, passwordRef.current.value);
      // adding user to db with subject and timetable set to []
      addUser(emailRef.current.value);
      toast.success("Sign up successful🎉");
      router.push("/subject", undefined);
    } catch {
      setEroor("Failed to create an account");
    }

    setLoading(false);
  }

  return (
    <div className="hero min-h-[90vh]  px-12 bg-base-200">
      {error != "" && notify()}
      <div className="hero-content flex-col lg:flex-row-reverse px-24 lg:gap-[2rem]">
        <div className="text-center lg:text-left">
          <h1 className="text-5xl font-bold">Sign UP!</h1>
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
                <span className="label-text">Confirm Password</span>
              </label>
              <input
                ref={passwordConfirmRef}
                type="password"
                placeholder="confirm password"
                className="input input-bordered"
              />
              <label className="label">
                <Link href="/">
                  <a className="label-text-alt link link-hover">
                    Already have an account? Login
                  </a>
                </Link>
              </label>
            </div>
            <div className="form-control mt-6">
              <button
                disabled={loading}
                type="submit"
                className="btn btn-primary"
              >
                SignUP
              </button>
            </div>
          </form>
          <button
            disabled={loading}
            onClick={() => googleLogin()}
            className="btn btn-primary mb-4 mx-8"
          >
            <FcGoogle size="28" />
            <span className="px-2">Sign up with google</span>
          </button>
        </div>
      </div>
    </div>
  );
}
