import "./globals.css";
import type { ReactNode } from "react";

export const metadata = {
  title: "InfoHarbor Dashboard",
  description: "Personal information OS dashboard",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="bg-gray-950 text-gray-100">{children}</body>
    </html>
  );
}
