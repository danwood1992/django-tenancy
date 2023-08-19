import { Inter, Lexend } from 'next/font/google'
import Footer from './footer'
import Nav from './navigation'
import '@/styles/tailwind.css'
import { type Metadata } from 'next'
import React from 'react'

export const metadata: Metadata = {
  title: {
    template: '%s - Django Realms',
    default: 'Django Realms - Tenancy made simple for small businesses',
  },
  description:
    'Most bookkeeping software is accurate, but hard to use. We make the opposite trade-off, and hope you don’t get audited.',
}

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

const lexend = Lexend({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-lexend',
})


export default function DashboardLayout({
  children, // will be a page or nested layout,
}: {
  children: React.ReactNode;
  title?: string;
}) {
  return (
    <div>
      <Nav />
      <div className="ml-80 flex-col h-screen ">
        
          {children}
       
      </div>
      <Footer />
    </div>
  );
}