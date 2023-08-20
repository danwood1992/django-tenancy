"use client"
// Used the useState hook to store the form's email and password.
// Added an onSubmit event to the form to handle the submission and then use the authenticateUser mutation.
// Updated the text fields to update the state when their values change.
// Displayed an error message if the authenticateUser mutation throws an error.
// Displayed a loading indicator on the button during the authentication process.


import Link from 'next/link';
import useAuthenticateUser from '@/hooks/useAuthenticateUser';
import { Button } from '@/components/Button';
import { TextField } from '@/components/Fields';
import { Logo } from '@/components/Logo';
import { SlimLayout } from '@/components/SlimLayout';
import { type Metadata } from 'next';
import { useState } from 'react';
import router from 'next/router';


export default function Login() {
  const { authenticateUser, loading, error, data } = useAuthenticateUser();
  const [credentials, setCredentials] = useState({ email: '', password: '' });

  const handleSubmit = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    try {
      await authenticateUser({
        variables: {
          username: credentials.email,
          password: credentials.password,
        },
      });
      // Redirect or do some action after successful authentication if needed
      // Redirect to dashboard
      router.push('/[realmID]dashboard'); 
    } catch (err) {
      // Handle the error if needed
    }
  };

  return (
    <SlimLayout>
      <div className="flex">
        <Link href="/" aria-label="Home">
          <Logo className="h-10 w-auto" />
        </Link>
      </div>
      <h2 className="mt-20 text-lg font-semibold text-gray-900">
        Sign in to your account
      </h2>
      <p className="mt-2 text-sm text-gray-700">
        Don’t have an account?{' '}
        <Link
          href="/register"
          className="font-medium text-green-600 hover:underline"
        >
          Sign up
        </Link>{' '}
        for a free trial.
      </p>
      <form onSubmit={handleSubmit} className="mt-10 grid grid-cols-1 gap-y-8">
        <TextField
          label="Email address"
          name="email"
          type="email"
          autoComplete="email"
          required
          onChange={e => setCredentials(prev => ({ ...prev, email: e.target.value }))}
        />
        <TextField
          label="Password"
          name="password"
          type="password"
          autoComplete="current-password"
          required
          onChange={e => setCredentials(prev => ({ ...prev, password: e.target.value }))}
        />
        <div>
          <Button type="submit" variant="solid" color="green" className="w-full" disabled={loading}>
            {loading ? 'Signing in...' : 'Sign in'}
          </Button>
        </div>
        {error && <p className="text-red-500 mt-2">{error.message}</p>}
      </form>
    </SlimLayout>
  )
}
