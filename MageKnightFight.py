class Character:
    def __init__(self,name,health,lvl):
        self.name=name
        self.health=health
        self.lvl=lvl

    def attack(self,target):
        damage = self.lvl*2
        target.take_damage(damage)
        return damage

    def take_damage(self,damage):
        self.health= max(self.health-damage,0)

    def is_alive(self):
        return self.health>0
    def get_info(self):
        return f'\nname: {self.name} \nis alive: {'Yes' if self.is_alive() else 'No'}\nhealth: {self.health} \nlevel: {self.lvl}'
    
class Mage(Character):
    def __init__(self,name,health,lvl,mana=10):
        super(Mage,self).__init__(name,health,lvl)
        self.mana=mana
    def attack(self, target):
        damage = self.lvl
        target.take_damage(damage)
        self.mana+=2
        return damage
    def spell_attack(self, target):
        if self.mana>=5:
            damage = self.lvl + 10 #магический урон
            target.take_damage(damage)
            self.mana-=5
            return damage
        else:
            print("недостаточно маны для атаки")
            return 0
    def get_info(self):
        return f'\nname: {self.name} \nis alive: {'Yes' if self.is_alive() else 'No'}\nhealth: {self.health} \nlevel: {self.lvl}\nmana: {self.mana}'
    
class Knight(Character):
    def __init__(self, name, health, lvl, shield=7):
        super(Knight,self).__init__(name, health, lvl)
        self.shield=shield
    def attack(self,target):
        damage = self.lvl*2 + 8
        target.take_damage(damage)
        return damage
    def take_damage(self,damage):
        self.health= max(self.health-damage-self.shield , 0)
    def get_info(self):
        return f'\nname: {self.name} \nis alive: {'Yes' if self.is_alive() else 'No'}\nhealth: {self.health} \nlevel: {self.lvl}\nshield: {self.shield}'
hero = Knight("Герой", 100, 5, 10)
enemy = Mage("Враг", 60, 3, 20)
print("до боя:\n")
print(hero.get_info())
print(enemy.get_info())
damage = enemy.attack(hero)
print(f'{enemy.name} атаковал {hero.name} и нанес {damage} урона!')
damage = enemy.spell_attack(hero)
print(f'{enemy.name} атаковал заклинанием {hero.name} и нанес {damage} урона!')
print("после ударов врага: \n")
print(hero.get_info())
print(enemy.get_info())
damage = hero.attack(enemy)
print(f'{hero.name} атаковал {enemy.name} и нанес {damage} урона!')
print("после удара героя: \n")
print(hero.get_info())
print(enemy.get_info())