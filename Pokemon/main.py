from class_combat import Combat
from class_poke import Pokemon
import tkinter as tk
import json


class MyApp(Combat):
    def __init__(self, master):
        self.master = master
        master.title("AutoMon")
        master.geometry("500x500")
        master.configure(bg="#F2F617")
        self.combat = Combat()
        self.lab_gold = tk.Label(master, text="gold " + str(self.combat.get_gold()))
        self.lab_gold.pack(side="top")
        self.lab_pk_ennemis = tk.Label(master, text="pokemon2")  # pokemon ennemis
        self.lab_pk_ennemis.pack(side="right", padx=10, pady=10)
        self.lab_pk_actuel = tk.Label(master, text="pokemon1")  # pokemon du joueur
        self.lab_pk_actuel.pack(side="left", padx=10, pady=10)
        self.but_loot_box = tk.Button(master, text="Loot Box 5$", command=self.open_loot_box)
        self.but_loot_box.pack()
        self.but_pokedex = tk.Button(master, text="Pokedex", command=self.open_pokedex)
        self.but_pokedex.pack()
        self.but_pc_box = tk.Button(master, text="Pc Box", command=self.open_pc_box)
        self.but_pc_box.pack()
        self.but_start_combat =tk.Button(master, text="start fight", command=self.start_combat)
        self.but_start_combat.pack()
        self.but_new_game = tk.Button(master, text="new game", command=self.new_game)
        self.but_new_game.pack(side="bottom")
        self.but_find_pk_sauvage = tk.Button(master, text="find wild pokemon", command=self.find_wild_pokemon)
        self.but_find_pk_sauvage.pack(side="right")
        # self.but_changer_pokemon = tk.Button(master, text="changer pokemon", command=self.changer_pokemon1)
        # self.but_changer_pokemon.pack(side="left")
        self.but_changer_left = tk.Button(master, text="<--", command=self.changer_left)
        self.but_changer_left.pack(side="left")
        self.but_changer_right = tk.Button(master, text="-->", command=self.changer_right)
        self.but_changer_right.pack(side="left")
    def open_pokedex(self):
        with open("pokedex.json", "r") as f:
            pokedex_list = json.load(f)
        pokedex_window = tk.Toplevel()
        pokedex_window.title("Pokedex")
        pokedex_window.geometry("200x200")
        listbox_pkdex = tk.Listbox(pokedex_window)
        listbox_pkdex.pack(fill="both", expand=True)
        for pokemon in pokedex_list:
            listbox_pkdex.insert("end", f"{pokemon['nom']} - {pokemon['type']}")
        self.combat.show_pokedex()

    def open_pc_box(self):
        with open("pc_box.json", "r")as f:
            pc_box_list = json.load(f)
            pc_box_window = tk.Toplevel()
            pc_box_window.title("Pc Box")
            pc_box_window.geometry("200x200")
            listbox_pc_box = tk.Listbox(pc_box_window)
            listbox_pc_box.pack(fill="both", expand=True)
            for pokemon in pc_box_list:
                listbox_pc_box.insert("end", f"{pokemon['nom']} - {pokemon['type']}")
        self.combat.show_pc_box()


    def update_pokemon_info(self):
        pokemon1 = self.combat.pokemon1
        pokemon2 = self.combat.pokemon2
        self.lab_pk_actuel.configure(text=f"{pokemon1.get_nom()} \n - PV: {pokemon1.get_pdv()} \n - Attaque: {pokemon1.get_p_att()} \n - Défense: {pokemon1.get_p_def()}", relief="raised", bg="green", font=("futura",15))
        self.lab_pk_ennemis.configure(text=f"{pokemon2.get_nom()} \n - PV: {pokemon2.get_pdv()} \n - Attaque: {pokemon2.get_p_att()} \n - Défense: {pokemon2.get_p_def()}", relief="raised", bg="red", font=("futura",15))

    def update_gold(self):
        self.lab_gold.configure(text="gold " + str(self.combat.get_gold()))
        

    def changer_pokemon1(self):
        self.combat.switch_pokemonWIP()
        self.update_pokemon_info()

    def changer_left(self):
        self.combat.switch_pokemonWIP()
        self.combat.scroll_left()
        self.update_pokemon_info()

    def changer_right(self):
        self.combat.switch_pokemonWIP()
        self.combat.scroll_right()
        self.update_pokemon_info()
    def find_wild_pokemon(self):
        self.combat.switch_pokemon2()
        self.update_pokemon_info()
    def start_combat(self):
        self.combat.tour_combat()
        self.update_pokemon_info()
        self.update_gold()
    def afficher_pk_info(self):
        pass
    def open_loot_box(self):
        self.combat.buy_loot_box()
        self.update_gold()

    def new_game(self):
        self.combat.del_pokedex()
        self.combat.del_pc_box()
        self.combat.starter_pokemon()
        self.combat.set_gold(0)
        self.update_gold()



root = tk.Tk()
myapp = MyApp(root)


root.mainloop()

