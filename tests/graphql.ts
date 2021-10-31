export const createUser = /* GraphQL */ `
  mutation createUser(
    $name: String
    $firstName: String
    $email: String!
    $password: String!
  ) {
    signup(
      name: $name
      firstName: $firstName
      email: $email
      password: $password
    ) {
      ... on UserAlreadyExists {
        message
      }
      ... on AuthPayload {
        accessToken
        user {
          id
          name
        }
      }
    }
  }
`

export const login = /* GraphQL */ `
  mutation login($email: String!, $password: String!) {
    login(email: $email, password: $password) {
      ... on InvalidUser {
        message
      }
      ... on AuthPayload {
        accessToken
      }
    }
  }
`

export const createDocument = /* GraphQL */ `
  mutation createDocument($pictureUrl: String!) {
    createDocument(pictureUrl: $pictureUrl) {
      id
      pictureUrl
    }
  }
`

export const deleteDocument = /* GraphQL */ `
  mutation deleteDocument($id: Int!) {
    deleteDocument(documentId: $id) {
      id
    }
  }
`

export const updateDocument = /* GraphQL */ `
  mutation updateDocument($documentId: Int!, $documentUrl: String!) {
    updateDocument(documentId: $documentId, documentUrl: $documentUrl) {
      pictureUrl
    }
  }
`
