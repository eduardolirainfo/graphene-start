
from graphene_start.main import schema

def test_query_user():
        query = '''
        query {
            user(userId: 5) {
                id
                name
                age
                email
            }
        }
        '''
        result = schema.execute(query)
        assert not result.errors
        assert result.data['user']['id'] == 5
        assert result.data['user']['name'] == 'Eduardo'
        assert result.data['user']['age'] == 39
        assert result.data['user']['email'] == 'eduardolirainfo@gmail.com'
