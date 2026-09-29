// Mirrors backend/app/models.py. Keep both in sync.

export type BookStatus = "queued" | "parsing" | "embedding" | "ready" | "failed";

export interface Book {
  id: string;
  title: string;
  filename: string;
  size_bytes: number;
  page_count: number;
  chunk_count: number;
  status: BookStatus;
  progress: number;
  error_code: string | null;
  error: string | null;
  warning: string | null;
  created_at: string;
  updated_at: string;
}

export interface Selection {
  text: string;
  page: number;
}

export interface Citation {
  page: number;
  page_end: number;
  heading: string;
}

export interface ConversationSummary {
  id: string;
  title: string;
  updated_at: string;
}

export interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
  selection: Selection | null;
  citations: Citation[] | null;
  model: string | null;
  stopped: boolean;
  created_at: string;
}

export interface NotesDoc {
  content: string;
  version: string | null;
  updated_at: string | null;
}

export interface RunResult {
  stdout: string;
  stderr: string;
  exit_code: number | null;
  timed_out: boolean;
  duration_ms: number;
}

export interface Health {
  ollama: { ok: boolean; url: string; version: string | null };
  models: {
    chat: { name: string; installed: boolean };
    embed: { name: string; installed: boolean };
  };
  docker: { installed: boolean; running: boolean; images: { python: boolean; javascript: boolean } };
  checked_at: string;
}

export interface ChatRequestBody {
  book_id: string;
  conversation_id: string | null;
  message: string;
  selection: Selection | null;
}

export type ChatEvent =
  | { type: "meta"; conversation_id: string; model: string }
  | { type: "token"; text: string }
  | { type: "citations"; items: Citation[]; weak: boolean }
  | { type: "done"; message_id: number | null }
  | { type: "error"; code: string; message: string; hint: string | null };

export type RunLanguage = "python" | "javascript";
