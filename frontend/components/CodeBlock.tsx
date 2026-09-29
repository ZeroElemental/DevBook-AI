import type { RunLanguage } from "@/lib/types";

const RUNNABLE: Record<string, RunLanguage> = {
  python: "python",
  py: "python",
  python3: "python",
  javascript: "javascript",
  js: "javascript",
  node: "javascript",
  mjs: "javascript",
};

export function runLanguage(fence: string | null): RunLanguage | null {
  return fence ? (RUNNABLE[fence.toLowerCase()] ?? null) : null;
}

interface CodeBlockProps {
  language: string | null;
  code: string;
  complete: boolean;
}

export default function CodeBlock({ language, code }: CodeBlockProps) {
  return (
    <figure className="overflow-hidden rounded-md border bg-surface-2">
      <figcaption className="border-b px-3 py-1 font-mono text-xs text-muted-foreground">{language ?? "text"}</figcaption>
      <pre className="overflow-x-auto p-3 font-mono text-[13px] leading-[1.55]">
        <code>{code}</code>
      </pre>
    </figure>
  );
}
