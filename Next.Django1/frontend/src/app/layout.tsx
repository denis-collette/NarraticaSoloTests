// frontend/src/app/layout.tsx
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import NavBar from "../components/NavBar"; // Ensure you have this component
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Narratica | Audiobook Streaming",
  description: "Stream and enjoy audiobooks from your favorite authors and narrators.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {/* Include the NavBar for consistent navigation */}
        <NavBar />
        {children}
      </body>
    </html>
  );
}
