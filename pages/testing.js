import { useEffect, useState } from "react";
import { Api } from "../components/API";
import { useAuth } from "../lib/context";

export default function Testing() {
  const { currentUser } = useAuth();
  if (!currentUser) {
    return <h1>no user</h1>;
  }

  return <Api userId={currentUser.uid} />;
}
