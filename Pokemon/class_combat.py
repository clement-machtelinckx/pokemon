from class_poke import Pokemon
import json
import random


class Combat:
    def __init__(self):
        self.gold = 0
        self.index_pokemon1 = 0
        with open('pc_box.json', 'r') as f:
            data = json.load(f)
            pokemon1_data = random.choice(data)

        with open('pokemons.json', 'r') as f:
            data = json.load(f)
            pokemon2_data = random.choice(data)
            self.pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['type'], pokemon1_data['lvl'],
                                    pokemon1_data['pdv'], pokemon1_data["p_att"], pokemon1_data['p_def'])
            self.pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['type'], pokemon2_data['lvl'],
                                    pokemon2_data['pdv'], pokemon2_data["p_att"], pokemon2_data['p_def'])
            self.initiative = random.randint(0, 1)

    def get_pokemon1(self):
        return self.pokemon1

    def get_pokemon2(self):
        return self.pokemon2

    def get_gold(self):
        return self.gold

    def set_gold(self, new_gold):
        self.gold = new_gold


    def gagner_gold(self):
        montant = random.randint(1, 3)
        self.gold += montant
        print("Vous avez gagné", montant, "pièces de monnaie !")

    def switch_pokemon2(self):
        with open('pokemons.json', 'r') as f:
            data = json.load(f)
            pokemon2_data = random.choice(data)
            self.pokemon2 = Pokemon(pokemon2_data['nom'], pokemon2_data['type'], pokemon2_data['lvl'],
                                    pokemon2_data['pdv'], pokemon2_data["p_att"], pokemon2_data['p_def'])
        print("Le Pokémon 2 a été changé avec succès !")

    def switch_pokemon1(self):
        with open("pc_box.json", "r") as f:
            data = json.load(f)
            pokemon1_data = random.choice(data)
            self.pokemon1 = Pokemon(pokemon1_data['nom'], pokemon1_data['type'], pokemon1_data['lvl'],
                                    pokemon1_data['pdv'], pokemon1_data["p_att"], pokemon1_data['p_def'])
        print("votre pokemon a été changer avec succés")



    def switch_pokemonWIP(self):
        self.load_pc_box()
        pokemon_data = self.pc_box[self.index_pokemon1]
        self.pokemon1 = Pokemon(pokemon_data['nom'], pokemon_data['type'], pokemon_data['lvl'], pokemon_data['pdv'],
                                pokemon_data['p_att'], pokemon_data['p_def'])
        print(f"Vous avez choisi {self.pokemon1.get_nom} !")

    def load_pc_box(self):
        with open("pc_box.json", "r") as f:
            self.pc_box = json.load(f)

    def scroll_right(self):
        self.index_pokemon1 = (self.index_pokemon1 + 1) % len(self.pc_box)
        print(f"Sélectionnez le pokemon {self.pc_box[self.index_pokemon1]['nom']} !")

    def scroll_left(self):
        self.index_pokemon1 = (self.index_pokemon1 - 1) % len(self.pc_box)
        print(f"Sélectionnez le pokemon {self.pc_box[self.index_pokemon1]['nom']} !")


    def miss_hit_crit(self):
        nb_alea = random.randint(0, 2)
        if nb_alea == 0:
            # print("miss")
            return 0
        elif nb_alea == 1:
            # print("hit")
            return 1
        elif nb_alea == 2:
            # print("crit")
            return 2

    def winner_is(self):
        if self.pokemon1.est_ko():
            print(self.pokemon2.get_nom() + " a gagner")
            self.pokemon2.show_info_pokemon()
            self.del_pk_from_box()
        elif self.pokemon2.est_ko():
            print(self.pokemon1.get_nom() + " a gagner")
            self.pokemon1.show_info_pokemon()
            self.gagner_gold()
            self.switch_pokemon2()
        else:
            return None

    def est_ko(self):
        if self.pokemon1.est_ko():
            return self.pokemon2
        elif self.pokemon2.est_ko():
            return self.pokemon1
        else:
            return None

    def attaque_pokemon1(self):
        m_h_c = self.miss_hit_crit()
        if m_h_c == 0:
            print(self.pokemon1.get_nom() + " rate")
            return None
        elif m_h_c == 1:
            if self.pokemon2.get_type() in self.check_faiblesse1():
                pdv_restant = self.pokemon2.get_pdv() - ((self.pokemon1.p_att * 2) - self.pokemon2.p_def)
                if pdv_restant >= 0:
                    self.pokemon2.set_pdv(pdv_restant)
                    print(self.pokemon1.get_nom() + " inflige " + str(
                        (self.pokemon1.p_att * 2) - self.pokemon2.p_def) + " super efficasse")
                    print("point de vie de " + self.pokemon2.get_nom() + " : " + str(self.pokemon2.get_pdv()))
                else:
                    self.pokemon2.set_pdv(0)
            else:
                pdv_restant = self.pokemon2.get_pdv() - (self.pokemon1.p_att - self.pokemon2.p_def)
                if pdv_restant >= 0:
                    self.pokemon2.set_pdv(pdv_restant)
                    print(self.pokemon1.get_nom() + " inflige " + str(self.pokemon1.p_att - self.pokemon2.p_def))
                    print("point de vie de " + self.pokemon2.get_nom() + " : " + str(self.pokemon2.get_pdv()))
                else:
                    self.pokemon2.set_pdv(0)
        elif m_h_c == 2:
            if self.pokemon2.get_type() in self.check_faiblesse1():
                pdv_restant = self.pokemon2.get_pdv() - (((self.pokemon1.p_att * 2) * 2) - self.pokemon2.get_p_def())
                if pdv_restant >= 0:
                    self.pokemon2.set_pdv(pdv_restant)
                    print(self.pokemon1.get_nom() + " inflige " + str(
                        ((self.pokemon1.p_att * 2) * 2) - self.pokemon2.p_def) + " super efficasse")
                    print("point de vie de " + self.pokemon2.get_nom() + " : " + str(self.pokemon2.get_pdv()))
                else:
                    self.pokemon2.set_pdv(0)
            else:
                pdv_restant = self.pokemon2.get_pdv() - ((self.pokemon1.p_att * 2) - self.pokemon2.p_def)
                if pdv_restant >= 0:
                    self.pokemon2.set_pdv(pdv_restant)
                    print(self.pokemon1.get_nom() + " inflige " + str((self.pokemon1.p_att * 2) - self.pokemon2.p_def))
                    print("point de vie de " + self.pokemon2.get_nom() + " : " + str(self.pokemon2.get_pdv()))
                else:
                    self.pokemon2.set_pdv(0)


        else:
            return None

    def attaque_pokemon2(self):
        m_h_c = self.miss_hit_crit()
        if m_h_c == 0:
            print(self.pokemon2.get_nom() + " rate")
            return None
        elif m_h_c == 1:
            if self.pokemon1.get_type() in self.check_faiblesse2():
                pdv_restant = self.pokemon1.get_pdv() - ((self.pokemon2.p_att * 2) - self.pokemon1.p_def)
                if pdv_restant >= 0:
                    self.pokemon1.set_pdv(pdv_restant)
                    print(self.pokemon2.get_nom() + " inflige " + str(
                        (self.pokemon2.p_att * 2) - self.pokemon1.p_def) + " super efficasse")
                    print("point de vie de " + self.pokemon1.get_nom() + " : " + str(self.pokemon1.get_pdv()))
                else:
                    self.pokemon1.set_pdv(0)
            else:
                pdv_restant = self.pokemon1.get_pdv() - (self.pokemon2.p_att - self.pokemon1.p_def)
                if pdv_restant >= 0:
                    self.pokemon1.set_pdv(pdv_restant)
                    print(self.pokemon2.get_nom() + " inflige " + str(self.pokemon2.p_att - self.pokemon1.p_def))
                    print("point de vie de " + self.pokemon1.get_nom() + " : " + str(self.pokemon1.get_pdv()))
                else:
                    self.pokemon1.set_pdv(0)
        elif m_h_c == 2:
            if self.pokemon1.get_type() in self.check_faiblesse2():
                pdv_restant = self.pokemon1.get_pdv() - (((self.pokemon2.p_att * 2) * 2) - self.pokemon1.p_def)
                if pdv_restant >= 0:
                    self.pokemon1.set_pdv(pdv_restant)
                    print(self.pokemon2.get_nom() + " inflige " + str(
                        ((self.pokemon2.p_att * 2) * 2) - self.pokemon1.p_def) + " super efficasse")
                    print("point de vie de " + self.pokemon1.get_nom() + " : " + str(self.pokemon1.get_pdv()))
                else:
                    self.pokemon1.set_pdv(0)
            else:
                pdv_restant = self.pokemon1.get_pdv() - ((self.pokemon2.p_att * 2) - self.pokemon1.p_def)
                if pdv_restant >= 0:
                    self.pokemon1.set_pdv(pdv_restant)
                    print(self.pokemon2.get_nom() + " inflige " + str((self.pokemon2.p_att * 2) - self.pokemon1.p_def))
                    print("point de vie de " + self.pokemon1.get_nom() + " : " + str(self.pokemon1.get_pdv()))
                else:
                    self.pokemon1.set_pdv(0)

        else:
            return None

    def check_faiblesse1(self):
        with open('faiblesses.json') as f:
            faiblesses = json.load(f)
            self.faiblesses_pokemon1 = []
            for faiblesse, types in faiblesses.items():
                if self.pokemon1.get_type() in types:
                    self.faiblesses_pokemon1.append(faiblesse)
        return self.faiblesses_pokemon1

    def check_faiblesse2(self):
        with open('faiblesses.json') as f:
            faiblesses = json.load(f)
            self.faiblesses_pokemon2 = []
            for faiblesse, types in faiblesses.items():
                if self.pokemon2.get_type() in types:
                    self.faiblesses_pokemon2.append(faiblesse)
        return self.faiblesses_pokemon2

    def save_pokedex2(self):
        with open('pokedex.json', 'r') as f:
            pokedex_list = json.load(f)
            new_pokemon = {"nom": self.pokemon2.get_nom(), "type": self.pokemon2.get_type(),
                           "lvl": self.pokemon2.get_lvl(), "pdv": self.pokemon2.get_pdv(),
                           "p_att": self.pokemon2.get_p_att(), "p_def": self.pokemon2.get_p_def()}
            for pokemon in pokedex_list:
                if pokemon["nom"] == new_pokemon["nom"]:
                    print("Ce Pokémon est déjà enregistré dans le pokedex.")
                    return
            pokedex_list.append(new_pokemon)
        with open('pokedex.json', 'w') as f:
            json.dump(pokedex_list, f, indent=3)

    def show_pokedex(self):
        with open("pokedex.json", "r") as f:
            pokedex_list = json.load(f)
            print(pokedex_list)

    def del_pokedex(self):
        with open("pokedex.json", "w") as f:
            json.dump([], f)

    def buy_loot_box(self):
        if self.get_gold() >= 5:
            rendu = self.get_gold() - 5
            self.set_gold(rendu)
            self.loot_box()
        else:
            None


    def loot_box(self):
        with open('pokemons.json', 'r') as f:
            data = json.load(f)
        random_index = random.randint(0, len(data) - 1)
        random_pokemon = data[random_index]
        with open("pc_box.json", "r") as f:
            pc_box = json.load(f)
            pc_box.append(random_pokemon)
        with open("pc_box.json", "w") as f:
            json.dump(pc_box, f, indent=3)
            print("bravo vous venez de trouver un " + random_pokemon["nom"])
        return random_pokemon["nom"]

    def show_pc_box(self):
        with open("pc_box.json", "r") as f:
            pc_box_list = json.load(f)
            print(pc_box_list)

    def del_pc_box(self):
        with open("pc_box.json", "w") as f:
            json.dump([], f)

    def del_pk_from_box(self):
        with open("pc_box.json", "r") as f:
            pc_box_list = json.load(f)
        pk_nom = self.pokemon1.get_nom()
        for i in range(len(pc_box_list)):
            if pc_box_list[i]["nom"] == pk_nom:
                del pc_box_list[i]
                break
        with open("pc_box.json", "w") as f:
            json.dump(pc_box_list, f, indent=3)

    def tour_combat(self):
        self.save_pokedex2()
        while not self.pokemon1.est_ko() and not self.pokemon2.est_ko():
            if self.initiative == 0:
                self.attaque_pokemon1()
                if self.pokemon2.est_ko():
                    break
                self.attaque_pokemon2()
                if self.pokemon1.est_ko():
                    break
                self.initiative = 1
            elif self.initiative == 1:
                self.attaque_pokemon2()
                if self.pokemon1.est_ko():
                    break
                self.attaque_pokemon1()
                if self.pokemon2.est_ko():
                    break
                self.initiative = 0
        self.winner_is()

    def starter_pokemon(self):
        starter = [{
            "nom": "Salameche",
            "type": "Feu",
            "lvl": 0,
            "pdv": 100,
            "p_att": 15,
            "p_def": 5
        },
            {
                "nom": "Carapuce",
                "type": "Eau",
                "lvl": 0,
                "pdv": 100,
                "p_att": 15,
                "p_def": 5
            },
            {
                "nom": "Bulbizarre",
                "type": "Plante",
                "lvl": 0,
                "pdv": 100,
                "p_att": 15,
                "p_def": 5
            }
        ]

        with open("pc_box.json", "w") as f:
            json.dump(starter, f, indent=3)

