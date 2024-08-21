from django.urls import reverse
from .models import Member
import pytest
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password',
    [
        ('test@test.com', 'test'),
        ('test', 'test'),
        ('test.com', 'test'),
        ('@test.com', 'test'),
        ('test@test.com', ''),
        ('test', ''),
    ]
)
def test_create_member(email, password):
    member = Member.objects.create_user(email, password)
    assert member.email == email
    
@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password',
    [
        ('', 'test'),
        ('', ''),
    ]
)
def test_create_member_with_empty_email(email, password):
    with pytest.raises(ValueError) as err:
        Member.objects.create_user(email, password)
    assert str(err.value) == 'The Email field must be set'
    
    
@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password, expected_status_code, expected_user_count',
    [
        ('test@test.com', 'test', 201, 1),
        ('test2@test.com', 'test', 201, 1),
        ('test3@test.com', 'test', 201, 1),
        ('', 'test', 400, 0),
        ('test', 'test', 400, 0),
        ('test.com', 'test', 400, 0),
        ('@test.com', 'test', 400, 0),
        ('test@test.com', '', 400, 0),
        ('', '', 400, 0),
        ('test', '', 400, 0),
    ]
)
def test_user_registration(client, email, password, expected_status_code, expected_user_count):
    res = client.post(reverse('register'), data={'email': email, 'password': password}, format='json')
    assert res.status_code == expected_status_code
    assert Member.objects.count() == expected_user_count

@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password, expected_status_code',
    [
        ('test@test.com', 'test', 200),
        ('test2@test.com', 'test', 200),
        ('test3@test.com', 'test', 200),
        ('', 'test', 400),
        ('test', 'test', 400),
        ('test.com', 'test', 400),
        ('@test.com', 'test', 400),
        ('test@test.com', '', 400),
        ('', '', 400),
        ('test', '', 400),
    ]
)
def test_user_login(client, email, password, expected_status_code):
    if not email:
        return
    Member.objects.create_user(email=email, password=password)
    res = client.post(reverse('login'), data={'email': email, 'password': password}, format='json')
    assert res.status_code == expected_status_code
    if res.status_code == 200:
        assert res.data['user']['email'] == email
        assert res.data.get('tokens')

@pytest.mark.django_db
@pytest.mark.parametrize(
    'email, password, expected_status_code',
    [
        ('test@test.com', 'test', 205),
        ('test2@test.com', 'test', 205),
        ('test3@test.com', 'test', 205),
        ('', 'test', 400),
        ('test', 'test', 401),
        ('test.com', 'test', 401),
        ('@test.com', 'test', 205),
        ('test@test.com', '', 401),
        ('', '', 400),
        ('test', '', 401),
    ]
)
def test_user_logout(client, email, password, expected_status_code):
    if not email:
        return
    
    user = Member.objects.create_user(email=email, password=password)
    
    logout_url = reverse('logout')
    
    if '@' in email and '.' in email and password:
        refresh = RefreshToken.for_user(user)
        client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {refresh.access_token}'
        res = client.post(logout_url, data={'refresh_token': str(refresh)})
    else:
        res = client.post(logout_url, data={'refresh_token': 'invalid_token'})
    
    assert res.status_code == expected_status_code