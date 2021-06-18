"""
    Structural:
      - Decorator pattern != python pattern
"""
# decorator design-pattern allow us to add behaviors of classes that made already without having to change that class

class Article:
    def show(self):
        print('All articles...')


class Login:
    def check_login(self, username, password):
        if username == 'shayan-9248' and  password == 'max123':
            return True


def outerLogin(func):
    def innerLogin():
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        l = Login()
        result = l.check_login(username, password)
        if result:
            func()
        else:
            print('Wrong username or password')
    return innerLogin


@outerLogin
def show_all_articles():
    a = Article()
    a.show()

show_all_articles()