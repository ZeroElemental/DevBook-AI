import type { Book } from "@/lib/types";

interface ReaderProps {
  book: Book | null;
  onPageChange(n: number): void;
}

export default function Reader({ book }: ReaderProps) {
  if (!book) {
    return (
      <div className="flex h-full items-center justify-center p-6">
        <div className="rounded-lg border-2 border-dashed p-10 text-center">
          <p className="font-semibold">Drop a programming book (PDF)</p>
          <p className="mt-1 text-sm text-muted-foreground">
            It stays on your machine. Parsed, indexed and ready to chat in a few minutes.
          </p>
        </div>
      </div>
    );
  }
  return <div className="h-full overflow-auto p-4 text-sm text-muted-foreground">{book.title}</div>;
}
