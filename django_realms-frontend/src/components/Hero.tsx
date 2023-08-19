
import { AnimatedLogo } from '@/components/AnimatedLogo'
import { Button } from '@/components/Button'
import { Container } from '@/components/Container'

export function Hero() {
  return (
    <Container className="relative pb-16 pt-20 text-center lg:pt-32 mt-10">
      
      {/* AnimatedLogo positioned absolutely to span the entire container */}
      <AnimatedLogo className="absolute top-0 left-0 w-full h-full z-0" />

      <h1 className="mx-auto max-w-4xl font-display text-5xl font-medium tracking-tight text-slate-900 sm:text-7xl z-10">
        {' '}
        
        <span className="relative whitespace-nowrap text-green-600 z-10">
          Kickstart
        </span>{' '}
        that SaaS project.
      </h1>

      <p className="mx-auto mt-6 max-w-2xl text-lg tracking-tight text-slate-700 z-10">
       An Opinionated template that simplifies the development of your multitnenant/SaaS project.
      </p>

      <div className="mt-10 flex justify-center gap-x-6 z-10">
        <Button href="/register">Documentation</Button>
        <Button href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" variant="outline">
          <svg
            aria-hidden="true"
            className="h-3 w-3 flex-none fill-green-600 group-active:fill-current z-10"
          >
            <path d="m9.997 6.91-7.583 3.447A1 1 0 0 1 1 9.447V2.553a1 1 0 0 1 1.414-.91L9.997 5.09c.782.355.782 1.465 0 1.82Z" />
          </svg>
          <span className="ml-3 z-10">Watch video</span>
        </Button>
      </div>
    </Container>
  )
}
