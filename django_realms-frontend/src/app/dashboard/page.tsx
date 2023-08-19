import Stats from './stats'
import { type Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Dashboard',
}

export default function Dashboard() {
  return (
      <div>
      
      <Stats />
      </div>
  )
}
