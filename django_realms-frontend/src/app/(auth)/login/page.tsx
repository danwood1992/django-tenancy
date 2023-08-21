'use client'
import { gql } from '@apollo/client';
import { useMutation } from '@apollo/client/react';

import { useState } from 'react';

export const LOGIN_USER = gql`
  mutation LoginUser($username: String!, $password: String!) {
    loginuser(username: $username, password: $password) {
      status
      message
      success
      user {
        realmaccess {
          isPrimary
          realm {
            name
          }
          realmAccount {
            id
            firstName
          }
        }
      }
    }
  }
`;

export default function Login() {
  const [loginUser, { loading, error, data }] = useMutation(LOGIN_USER);
  // const router = useRouter();
  const [realmId, setRealmId] = useState<string | null>(null)


  const handleLogin = async (e: { preventDefault: () => void; target: { email: { value: any; }; password: { value: any; }; }; }) => {
    e.preventDefault();
    const email = e.target.email.value;
    const password = e.target.password.value;
    
    try {
      const { data } = await loginUser({
        variables: { username: email, password: password }
      });
  
      if (data.loginuser.success) {
        console.log("Login success:", data.loginuser.user);
  
        // Find the primary realm from the realmaccess array
        const primaryRealm = data.loginuser.user.realmaccess.find((access: any) => access.isPrimary);
      
        // If a primary realm is found, extract the id from the realm
        if (primaryRealm) {
          const realmId = primaryRealm.realmAccount.id;
          console.log("Primary realm found:", realmId);
         

          // Redirect to a path using the extracted realmId. Modify the path as per your requirement.
          window.location.href = `/dashboard/${realmId}/`;

        } else {
          console.error("No primary realm found");

        }
  
      } else {
        // Handle error message - data.loginuser.message
      }
    } catch (err) {
      console.error("Login error:", err);
    }
  };

  return (
    <>
    
      <div className="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-sm">
          <img
            className="mx-auto h-10 w-auto"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500"
            alt="Your Company"
          />
          <h2 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">
            Sign in to your account
          </h2>
        </div>

        <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form className="space-y-6" onSubmit={handleLogin}>
            <div>
              <label htmlFor="email" className="block text-sm font-medium leading-6 text-white">
                Email address
              </label>
              <div className="mt-2">
                <input
                  id="email"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div className="flex items-center justify-between">
                <label htmlFor="password" className="block text-sm font-medium leading-6 text-white">
                  Password
                </label>
                <div className="text-sm">
                  <a href="#" className="font-semibold text-indigo-400 hover:text-indigo-300">
                    Forgot password?
                  </a>
                </div>
              </div>
              <div className="mt-2">
                <input
                  id="password"
                  name="password"
                  type="password"
                  autoComplete="current-password"
                  required
                  className="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <button
                type="submit"
                className="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
              >
                Sign in
              </button>
            </div>
          </form>

          <p className="mt-10 text-center text-sm text-gray-400">
            Not a member?{' '}
            <a href="#" className="font-semibold leading-6 text-indigo-400 hover:text-indigo-300">
              Start a 14 day free trial
            </a>
          </p>
        </div>
      </div>
    </>
  )
}