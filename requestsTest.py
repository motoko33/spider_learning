import requests

cookies = '_ga=GA1.2.1672237832.1508858571; _device_id=8ba8a39d1a7c0de49b4bd75462c25489; ' \
          '_octo=GH1.1.1671875421.1578733765; user_session=yqCBDryM4wK8CWA7gQl-WeWpF25D1lMzdJF5249A_n-G1BQS; ' \
          '__Host-user_session_same_site=yqCBDryM4wK8CWA7gQl-WeWpF25D1lMzdJF5249A_n-G1BQS; logged_in=yes; ' \
          'dotcom_user=motoko33; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; ' \
          '_gh_sess=n27S6EUZqfzq2AxJocLPh%2BBadb%2BQ6HxvsIyLPyLta%2BNKqFm%2FkgnTkJPjI72pud' \
          '%2FktystRpOElKnXsrso6HTq8LuNc3rhtagr6eC8xEWtWDuMHrUWApPHvMpc0uwf6' \
          '%2BgZ55rKlowNVKQmK0rnXh3rFS1gtgvpQ7GfjVyIt6dMIqI%3D--3cNu7LLk8naDMTyS--pHRyUbYdi0aZekU21kwoEw%3D%3D '
jar = requests.cookies.RequestsCookieJar()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) ' \
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('https://github.com/', cookies=jar, headers=headers)
print(r.text)