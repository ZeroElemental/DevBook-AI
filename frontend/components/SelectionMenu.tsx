import { PlusIcon, SparklesIcon } from "lucide-react";

interface SelectionMenuProps {
  selection: { text: string; page: number; rect: DOMRect } | null;
  canExplain: boolean;
  explainDisabledReason?: string;
  onExplain(): void;
  onSendToNotes(): void;
}

export default function SelectionMenu({ selection, canExplain, explainDisabledReason, onExplain, onSendToNotes }: SelectionMenuProps) {
  if (!selection) return null;
  return (
    <div role="menu" className="absolute z-50 flex flex-col rounded-lg border bg-popover p-1 text-sm shadow-md">
      <button role="menuitem" disabled={!canExplain} title={explainDisabledReason} onClick={onExplain} className="flex items-center gap-2 rounded-md px-2 py-1 hover:bg-accent disabled:opacity-50">
        <SparklesIcon className="size-3.5" /> Explain
      </button>
      <button role="menuitem" onClick={onSendToNotes} className="flex items-center gap-2 rounded-md px-2 py-1 hover:bg-accent">
        <PlusIcon className="size-3.5" /> Send to Notes
      </button>
    </div>
  );
}
