<img src="https://upload.wikimedia.org/wikipedia/ro/thumb/1/18/Logo_UAIC_Iasi.svg/800px-Logo_UAIC_Iasi.svg.png" alt="Alexandru Ioan Cuza University Iasi" width="50"/>

<img src="https://scontent.fias1-1.fna.fbcdn.net/v/t1.6435-9/88174028_2757773254320944_3999542965591605248_n.png?_nc_cat=102&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=C6GR7nKCJxIAX_5Xx_l&_nc_oc=AQm9QcQuQiG_aspikN3X08UI8fRinhfHqIzWdmUPoKtpibBqtQVGkOy-HeZYZ9Xu-7i86rKtiI2SneNLu0D9K7G7&_nc_ht=scontent.fias1-1.fna&oh=28c9ea86ed06477b03ed4d994284b892&oe=619965E2" alt="Faculty of Computer Science Iasi" width="50"/>

# Document Obfuscator

**Diagrams:** [Document obfuscator class & usecase diagrams](https://app.diagrams.net/#G1ZvE9eP7MMW0dSso3u6s9COywi1e0YyxO)

Document Obfuscator is a project developed as a part of the [Advanced Software Engineering Techniques](https://profs.info.uaic.ro/~adiftene/Scoala/2022/ASET/index.html) course (2021-2022) at [Faculty of Computer Science Iasi](https://www.info.uaic.ro/en/home-page-2/), ["Alexandru Ioan Cuza" University Iasi](https://www.uaic.ro/en/).

**Course:** Advanced Software Engineering Techniques

**Professor:** Adrian Iftene

**Team:** Cobuz Cezar (MSD1), Luca Alexandru Gean (MSD1), Zapan Calin-George (MSD1);

**Coordinator:** Irimia Cosmin

**Contact information:** calin.zapan@gmail.com, cobuzcezar@gmail.com, alexandrugean.luca@gmail.com

## Lab 4 - 25.10.2021

### Design Patterns

**PubSub** - For realtime features (sharing documents, chats, notifications)

**Decorator** - Enhancing the behavior of a function without modifying the function itself - verify permissions, perform caching

**Observer** - For Detecting changes of state

**Bridge** - Implemented a middleware to handle the encryption/decryption of data before and after the next component in the pipeline is invoked.

**Prototype** - Provides a mechanism to copy the original object to a new object and then modify it according to our needs, used for creating Queries, Mutations, etc.

**Composite** - Creating a whole component called context that has access to multiple features, unifying them: pubsub mechanism, authorization mechanism, Prisma ORM etc.

**ORM** - Used Prisma ORM for the database communication

## Documentation

[📖 Document Obfuscator documentation](https://docs.google.com/document/d/1lzFYpHr9nZhxq4BpfmtOMLNQP-omLHmoRBRon-LCZoI/edit?usp=sharing) covers state of art, solution description.

## Modules

Each module has its own repository

[📱 Mobile App](https://github.com/CezarCobuz/document-obfuscator-app)

## Orchestrator Server

### 1. Clone this repo & install dependencies

Install Node dependencies:

`yarn` (recommended) or `npm install`

### 2. Set up the database

This uses a simple [SQLite database](https://www.sqlite.org/index.html).

**_Note_**: You can delete the migrations folder to create your own new migrations

To set up your database, run:

```sh
yarn db:save
yarn db:migrate
```

### 3. Generate Prisma Client (type-safe database client)

Run the following command to generate [Prisma Client](https://www.prisma.io/docs/reference/tools-and-interfaces/prisma-client/generating-prisma-client):

```sh
yarn generate:prisma
```

Now you can seed your database using the `seed` script from `package.json`:

```sh
yarn seed
```

### 4. Start the GraphQL server

Launch your GraphQL server with this command:

```sh
yarn dev
```

Navigate to [http://localhost:4002](http://localhost:4002) in your browser to explore the API of your GraphQL server in a [GraphQL Playground](https://github.com/prisma-labs/graphql-playground).

### 5. Using the GraphQL API

The schema that specifies the API operations of your GraphQL server is defined in [`./src/generated/schema.graphql`](./src/generated/schema.graphql). Below are a number of operations that you can send to the API using the GraphQL Playground.

Feel free to adjust any operation by adding or removing fields. The GraphQL Playground helps you with its auto-completion and query validation features.
