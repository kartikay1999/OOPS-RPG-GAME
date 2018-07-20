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
    def get_stats(self):
         bar_ticks=((self.hp/self.maxhp)*100/5)-1
         hp_bar=""

         while bar_ticks>0:
             hp_bar+="█"
             bar_ticks-=1
         while len(hp_bar)<19:
             hp_bar+="**"
         bar_tick=((self.mp/self.maxmp)*100/10)
         mp_bar=""
         while bar_tick>0:
             mp_bar+="█"
             bar_tick-=1
         while len(mp_bar)<10:
             mp_bar+="**"
         print("                               ______________________________             _______________")
         print(self.name+":   " + bcolors.WARNING ,str(self.hp),"/",str((self.maxhp)),"    |"+hp_bar+"| " + bcolors.OKBLUE
               ,str(self.mp),"/",str(self.maxmp)," |"+mp_bar+"|" + bcolors.ENDC)