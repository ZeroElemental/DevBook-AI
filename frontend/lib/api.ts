import type { Book, Health } from "@/lib/types";

export const API = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8000";

export class ApiError extends Error {
  constructor(
    public status: number,
    public code: string,
    message: string,
    public hint: string | null,
  ) {
    super(message);
  }
}

async function toApiError(res: Response): Promise<ApiError> {
  const body = await res.json().catch(() => null);
  const detail = body?.detail;
  if (Array.isArray(detail)) {
    return new ApiError(res.status, "validation_error", detail[0]?.msg ?? "Invalid input", null);
  }
  if (detail?.code) return new ApiError(res.status, detail.code, detail.message, detail.hint ?? null);
  return new ApiError(res.status, "internal_error", "Something went wrong. Check the backend log.", null);
}

async function json<T>(path: string, init?: RequestInit): Promise<T> {
  let res: Response;
  try {
    res = await fetch(API + path, { ...init, signal: init?.signal ?? AbortSignal.timeout(30_000) });
  } catch (e) {
    if ((e as Error).name === "AbortError") throw e;
    throw new ApiError(0, "backend_unreachable", "Can't reach the DevBook backend.", null);
  }
  if (!res.ok) throw await toApiError(res);
  return res.status === 204 ? (undefined as T) : res.json();
}

export const api = {
  health: () => json<Health>("/health"),
  books: () => json<Book[]>("/books"),
  bookFileUrl: (id: string) => `${API}/books/${id}/file`,
};
