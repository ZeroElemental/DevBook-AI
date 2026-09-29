import type { Book } from "@/lib/types";

interface NotesProps {
  book: Book | null;
}

export default function Notes({ book }: NotesProps) {
  return (
    <section className="flex h-full flex-col bg-card">
      <header className="border-b px-4 py-2 text-sm font-semibold">Notes</header>
      <p className="p-4 text-sm text-muted-foreground">
        {book ? "Highlight text → Send to Notes, or press Edit." : "Open a book to see its notes."}
      </p>
    </section>
  );
}
