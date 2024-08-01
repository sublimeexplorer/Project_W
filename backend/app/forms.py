from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member
        fields = (
            'first_name',
            'last_name',
            'email',
        )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
        
"""


1. Form Submission:
   - User fills out the registration form and clicks submit.
   - The browser sends a POST request to the server with the form data.

2. URL Routing:
   - Django's URL dispatcher matches the request URL to the appropriate view function.

3. View Function:
   - The view function associated with the registration URL is called.
   - It receives the request object containing the form data.

4. Form Processing:
   - The view creates an instance of the registration form (e.g., UserCreationForm) with the POST data.
   - Form validation is performed:
     a. Clean methods are called on each field.
     b. The form's clean() method is called for any cross-field validation.

5. Form Validation:
   - If the form is not valid, the view typically re-renders the form with error messages.
   - If the form is valid, processing continues.

6. User Creation:
   - The form's save() method is called.
   - This method typically creates a User instance but doesn't save it to the database yet.

7. Password Handling:
   - The password is hashed using Django's password hashing system.

8. Database Transaction:
   - A database transaction is started (if not already in one).

9. User Saving:
   - The User instance is saved to the database.
   - This creates a new record in the auth_user table (or your custom user table).

10. Signal Dispatch:
    - The post_save signal for the User model is sent.
    - Any receivers of this signal are called (e.g., to create a user profile).

11. Additional Processing:
    - Any additional user-related objects are created (e.g., UserProfile).
    - These are also saved to their respective database tables.

12. Transaction Commit:
    - If all operations are successful, the database transaction is committed.
    - If an error occurs, the transaction is rolled back.

13. Login (Optional):
    - Some applications automatically log in the user after registration.
    - This involves creating a session for the user.

14. Response Generation:
    - The view generates a response, typically a redirect to a success page or the user's new profile page.

15. Response Sent:
    - The server sends the HTTP response back to the user's browser.

16. Browser Action:
    - The user's browser receives the response and acts accordingly (e.g., redirecting to a new page).

Throughout this process, Django's ORM (Object-Relational Mapping) handles the translation between Python objects and database operations, ensuring that the user data is properly stored in the database.

This process can be customized at various points, for example, to add email verification, handle profile creation differently, or integrate with external services. The exact steps may vary slightly depending on your specific implementation and requirements.
"""