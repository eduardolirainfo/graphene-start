from graphene import Field, Int, List, Mutation, ObjectType, Schema, String


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    email = String()


class CreateUser(Mutation):
    class Arguments:
        name = String()
        age = Int()
        email = String()

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, name, age, email):
        user = {
            'id': len(Query.users) + 1,
            'name': name,
            'age': age,
            'email': email,
        }
        Query.users.append(user)

        return CreateUser(user=user)


class UpdateUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
        name = String()
        age = Int()
        email = String()

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, user_id, name=None, age=None, email=None):
        user = None
        for u in Query.users:
            if u['id'] == user_id:
                user = u
                break
        if not user:
            return UpdateUser(user=None)

        if name is not None:
            user['name'] = name
        if age is not None:
            user['age'] = age
        if email is not None:
            user['email'] = email

        return UpdateUser(user=user)


class DeleteUser(Mutation):
    class Arguments:
        user_id = Int(required=True)

    user = Field(UserType)

    @staticmethod
    def mutate(root, info, user_id):
        user = None
        for idx, u in enumerate(Query.users):
            if u['id'] == user_id:
                user = u
                del Query.users[idx]
                break
        if not user:
            return None

        Query.users.remove(user)

        return DeleteUser(user=user)


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


class Mutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = Schema(query=Query, mutation=Mutation)

gql_query = """
query{
  user(userId: 1){
    id
    name
    age
    email
  }
}
"""


# gql = """
# query{
#   usersByMinAge(minAge: 35){
#     id
#     name
#     age
#     email
#   }
# }
# """

# gql = """
# mutation{
#   createUser(name: "Tom", age: 40, email: "demoy@gmail.com"){
#     user{
#       id
#       name
#       age
#       email
#     }
#   }
# }
# """


# gql_update = """
# mutation{
#   updateUser(userId: 1, name: "Update User",
#   age: 65, email: "demoxx@gmail.com"){
#     user{
#       id
#       name
#       age
#       email
#     }
#   }
# }
# """


gql_delete = """
mutation{
  deleteUser(userId: 1){
    user{
      id
      name
      age
      email
    }
  }
}
"""


if __name__ == '__main__':
    result = schema.execute(gql_query)
    print(result)
    result_2 = schema.execute(gql_delete)
    print(result_2)
    result = schema.execute(gql_query)
    if result.errors:
        print(result.errors)
    else:
        print(result.data)
