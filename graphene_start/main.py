from graphene import Field, List, Int, ObjectType, Schema, String


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    email = String()


class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    users_by_min_age = List(UserType, min_age=Int())
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
    def resolve_user(root, info, user_id):
        matched_users = [user for user in Query.users if user['id'] == user_id]

        return matched_users[0] if matched_users else None

    @staticmethod
    def resolve_users_by_min_age(root, info, min_age):
        matched_users = [
            user for user in Query.users if user['age'] >= min_age
        ]

        return matched_users if matched_users else None


schema = Schema(query=Query)

# gql = """
# query{
#   user(userId: 3){
#     id
#     name
#     age
#     email
#   }
# }
# """

gql = """
query{
  usersByMinAge(minAge: 35){
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
