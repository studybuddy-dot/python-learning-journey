#create class creator with attributes(name,username).Add method bio()

class Creator:
    def __init__(self, name, username):
        self.name = name
        self.username = username

    def bio(self):
        return f"{self.name} (@{self.username}) is a content creator."

# Example
c1 = Creator("John Doe", "johndoe123")
print(c1.bio())
