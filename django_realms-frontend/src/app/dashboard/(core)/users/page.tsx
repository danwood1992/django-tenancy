import { type Metadata } from 'next'
import UserTable from './_components/usertable'
export const metadata: Metadata = {
  title: 'Dashboard',
}

export default function Account() {
  return (
      <div>
        <UserTable />
      </div>
  )
}