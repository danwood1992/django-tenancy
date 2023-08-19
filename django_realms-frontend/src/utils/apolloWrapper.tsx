"use client";

import {ApolloLink, HttpLink} from "@apollo/client";
import {
    ApolloNextAppProvider,
    NextSSRInMemoryCache,
    NextSSRApolloClient,
    SSRMultipartLink,
} from "@apollo/experimental-nextjs-app-support/ssr";
import React from "react";

const vastdesk_api_url = process.env.REACT_APP_VASTDESK_API_URL;

function makeClient() {
    const httpLink = new HttpLink({
        uri: vastdesk_api_url,
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
