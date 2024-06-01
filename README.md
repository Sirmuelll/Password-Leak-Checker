Password Leak Checker

A Python-based password leak checker that uses the Have I Been Pwned API to determine if a given password has been compromised in a data breach.

Features
- Hashing: Uses SHA-1 to hash the password.
- Partial Hash Matching: Sends only the first five characters of the hashed password to the API to ensure privacy.
- API Integration: Checks the partial hash against the Have I Been Pwned database.
- Exact Match: Verifies the exact match of the hashed password from the API response.
- Leak Count: Returns the number of times the password has been found in breaches.

Installation
- Clone the Repository: git clone https://github.com/your-username/password-leak-checker.git
cd password-leak-checker

- Install Dependencies
- Usage: python password_leak_checker.py

Parameters
- password: The password you want to check.

Output
- The number of times the password has been found in breaches and a suggest to change or keep it.
