from game import Person,bcolors
from magic import spell
from inventory import items
import random



# magic
fire=spell('fire',10,300,'black')
thunder=spell('thunder',15,350,'black')
quake=spell('quake',12,325,'black')
cure=spell('cure',15,340,'white')
cura=spell('cura',20,400,'white')

# items
potion=items("potion","potion","Heals 100 hp",100)
hipotion=items("Hi-Potion","potion","Heals 150 hp",150)
super_potion=items("Super-Potion","potion","Heals 500 hp",500)
elixir=items("elxir","elixir","fully restores HP/MP of one party member",99999)
mega_elixir=items("mega elixir","elixir","fully restores HP/MP of party ",99999)

grenade=items("Grenade","attack","Deals 500 damage ",500)
player_spells=[fire,thunder,quake,cure,cura]
enemy_spells=[fire,thunder,cure]
player_items=[{"item":potion,"quantity":5},{"item":hipotion,"quantity":5},
             {"item":super_potion,"quantity":1},{"item":elixir,"quantity":2},
             {"item":mega_elixir,"quantity":1},{"item":grenade,"quantity":2}]
# players
player0 =Person("VALOS    ",3060,65,200,34,player_spells,player_items)
player1=Person("ROBOT    ",3460,65,180,34,player_spells,player_items)
player2=Person("BATMAN   ",4160,65,210,34,player_spells,player_items)
players=[player0,player1,player2]

#enemies
enemy1=Person("IMP  ",500,65,325,25,enemy_spells,[])
enemy2=Person("MAGUS ",6000,65,700,25,enemy_spells,[])
enemy3=Person("IMP  ",600,65,300,25,enemy_spells,[])
enemies=[enemy1,enemy2,enemy3]


running=True
i=0
print(bcolors.FAIL+bcolors.BOLD+"ENEMY STRIKES"+bcolors.ENDC)

while running:
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:

        player.get_stats()
    print("\n")
    for player in players:
        player.choose_action()
        choice=input("Choose Action: ")
        index=int(choice)-1
        if index==0:
            dmg=player.gen_dmg()
            enemy=player.choose_target(enemies)
            enemies[enemy].take_dmg(dmg)
            print("You attacked "+ enemies[enemy].name+ " for ",dmg," points.    ENEMY HP = ",enemies[enemy].get_hp())
            if enemies[enemy].get_hp()==0:
                print("     "+bcolors.OKBLUE+enemies[enemy].name.upper()+" DIED\n"+bcolors.ENDC)

                del enemies[enemy]
            elif enemies[enemy]==0:
                print("     YOU WIN")
        #magic
        elif index==1:
            player.choose_magic()
            magic_choice=int(input("choose magic: "))-1
            if magic_choice == -1:
                continue

            spell=player.magic[magic_choice]
            m_dmg=spell.gen_magic_dmg()
            current_mp = player.get_mp()
            if spell.cost>current_mp:
                print(bcolors.FAIL+"\nNOT ENOUGH MP\n"+bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            if spell.type == "white":
                player.heal(m_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "\n" + "heals for: ", str(m_dmg), "points" + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(m_dmg)
                print(bcolors.OKBLUE+"\n"+spell.name+"\n"+"deals",str(m_dmg),"points of damage on "+enemies[enemy].name+bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " DIED\n")
                    del enemies[enemy]
        #items
        elif index==2:
            player.choose_item()
            item_choice=int(input("Choose item: "))-1
            if item_choice==-1:
                continue

            items=player.item[item_choice]["item"]


            if player.item[item_choice]["quantity"]==0:
               print(bcolors.FAIL+ "none left"+bcolors.ENDC)
            if items.type=="potion":
                player.heal(items.prop)
            elif items.type=="elixir" :
                if items.name=="mega elixir":
                    for i in players:
                        i.hp=i.maxhp
                        i.mp=i.maxmp
                else:
                    player.heal(items.prop)
                    player.heal_mp(items.prop)
            elif items.type=="attack":
                g_dmg=items.prop
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(g_dmg)
                print("You attacked " + enemies[enemy].name + " for ", g_dmg, " points.    ENEMY HP = ",
                      enemies[enemy].get_hp())
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " DIED\n")
                    del enemies[enemy]
            player.item[item_choice]["quantity"]-=1

    print("-------------------")

    print("-------------------")
    if player.get_hp()==0:
        print(bcolors.FAIL+"YOU LOSE"+bcolors.ENDC)
    defeated_enemies=0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp()==0:
            defeated_enemies+=1
        elif defeated_enemies==2:
            print(bcolors.OKBLUE+"YOU WIN!"+bcolors.ENDC)
            running=False
    for player in players:
        if player.get_hp()==0:
            defeated_players+=1
        elif defeated_players==2:
            print(bcolors.OKBLUE + "YOU LOSE!" + bcolors.ENDC)
            running = False

    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        target = random.randrange(0, len(players))

        if enemy_choice == 0:
            enemy_dmg = enemy.gen_dmg()
            players[target].take_dmg(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for ", enemy_dmg," points")


        # Enemy magic
        elif enemy_choice==1:
            (spell,m_dmg)=enemy.choose_enemy_spell()
            print(enemy.name," Chose "+bcolors.OKBLUE+spell.name.upper()+bcolors.ENDC)
            enemy.reduce_mp(spell.cost)
            if spell.type == "white":
                enemy.heal(m_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "\n" + "heals " +enemy.name+" for: ", str(m_dmg), "points" + bcolors.ENDC)
            elif spell.type == "black":
                players[target].take_dmg(m_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name.upper() + "\n" + "deals", str(m_dmg),
                      "points of damage on " + players[target].name + bcolors.ENDC)
                if players[target].get_hp() == 0:
                    print(players[target].name + " DIED\n")
                    del players[target]


