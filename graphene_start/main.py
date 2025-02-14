from graphene import ObjectType, Schema, String


class Query(ObjectType):
    hello = String(name=String(default_value='mundo'))

    @staticmethod
    def resolve_hello(parent, info, name):
        return f'Olá {name}'


schema = Schema(query=Query)

gql = """
{
  hello(name: "GraphQL")
}
"""


if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)
