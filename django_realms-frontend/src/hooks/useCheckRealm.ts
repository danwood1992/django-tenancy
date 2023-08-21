'use client'
import { gql } from '@apollo/client';
import { useQuery } from '@apollo/client/react';

export const CHECK_REALM_QUERY = gql`
    query CheckRealm {
        viewer {
            realmaccess {
                isActive
                realm {
                    id
                }
            }
        }
    }
`;

export function useCheckRealm() {
    const { data, loading, error } = useQuery(CHECK_REALM_QUERY);
    
    
   

    return { data, loading, error };
}


