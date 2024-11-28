from abc import ABC, abstractmethod


class GameAI(ABC):
    builded_structures: list = []
    units: list = []
    map_center_position = '3425,5666'

    def turn(self):
        self.build_structures()
        self.collect_resources()
        self.build_units()
        self.attack()

    def collect_resources(self):
        for build in self.builded_structures:
            print(f'Collecting resources from {build}')

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    def attack(self):
        enemy = self.closest_enemy()

        if enemy:
            self.send_warriors(enemy['position'])
        else:
            self.send_scouts(self.map_center_position)
    
    @abstractmethod
    def send_scouts(self, enemy_position):
        pass

    @abstractmethod
    def send_warriors(self, enemy_position):
        pass

    def closest_enemy(self):
        return {'position': "1234234,325553"}


class OrcAI(GameAI):
    def build_structures(self):
        self.builded_structures = ['Farms', 'Barracks', 'Stronghold']
        print('🏗️ Build farms, then barracks, then stronghold')

    def build_units(self):
        self.units = ['Peon', 'Grunt']
        print('🏗️ Build peon and grunt')

    def send_scouts(self, enemy_position):
        print(f'🦸 Send scouts to this position: {enemy_position}')

    def send_warriors(self, enemy_position):
        print(f'🦸 Send warriors to this position: {enemy_position}')


class MonsterAI(GameAI):
    def collect_resources(self):
        print("❌ Monsters don't collect resources.")

    def build_structures(self):
        print("❌ Monsters don't build structures.")

    def build_units(self):
        print("❌ Monsters don't build units.")

    def send_scouts(self, enemy_position):
        print('Nothing to do')

    def send_warriors(self, enemy_position):
        print('Nothing to do')


if __name__ == '__main__':
    orc_ai = OrcAI()
    orc_ai.turn()

    monster_ai = MonsterAI()
    monster_ai.turn()