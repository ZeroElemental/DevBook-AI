import { MenuIcon } from "lucide-react";
import { Button } from "@/components/ui/button";
import HealthDots from "@/components/HealthDots";
import type { Book, Health } from "@/lib/types";

interface TopBarProps {
  book: Book | null;
  page: number;
  pageCount: number;
  health: Health | null;
  onOpenLibrary(): void;
  onGoToPage(n: number): void;
}

export default function TopBar({ book, page, pageCount, health, onOpenLibrary }: TopBarProps) {
  return (
    <header className="flex h-12 shrink-0 items-center gap-3 border-b bg-card px-3 text-sm">
      <Button variant="ghost" size="icon" aria-label="Open library" onClick={onOpenLibrary}>
        <MenuIcon className="size-4" />
      </Button>
      <span className="font-semibold">DevBook AI</span>
      <span className="truncate text-muted-foreground">{book?.title ?? "No book open"}</span>
      {book && (
        <span className="ml-auto font-mono text-xs text-muted-foreground">
          p. {page} / {pageCount}
        </span>
      )}
      <HealthDots health={health} />
    </header>
  );
}
