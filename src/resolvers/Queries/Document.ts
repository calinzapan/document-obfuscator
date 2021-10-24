import { extendType, intArg, nonNull } from 'nexus'
import { resolve } from 'path/posix'

export const post = extendType({
  type: 'Query',
  definition(t) {
    t.nonNull.list.field('getUserDocuments', {
      type: 'Document',
      resolve(_parent, _args, ctx) {
        return ctx.prisma.document.findMany({
          where: { authorId: ctx.userId },
        })
      },
    })
    t.field('getDocumentById', {
      type: 'Document',
      args: { id: nonNull(intArg()) },
      resolve(_parent, args, ctx) {
        return ctx.prisma.document.findFirst({ where: { id: args.id } })
      },
    })
  },
})
