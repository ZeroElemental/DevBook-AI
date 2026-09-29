import ReactMarkdown from "react-markdown";
import rehypeHighlight from "rehype-highlight";
import remarkGfm from "remark-gfm";
import type { Citation } from "@/lib/types";

interface MarkdownProps {
  children: string;
  citations?: Citation[];
}

// Raw HTML is intentionally not rendered (no rehype-raw).
export default function Markdown({ children }: MarkdownProps) {
  return (
    <div className="prose-sm max-w-[72ch] leading-relaxed">
      <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeHighlight]}>
        {children}
      </ReactMarkdown>
    </div>
  );
}
