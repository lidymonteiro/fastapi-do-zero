def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá, Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'ada',
            'email': 'ada@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'ada',
        'email': 'ada@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'ada',
                'email': 'ada@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'margareth',
            'email': 'margareth@example.com',
            'password': 'secret-new',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'margareth',
        'email': 'margareth@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
