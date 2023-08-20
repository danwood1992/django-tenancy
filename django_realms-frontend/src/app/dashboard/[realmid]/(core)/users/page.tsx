import { type Metadata } from 'next'
import UserTable from '@/components/dashboard/users/usertable'
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