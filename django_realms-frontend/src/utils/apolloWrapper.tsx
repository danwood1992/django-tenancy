"use client";

import {ApolloLink, HttpLink} from "@apollo/client";
import {
    ApolloNextAppProvider,
    NextSSRInMemoryCache,
    NextSSRApolloClient,
    SSRMultipartLink,
} from "@apollo/experimental-nextjs-app-support/ssr";
import React from "react";

const api_url = process.env.NEXT_PUBLIC_DJANGO_REALMS_API_URL;

console.log("api_url", api_url);

function makeClient() {
    const httpLink = new HttpLink({
        uri: api_url,
        fetchOptions: {
            cache: "no-store",
        },
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

export function ApolloWrapper({children}: React.PropsWithChildren) {
    return (
        <ApolloNextAppProvider makeClient={makeClient}>
            {children}
        </ApolloNextAppProvider>
    );
}
