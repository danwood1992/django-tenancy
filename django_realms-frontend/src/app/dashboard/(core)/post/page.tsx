import AddPost from './_components/addpost'
import { type Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Dashboard',
}

export default function Dashboard() {
  return (
      <div>
      
      <AddPost />
      </div>
  )
}
