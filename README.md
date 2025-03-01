# Cyber Security Base 2025 - Project 1

LINK: https://github.com/levomaaa/csbproject1

## Installation

1. Install python and django if you don't already have them.
2. Clone this repository on your own computer and go to its root folder.
3. Create the database by command `python3 manage.py migrate` (might not be necessary).
4. Start the application by command `python3 manage.py runserver`.
5. You can log in with either using username: `kalle` password: `1234` or username: `pirkka` password: `0000`.

## Flaw 1 - Cross-Site Request Forgery (CSRF)

This flaw occurs in two different cases below.

Case 1:
- https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L12
- https://github.com/levomaaa/csbproject1/blob/main/pages/templates/index.html#L10

Case 2:
- https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L30
- https://github.com/levomaaa/csbproject1/blob/main/pages/templates/profile.html#L10

### Description

In `login_view` and `profile_view` functions the `@csrf_exempt` decorator disables CSRF protection. Also when the `{% csrf_token %}` is commented out in `index.html` and `profile.html`, the CSRF protection is completely disabled. This vulnerability allows attackers to use a victim's session to submit login requests, bypassing authentication and performing unauthorized actions.

### Fix

This flaw can be fixed by removing both `@csrf_exempt` decorators. Also, the `{% csrf_token %}` lines in the HTML templates should be uncommented. The exact source links for the flaws and fixes are provided above.

### Screenshots

- [Before](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-1/flaw-1-before-1.png)
- [After](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-1/flaw-1-after-1.png)

## Flaw 2 - Broken Access Control

The flaw occurs here: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L31

### Description

The flaw exists in `profile_view` function. This flaw allows any user (logged in or not) to modify any users profiles by sending a `POST`request to `/profile/<username>/`. There is no check to verify that the logged-in user is editing their own profile.

### Fix

We add four lines of code to the `profile_view` which check that the profile editor is the logged-in profile owner. The fix is shown here: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L32.

### Screenshots

- [Before](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-2/flaw-2-before-1.png)
- [After 1/2](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-2/flaw-2-after-1.png)
- [After 2/2](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-2/flaw-2-after-2.png)

## Flaw 3 - Cryptographic Failures

I have my `SECRET_KEY`shown in the code and in Github. It's located here: https://github.com/levomaaa/csbproject1/blob/main/csbproject1/settings.py#L30.

### Description

The `SECRET_KEY`is hardcoded in `settings.py` which is a cryptographic flaw. When the `SECRET_KEY` is exposed, anyone who has access to it could potentially forge session cookies, CSRF tokens, etc. That way the attacker could access some other users profile information. 

### Fix
Remove the hardcoded `SECRET_KEY` from `settings.py`. Create a `.env`file in your project directory and put the `SECRET_KEY`to the file. Address the `.env` file from `settings.py`. The fix is shown here: https://github.com/levomaaa/csbproject1/blob/main/csbproject1/settings.py#L24.

### Screenshots

- [Before](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-3/flaw-3-before-1.png)
- [After](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-3/flaw-3-after-1.png)

## Flaw 4 - Security Misconfiguration

Djangos debug mode is enabled in `settings.py`. Located here: https://github.com/levomaaa/csbproject1/blob/main/csbproject1/settings.py#L33.

### Description

`DEBUG = True` in `settings.py`. This is a security risk because Djangos debug feuture shows error messages including database queries, stack traces, settings, etc, which can be exploited by attackers. This debug feature shared a lot of information which can also be sensitive. A screenshot below shows a small example what information you could get.

### Fix

Set the `DEBUG = True` in `settings.py` as `DEBUG = False`. Then the attacker is not able to see the debug feature. The fix is shown here: https://github.com/levomaaa/csbproject1/blob/main/csbproject1/settings.py#L34.

### Screenshots

- [Before](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-4/flaw-4-before-1.png)
- [After](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-4/flaw-4-after-1.png)

## Flaw 5 - Insecure Design

I don't have a limit for login attempts. Located here: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L13.

### Description

Method `login_view` in `views.py` does not contain any login limiting or brute force protection. Attackers can brute-force passwords by submitting multiple login requests without any limitations. This means that the account remains accessible even after multiple failed login attempts, unlike standard security practices that enforce lockouts. This could allow the attacker to gain unauthorized access by guessing weak passwords or using automated tools to do that.

### Fix 

We will fix this by tracking failed login attempts and limiting them to 5. After 5 failed login attempts the users account is locked for 30 seconds and after that they can try again. Error is shown after 5 failed attempts as shown in the screenshots. The fixes are shown in four parts below:
- Fix 1/4: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L11
- Fix 2/4: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L23
- Fix 3/4: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L34
- Fix 4/4: https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L39

### Screenshots

- [Before](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-5/flaw-5-before-1.png)
- [After](https://github.com/levomaaa/csbproject1/blob/main/screenshots/flaw-5/flaw-5-after-1.png)