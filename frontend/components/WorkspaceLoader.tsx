"use client";

import dynamic from "next/dynamic";

// The workspace uses pdf.js and localStorage, so it renders in the browser only.
const Workspace = dynamic(() => import("./Workspace"), {
  ssr: false,
  loading: () => <div className="h-full bg-background" />,
});

export default function WorkspaceLoader() {
  return <Workspace />;
}
