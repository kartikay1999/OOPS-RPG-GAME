from game import Person,bcolors
from magic import spell
from inventory import items



# magic
fire=spell('fire',10,100,'black')
thunder=spell('thunder',15,150,'black')
quake=spell('quake',12,125,'black')
cure=spell('cure',15,140,'white')
cura=spell('cura',20,200,'white')
# items
potion=items("potion","potion","Heals 50 hp",50)
hipotion=items("Hi-Potion","potion","Heals 100 hp",100)
super_potion=items("Super-Potion","potion","Heals 500 hp",500)
elixir=items("elxir","elixir","fully restores HP/MP of one party member",99999)
mega_elixir=items("mega elixir","elixir","fully restores HP/MP of party ",99999)

grenade=items("Grenade","attack","Deals 500 damage ",500)
player_spells=[fire,thunder,quake,cure,cura]
player_items=[{"item":potion,"quantity":5},{"item":hipotion,"quantity":5},
             {"item":super_potion,"quantity":1},{"item":elixir,"quantity":2},
             {"item":mega_elixir,"quantity":1},{"item":grenade,"quantity":2}]
# players
player =Person("VALOS:   ",4160,65,150,34,player_spells,player_items)
player1=Person("player1: ",3460,65,80,34,player_spells,player_items)
player2=Person("player2: ",3060,65,100,34,player_spells,player_items)
enemy=Person("enemy1",6000,65,200,25,[],[])
players=[player,player1,player2]
running=True
i=0
print(bcolors.FAIL+bcolors.BOLD+"ENEMY STRIKES"+bcolors.ENDC)

while running:
    for player in players:
        player.get_stats()
    print("\n")
    for player in players:
        player.choose_action()
        choice=input("Choose Action: ")
        index=int(choice)-1
        if index==0:
            dmg=player.gen_dmg()
            enemy.take_dmg(dmg)
            print("You attacked for",dmg,"points.    ENEMY HP = ",enemy.get_hp())
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
                enemy.take_dmg(m_dmg)
                print(bcolors.OKBLUE+"\n"+spell.name+"\n"+"deals",str(m_dmg),"points of damage"+bcolors.ENDC)

        #items
        elif index==2:
            player.choose_item()
            item_choice=int(input("Choose item: "))-1
            if item_choice==-1:
                continue

            items=player.item[item_choice]["item"]

            player.item[item_choice]["quantity"]-=1
            if player.item[item_choice]["quantity"]==0:
               print(bcolors.FAIL+ "none left"+bcolors.ENDC)
            if items.type=="potion":
                player.heal(items.prop)
            elif items.type=="elixir" :
                player.heal(items.prop)
                player.heal_mp(items.prop)
            elif items.type=="attack":
                g_dmg=items.prop
                enemy.take_dmg(g_dmg)

    enemy_choice=1
    enemy_dmg=enemy.gen_dmg()
    player.take_dmg(enemy_dmg)
    print("enemy attacks for: ",enemy_dmg)

    print("-------------------")

    print("your hp:     "+bcolors.WARNING+str(player.get_hp())+"/"+str(player.get_max_hp())+bcolors.ENDC)
    print("your mp:     " + bcolors.FAIL + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
    print("enemy hp:     " + bcolors.HEADER + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("-------------------")
    if player.get_hp()==0:
        print(bcolors.FAIL+"YOU LOSE"+bcolors.ENDC)
        break
    elif enemy.get_hp()==0:
        print(bcolors.FAIL + "YOU WIN" + bcolors.ENDC)
        break