import { Inter, Lexend } from 'next/font/google'
import Footer from '../../../components/dashboard/layout/footer'
import Nav from '../../../components/dashboard/layout/navigation'
import '@/styles/tailwind.css'
import { type Metadata } from 'next'
import React from 'react'


// map data to realmId

// use realmId to get realm data



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
      <div className="dash-container">
          {children}
      </div>
      <Footer />
    </div>
  );
}