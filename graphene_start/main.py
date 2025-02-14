from graphene import Field, Int, ObjectType, Schema, String


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    email = String()


class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    users = [
        {
            'id': 1,
            'name': 'John',
            'age': 35,
            'email': 'demo1@gmail.com',
        },
        {
            'id': 2,
            'name': 'Jane',
            'age': 28,
            'email': 'demo2@gmail.com',
        },
        {
            'id': 3,
            'name': 'Alice',
            'age': 32,
            'email': 'demo3@gmail.com',
        },
        {
            'id': 4,
            'name': 'Bob',
            'age': 45,
            'email': 'demo4@gmail.com',
        },
    ]

    @staticmethod
    def resolve_user(parent, info, user_id):
        matched_users = [user for user in Query.users if user['id'] == user_id]

        return matched_users[0] if matched_users else None


schema = Schema(query=Query)

gql = """
query{
  user(userId: 3){
    id
    name
    age
    email
  }
}
"""


if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)
