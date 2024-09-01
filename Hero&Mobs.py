class Hero:

    def __init__(self, health=100, attack_damage=10, level=1):
        self.name = 'Hero'
        self.health = health
        self.attack_damage = attack_damage
        self.level = level
        self.inventory = []

    def attack(self, other):
        if self.health > 0:
            other.health -= self.attack_damage
            return f'{self.name}({self.health}) наносит {self.attack_damage} урона'
        else:
            return f'{self.name} погиб!'

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
        if self.health > 0:
            other.health -= self.attack_damage
            return f'{self.name}({self.health}) наносит {self.attack_damage} урона'
        else:
            return f'{self.name} повержен!'

    def __str__(self):
        return f'{self.__class__.__name__} {self.health}'


def main():

    def combat(first: Hero, second: Mob):
        while first.health > 0 and second.health > 0:
            print(first.attack(second))
            print(second.attack(first))
        win = first.name if second.health <= 0 else second.name
        return f'Победил {win}'

    hero = Hero()
    mob = Mob('Ork', attack_damage=20)
    print('Начало схватки\n', '-' * 30)
    print(f'Status: \n{hero.name}: health - {hero.health}', end=' против ')
    print(f'{mob.name}: health - {mob.health}')
    print(combat(hero, mob))


if __name__ == '__main__':
    main()
