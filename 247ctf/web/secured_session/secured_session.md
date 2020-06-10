# Secured session

Reference: https://blog.miguelgrinberg.com/post/how-secure-is-the-flask-user-session

1. Visit the website, open Inspection Tools and check the network session cookie, e.g.:
Cookie: session=eyJmbGFnIjp7IiBiIjoiTWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0ifX0.XtwyzA.6qygK90jCjmVSEqogJf75FiUxuo

2. Take the first part of session variable before the period (payload), and decode it in base 64:
>>> `base64.urlsafe_b64decode('eyJmbGFnIjp7IiBiIjoiTWpRM1ExUkdlMlJoT0RBM09UVm1PR0UxWTJGaU1tVXdNemRrTnpNNE5UZ3dOMkk1WVRreGZRPT0ifX0=')`
b'{"flag":{" b":"MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ=="}}'

3. Repeat the decode step:
>>> `base64.urlsafe_b64decode("MjQ3Q1RGe2RhODA3OTVmOGE1Y2FiMmUwMzdkNzM4NTgwN2I5YTkxfQ==")`
b'247CTF{FLAG_WAS_HERE}'