class Shark:
    # Class variables animal_type = "fish"
    animal_type = "fish"
    location = "ocean"
    followers = 0
    # Método construtor com nome de variável de instância e idade
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Método com seguidores de variável de instânciap
    def set_followers (self, followers):
        self.followers
        followers
        print("This user has " + str(followers) + " followers")

nemo = Shark("Nemo",15)

nemo.set_followers(5)

print(nemo.followers)