'use client'
import { ApolloClient, InMemoryCache, ApolloLink, HttpLink } from "@apollo/client";
import {
    ApolloNextAppProvider,
    NextSSRInMemoryCache,
    NextSSRApolloClient,
    SSRMultipartLink,
} from "@apollo/experimental-nextjs-app-support/ssr";
import { setContext } from '@apollo/client/link/context';
import React from "react";

const api_url = process.env.NEXT_PUBLIC_DJANGO_REALMS_API_URL;

function getCsrfToken() {
    if (typeof window === 'undefined') return null; // Ensure you're on the client side
    const cookieValue = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
    return cookieValue ? cookieValue.split('=')[1] : '';
}

const authLink = setContext((_, { headers }) => {
    const token = getCsrfToken();
    return {
      headers: {
        ...headers,
        'X-CSRFToken': token || '',
      }
    };
});

const httpLink = new HttpLink({
    uri: api_url,
    credentials: 'include',
    fetchOptions: {
        cache: "no-store",
    },
});

function makeClient() {
    const client = new ApolloClient({
        link: authLink.concat(httpLink), 
        cache: new InMemoryCache(),
    });

    return new NextSSRApolloClient({
        cache: new NextSSRInMemoryCache(),
        link:
            typeof window === "undefined"
                ? ApolloLink.from([
                      new SSRMultipartLink({
                          stripDefer: true,
                      }),
                      httpLink,
                  ])
                : httpLink,
    });
}

export function ApolloWrapper({children}: React.PropsWithChildren<any>) {
    return (
        <ApolloNextAppProvider makeClient={makeClient}>
            {children}
        </ApolloNextAppProvider>
    );
}
