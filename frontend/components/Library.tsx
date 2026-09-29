import { Sheet, SheetContent, SheetDescription, SheetHeader, SheetTitle } from "@/components/ui/sheet";
import type { Book } from "@/lib/types";

interface LibraryProps {
  open: boolean;
  onOpenChange(open: boolean): void;
  books: Book[];
  activeId: string | null;
  onOpenBook(id: string): void;
}

export default function Library({ open, onOpenChange, books, activeId, onOpenBook }: LibraryProps) {
  return (
    <Sheet open={open} onOpenChange={onOpenChange}>
      <SheetContent side="left" className="w-[360px]">
        <SheetHeader>
          <SheetTitle>Library</SheetTitle>
          <SheetDescription>Your books stay on this machine.</SheetDescription>
        </SheetHeader>
        <ul className="px-4 text-sm">
          {books.length === 0 && <li className="text-muted-foreground">No books yet.</li>}
          {books.map((b) => (
            <li key={b.id}>
              <button
                className={`w-full truncate rounded-md px-2 py-1.5 text-left hover:bg-accent ${b.id === activeId ? "bg-accent" : ""}`}
                onClick={() => onOpenBook(b.id)}
              >
                {b.title}
              </button>
            </li>
          ))}
        </ul>
      </SheetContent>
    </Sheet>
  );
}
