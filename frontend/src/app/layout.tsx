import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Planwise",
  description: "Automated routine organizer with priority logic and Google Calendar integration.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
