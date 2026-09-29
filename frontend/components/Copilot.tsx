import { Textarea } from "@/components/ui/textarea";
import type { Book } from "@/lib/types";

interface CopilotProps {
  book: Book | null;
}

export default function Copilot({ book }: CopilotProps) {
  const ready = book?.status === "ready";
  return (
    <section className="flex h-full flex-col bg-card">
      <header className="border-b px-4 py-2 text-sm font-semibold">Copilot</header>
      <div className="flex-1 overflow-auto p-4 text-sm text-muted-foreground">
        {book ? `Ask about ${book.title}` : "Open a book to start asking questions."}
      </div>
      <div className="border-t p-3">
        <Textarea placeholder="Ask about this book…" disabled={!ready} rows={2} />
      </div>
    </section>
  );
}
