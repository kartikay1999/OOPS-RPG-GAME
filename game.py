import random
from magic import spell

class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    WARNING='\033[92m'
    FAIL='\033[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'

class Person:
    def __init__(self,name,hp,mp,atk,df,magic,item):
        self.name=name
        self.maxhp=hp
        self.item=item
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.actions=["Attack", "Magic","Items"]

    def gen_dmg(self):
        return random.randrange(self.atkl,self.atkh)

    def take_dmg(self,dmg):
        self.hp-=dmg
        if self.hp < 0:
         self.hp=0
         return self.hp
    def heal(self,dmg):
        self.hp+=dmg
        if self.hp>self.maxhp:
            self.hp=self.maxhp
    def heal_mp(self,dmg):
        self.mp+=dmg
        if self.mp>self.maxmp:
            self.mp=self.maxmp

    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp
    def reduce_mp(self,cost):
        self.mp-=cost

    def choose_action(self):
        i=1
        print(bcolors.OKBLUE+"\n",self.name,"\n"+bcolors.ENDC)
        print("actions")
        for item in self.actions:
            print(str(i)+":",item)
            i+=1
    def choose_magic(self):
        i=1
        print(self.magic)

        print(bcolors. OKBLUE+bcolors.BOLD+"magic"+bcolors.ENDC)
        for spell in self.magic:
            print(str(i)+":",spell.name, "(cost",str(spell.cost)+")")
            i+=1
    def choose_item(self):
        i=1
        print(self.item)
        print(bcolors.OKBLUE+bcolors.BOLD+"items"+bcolors.ENDC)
        for item in self.item:
            print(str(i)+". ",item["item"].name,":",item["item"].description,"(x"+str(item["quantity"])+")")
            i+=1
    def choose_target(self,enemies):
        i=1
        print("\n"+bcolors.OKBLUE+bcolors.BOLD+"TARGET :"+bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp()!=0:
                print(str(i)+". ",enemy.name)
                i+=1
        choice=int(input("Choose Target: "))-1
        return choice

    def get_enemy_stats(self):
        hp_bar=""
        bar_ticks=(self.hp/self.maxhp)*100/4
        while bar_ticks>0:
            hp_bar+= "█"
            bar_ticks -= 1
        while len(hp_bar)<50:
            hp_bar+="  "
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            current_hp += hp_string
            while decreased >= 0:
                current_hp += " "

                decreased -= 1
        else:
            current_hp = hp_string

        print("                     _______________________________________")
        print(self.name+":  " + bcolors.FAIL + current_hp + "  |" + hp_bar + "|" + bcolors.ENDC+"\n\n")

    def get_stats(self):
         bar_ticks=((self.hp/self.maxhp)*100/5)-1
         hp_bar=""
         while bar_ticks>0:
             hp_bar+="█"
             bar_ticks-=1
         while len(hp_bar)<19:
             hp_bar+="  "
         bar_tick=((self.mp/self.maxmp)*100/10)
         mp_bar=""
         while bar_tick>0:
             mp_bar+="█"
             bar_tick-=1
         while len(mp_bar)<10:
             mp_bar+="   "
         hp_string=str(self.hp)+"/"+str(self.maxhp)
         current_hp=""
         if len(hp_string)<9:
             decreased=9-len(hp_string)
             current_hp += hp_string
             while decreased>=0:
                 current_hp+=" "

                 decreased -= 1
         else :
             current_hp=hp_string

         mp_string = str(self.mp) + "/" + str(self.maxmp)
         current_mp = ""
         if len(mp_string) < 7:
            decrease = 7 - len(mp_string)
            current_mp += mp_string
            while decrease >= 0:
                current_mp += " "

                decrease -= 1
            else:
                current_mp = mp_string
         print("                      ______________________________")
         print(self.name+":"+ bcolors.WARNING +current_hp+"  |"+hp_bar+"|"+bcolors.ENDC)
         print(self.name+":"+bcolors.FAIL+current_mp+"      |"+mp_bar+"|"+bcolors.ENDC)
    def choose_enemy_spell(self):

        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        m_dmg = spell.gen_magic_dmg()
        pct=(self.hp/self.maxhp)*100
        if self.mp < spell.cost or spell.type=="white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return (spell, m_dmg)