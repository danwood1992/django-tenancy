import { type Metadata } from 'next'
import UserTable from './usertable'
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