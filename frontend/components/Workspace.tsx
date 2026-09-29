"use client";

import { useState } from "react";
import { useDefaultLayout } from "react-resizable-panels";
import { ResizableHandle, ResizablePanel, ResizablePanelGroup } from "@/components/ui/resizable";
import Copilot from "@/components/Copilot";
import Library from "@/components/Library";
import Notes from "@/components/Notes";
import Reader from "@/components/Reader";
import TopBar from "@/components/TopBar";
import type { Book, Health } from "@/lib/types";

export default function Workspace() {
  const [books] = useState<Book[]>([]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [page, setPage] = useState(1);
  const [libraryOpen, setLibraryOpen] = useState(false);
  const [health] = useState<Health | null>(null);

  const { defaultLayout, onLayoutChanged } = useDefaultLayout({ id: "devbook-layout", storage: localStorage });

  const book = books.find((b) => b.id === activeId) ?? null;

  return (
    <div className="flex h-full flex-col">
      <TopBar
        book={book}
        page={page}
        pageCount={book?.page_count ?? 0}
        health={health}
        onOpenLibrary={() => setLibraryOpen(true)}
        onGoToPage={setPage}
      />
      <Library
        open={libraryOpen}
        onOpenChange={setLibraryOpen}
        books={books}
        activeId={activeId}
        onOpenBook={setActiveId}
      />
      <ResizablePanelGroup
        id="devbook-layout"
        orientation="horizontal"
        defaultLayout={defaultLayout}
        onLayoutChanged={onLayoutChanged}
        className="min-h-0 flex-1"
      >
        <ResizablePanel id="reader" defaultSize="45%" minSize="30%">
          <Reader book={book} onPageChange={setPage} />
        </ResizablePanel>
        <ResizableHandle aria-label="Resize reader and notes" />
        <ResizablePanel id="notes" defaultSize="25%" minSize="18%">
          <Notes book={book} />
        </ResizablePanel>
        <ResizableHandle aria-label="Resize notes and copilot" />
        <ResizablePanel id="copilot" defaultSize="30%" minSize="22%">
          <Copilot book={book} />
        </ResizablePanel>
      </ResizablePanelGroup>
    </div>
  );
}
