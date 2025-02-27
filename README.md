# Cyber Security Base 2025 - Project 1

LINK: https://github.com/levomaaa/csbproject1

## Installation

1. Install python and django if you don't already have them.
2. Clone this repository on your own computer and go to its root folder.
3. Create the database by command `python3 manage.py migrate` (might not be necessary).
4. Start the application by command `python3 manage.py runserver`.
5. You can log in with either using username: `kalle` password: `1234` or username: `pirkka` password: `0000`.

## FLAW 1 - Cross-Site Request Forgery (CSRF)

This flaw occurs in two different cases below.

Case 1:
- https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L11
- https://github.com/levomaaa/csbproject1/blob/main/pages/templates/index.html#L9

Case 2:
- https://github.com/levomaaa/csbproject1/blob/main/pages/views.py#L28
- https://github.com/levomaaa/csbproject1/blob/main/pages/templates/profile.html#L9

### Description

In `login_view` and `profile_view` functions the `@csrf_exempt` decorator disables CSRF protection. Also when the `{% csrf_token %}` is commented out in `index.html` and `profile.html`, the CSRF protection is completely disabled. This vulnerability allows attackers to use a victim's session to submit login requests, bypassing authentication and performing unauthorized actions.

### Fix

This flaw can be fixed by removing both `@csrf_exempt` decorators. Also, the `{% csrf_token %}` lines in the HTML templates should be uncommented. The exact source links for the flaws are provided above.

### Screenshots
- Before: https://github.com/levomaaa/csbproject1/tree/main/screenshots/flaw-1-before-1.png
- After: https://github.com/levomaaa/csbproject1/tree/main/screenshots/flaw-1-after-1.png