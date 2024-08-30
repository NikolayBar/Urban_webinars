class Hero:

    def __init__(self, health=100, attack_damage=10, level=1):
        self.health = health
        self.attack_damage = attack_damage
        self.level = level
        self.inventory = []

    def attack(self, other):
        pass

    def find_item(self, item):
        message = f'Вы нашли {item}'
        self.inventory.append(item)
        print(message)


class Mob:

    def __init__(self, name: str, health=100, attack_damage=10):
        self.name = name
        self.attack_damage = attack_damage
        self.health = health

    def attack(self, other):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
