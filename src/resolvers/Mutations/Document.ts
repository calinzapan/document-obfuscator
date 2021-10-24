import { intArg, extendType, nonNull, stringArg } from 'nexus'

export const document = extendType({
  type: 'Mutation',
  definition(t) {
    t.field('createDocument', {
      type: 'Document',
      args: { pictureUrl: nonNull(stringArg()) },
      resolve(_parent, args, ctx) {
        const data = {
          ...args,
          author: { connect: { id: ctx.userId } },
        }
        return ctx.prisma.document.create({ data })
      },
    })
    t.field('deleteDocument', {
      type: 'Document',
      args: { documentId: nonNull(intArg()) },
      resolve(_parent, args, ctx) {
        return ctx.prisma.document.delete({ where: { id: args.documentId } })
      },
    })
  },
})
