class Hero:

    def __init__(self, health=100, attack_damage=10, level=1):
        self.name = 'Hero'
        self.health = health
        self.attack_damage = attack_damage
        self.level = level
        self.inventory = []

    def attack(self, other):
        other.health -= self.attack_damage
        print(f'{self.name} attacked {other.name}, damage {self.attack_damage}')

    def find_item(self, item):
        message = f'Вы нашли {item}'
        self.inventory.append(item)
        print(message)

    def __str__(self):
        return f'{self.name} {self.health}'


class Mob:

    def __init__(self, name: str, health=100, attack_damage=10):
        self.name = name
        self.attack_damage = attack_damage
        self.health = health

    def attack(self, other):
        other.health -= self.attack_damage
        print(f'{self.name} нанес {self.attack_damage}')

    def __str__(self):
        return f'{self.__class__.__name__} {self.health}'


def main():
    def combat(first: Hero, second: Mob):
        print(f'Status:\n{first.name}: health - {first.health}')
        print(f'{second.name}: health - {second.health}')
        first.attack(second)
        second.attack(first)
        if first.health <= 0:
            return f'Победил {second.name}'
        if second.health <= 0:
            return f'Победил {first.name}'
        else:
            return combat(first, second)

    hero = Hero()
    mob = Mob('Ork', attack_damage=5)
    print('Начало схватки')
    print(combat(hero, mob))


if __name__ == '__main__':
    main()
