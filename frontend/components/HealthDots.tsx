import type { Health } from "@/lib/types";

interface HealthDotsProps {
  health: Health | null;
}

type Level = "unknown" | "ok" | "warn" | "bad";

const COLOR: Record<Level, string> = {
  unknown: "bg-muted-foreground/40",
  ok: "bg-success",
  warn: "bg-warn",
  bad: "bg-destructive",
};

function levels(h: Health | null): [string, Level][] {
  if (!h) return [["Ollama", "unknown"], ["Models", "unknown"], ["Docker", "unknown"]];
  const models = h.models.chat.installed && h.models.embed.installed;
  const docker = h.docker.running && h.docker.images.python && h.docker.images.javascript;
  return [
    ["Ollama", h.ollama.ok ? "ok" : "bad"],
    ["Models", models ? "ok" : "bad"],
    ["Docker", docker ? "ok" : "warn"],
  ];
}

export default function HealthDots({ health }: HealthDotsProps) {
  return (
    <div className="ml-auto flex items-center gap-1.5" role="group" aria-label="Setup health">
      {levels(health).map(([name, level]) => (
        <span key={name} title={`${name}: ${level}`} aria-label={`${name}: ${level}`} className={`size-2 rounded-full ${COLOR[level]}`} />
      ))}
    </div>
  );
}
