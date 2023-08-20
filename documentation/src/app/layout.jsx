import { Inter } from 'next/font/google'
import localFont from 'next/font/local'
import clsx from 'clsx'

import { Providers } from '@/app/providers'
import { Layout } from '@/components/Layout'

import '@/styles/tailwind.css'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
})

// Use local version of Lexend so that we can use OpenType features
const lexend = localFont({
  src: '../fonts/lexend.woff2',
  display: 'swap',
  variable: '--font-lexend',
})

export const metadata = {
  title: {
    template: '%s - Docs',
    default: 'Django Realms Documentation',
  },
  description:
    'The official documentation for Django Realms.',
    authors: [{name: "Django Realms"}],
    manifest: "site.webmanifest",
    themeColor: "#ffffff",
    icons: {
        icon: [
            {
                url: "/favicon-32x32.png",
                type: "image/png",
                rel: "icon",
                sizes: "32x32",
            },
            {
                url: "/favicon-16x16.png",
                type: "image/png",
                rel: "icon",
                sizes: "16x16",
            },
        ],
        apple: {
            url: "/apple-touch-icon.png",
            type: "image/png",
            rel: "apple-touch-icon",
            sizes: "180x180",
        },
    },
    applicationName: "Django Realms Documentation",
    appleWebApp: {
        title: "Django Realms Documentation",
    },
}

export default function RootLayout({ children }) {
  return (
    <html
      lang="en"
      className={clsx('h-full antialiased', inter.variable, lexend.variable)}
      suppressHydrationWarning
    >
      <body className="flex min-h-full bg-white dark:bg-slate-900">
        <Providers>
          <Layout>{children}</Layout>
        </Providers>
      </body>
    </html>
  )
}
