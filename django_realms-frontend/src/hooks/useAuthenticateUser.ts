'use client'

import { gql, useMutation } from '@apollo/client';

const TOKEN_AUTH_MUTATION = gql`
    mutation TokenAuth($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
            token
        }
    }
`;

const useAuthenticateUser = () => {
    const [authenticateUser, { loading, error, data }] = useMutation(TOKEN_AUTH_MUTATION);

    return { authenticateUser, loading, error, data };
}

export default useAuthenticateUser;