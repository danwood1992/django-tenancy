import Image from 'next/image'

import { Button } from '@/components/Button'
import { Container } from '@/components/Container'


export function CallToAction() {
  return (
    <section
      id="get-started-today"
      className="relative overflow-hidden bg-slate-200 py-32"
    >
      
      <Container className="relative">
        <div className="mx-auto max-w-lg text-center">
          <h2 className="font-display text-3xl tracking-tight text-slate-800 sm:text-4xl">
            Get started today
          </h2>
          <p className="mt-4 text-lg tracking-tight text-slate-800">
            It’s time to take control of your books. Buy our software so you can
            feel like you’re doing something productive.
          </p>
          <Button href="/register" color="green" className="mt-10">
            Sign up as a tenant
          </Button>
        </div>
      </Container>
    </section>
  )
}
