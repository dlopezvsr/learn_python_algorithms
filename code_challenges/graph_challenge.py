class Friend:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def check_friend(self, friend_to_check):
        for friend in self.friends:
            if friend_to_check in friend.friends:
                return True
        return False


a = Friend("A")
b = Friend("B")
c = Friend("C")
d = Friend("D")

a.add_friend(b)
b.add_friend(c)
c.add_friend(d)

print(a.check_friend(d))
