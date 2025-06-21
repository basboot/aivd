from test import Test


class SuperTest(Test):
    def show(self):
        print("override")


if __name__ == '__main__':
    st = SuperTest(10)

    st.show()