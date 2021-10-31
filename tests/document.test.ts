import { document } from './../src/resolvers/Mutations/Document'
import { request, GraphQLClient } from 'graphql-request'
import {
  createUser,
  createDocument,
  deleteDocument,
  updateDocument,
} from './graphql'
import { getConfig } from './helpers'

let token = ''

const config = getConfig()

test('authenticated user can create a document', async () => {
  const user = {
    name: 'user 1',
    firstName: 'doe',
    email: 'u1@g.com',
    password: 'user 1',
  }
  const response: any = await request(config.url, createUser, user)
  token = response.signup.accessToken
  const graphQLClient = new GraphQLClient(config.url, {
    headers: {
      authorization: `Bearer ${token}`,
    },
  })

  const document: any = await graphQLClient.request(createDocument, {
    pictureUrl: 'https://picture.url/buletin',
  })

  expect(document).toHaveProperty('createDocument')
  expect(document.createDocument.id).toBeDefined()
})

test('same authenticated user can update a post', async () => {
  const graphQLClient = new GraphQLClient(config.url, {
    headers: {
      authorization: `Bearer ${token}`,
    },
  })
  const newImageUrl = 'https://picture.url/passport'

  const document: any = await graphQLClient.request(updateDocument, {
    documentId: 1,
    documentUrl: newImageUrl,
  })
  expect(document).toHaveProperty('updateDocument')
  expect(document.updateDocument.pictureUrl).toBe(newImageUrl)
})

test('same authenticated user can delete a post', async () => {
  const graphQLClient = new GraphQLClient(config.url, {
    headers: {
      authorization: `Bearer ${token}`,
    },
  })

  const document: any = await graphQLClient.request(deleteDocument, {
    id: 1,
  })

  expect(document).toBeDefined()
})
