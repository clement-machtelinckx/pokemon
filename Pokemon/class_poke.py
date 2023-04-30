import json

class Pokemon:
    def __init__(self, nom, type, lvl=0, pdv=100, p_att=0, p_def=0):
        self.__nom = nom
        self.type = type
        self.p_att = p_att
        self.p_def = p_def
        self.lvl = lvl
        self.__pdv = pdv

    def get_nom(self):
        return self.__nom

    def get_type(self):
        return self.type

    def get_p_att(self):
        return self.p_att

    def get_p_def(self):
        return self.p_def

    def get_lvl(self):
        return self.lvl

    def get_pdv(self):
        return self.__pdv

    def set_nom(self, new_nom):
        self.__nom = new_nom

    def set_p_att(self, new_p_att):
        self.p_att = new_p_att

    def set_p_def(self, new_p_def):
        self.p_def = new_p_def

    def set_lvl(self, new_lvl):
        self.lvl = new_lvl

    def set_pdv(self, new_pdv):
        self.__pdv = new_pdv

    def show_info_pokemon(self):    # montre les infos du pokemon
        print("nom : " + self.get_nom())
        print("lvl : " + str(self.get_lvl()))
        print("point de vie : " + str(self.get_pdv()))
        print("attaque : " + str(self.get_p_att()))
        print("defence : " + str(self.get_p_def()))

    def est_ko(self):  # verifie si le pokemon est ko
        if self.get_pdv() <= 0:
            print(self.get_nom() + " est ko")
            return True
        else:
            return False

    def save_pokedex(self):
        with open('pokedex.json', 'r') as f:
            pokedex_list = json.load(f)
            new_pokemon = self.pokemon_save()
            pokedex_list.append(new_pokemon)
        with open('pokedex.json', 'w') as f:
            json.dump(pokedex_list, f, indent=3)

    def pokemon_save(self):
        return {
            "nom": self.get_nom(),
            "type": self.get_type(),
            "lvl": self.get_lvl(),
            "pdv": self.get_pdv(),
            "p_att": self.get_p_att(),
            "p_def": self.get_p_def()
        }

    def add_pokemon(self):
        with open('pokemons.json', 'r') as f:
            pokemon_list = json.load(f)
            new_pokemon = {"nom": self.get_nom(), "type": self.get_type(), "lvl": self.get_lvl(), "pdv": self.get_pdv(), "p_att": self.get_p_att(), "p_def": self.get_p_def()}
            pokemon_list.append(new_pokemon)
        with open('pokemons.json', 'w') as f:
            json.dump(pokemon_list, f, indent=3)




