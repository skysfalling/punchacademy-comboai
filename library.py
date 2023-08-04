class Punch:
    def __init__(self, number, name, damage, stamina, target_sectors):
        self.number = number
        self.name = name
        self.target_sectors = target_sectors
        self.target_sectors_str = "".join(target_sectors)

        self.damage = damage
        self.stamina = stamina

    def __repr__(self) -> str:
        target_sectors = "".join(self.target_sectors)
        return f"{self.number} - {self.name} :: (dmg={self.damage} stm={self.stamina} tgt={self.target_sectors_str})"


class PunchLibrary:
    def __init__(self):
        self.jab = Punch(1, "Jab", 1, 1, ["b", "d", "e", "f"])
        self.cross = Punch(2, "Cross", 2, 2, ["b", "d", "e", "f"])
        self.left_hook = Punch(3, "Left Hook", 3, 3, ["a", "d"])
        self.right_hook = Punch(4, "Right Hook", 3, 3, ["c", "f"])
        self.left_uppercut = Punch(5, "Left Uppercut", 5, 5, ["b"])
        self.right_uppercut = Punch(6, "Right Uppercut", 5, 5, ["b"])

        self.punches = [
            self.jab,
            self.cross,
            self.left_hook,
            self.right_hook,
            self.left_uppercut,
            self.right_uppercut
        ]

    def GetPunch(self, index):
        for punch in self.punches:
            if index == punch.number:
                return punch

    def GetPunchOptions(self, sectorGroup):
        punchOptions = []
        for sector in sectorGroup.GetFreeSectors():
            for punch in self.punches:
                # if sector is in punch requirements, add to available punches
                if sector.name in punch.target_sectors and punch not in punchOptions:
                    punchOptions.append(punch)
        sortedPunchOptions = sorted(
            punchOptions, key=lambda item: item.number)
        return sortedPunchOptions


punchLibrary = PunchLibrary()

# ========================================= /// >>

defense_stances = {
    "centerface": "b",
    "looseface": "ac",
    "leftside": "ade",
    "rightside": "cef",
    "body": "def"
}


class Combo:
    def __init__(self, combo_str):
        self.combo_str = combo_str
        self.punches = []
        self.damage_output = 0
        self.stamina_cost = 0

        # get punches from combo string
        for char in combo_str:
            self.punches.append(punchLibrary.GetPunch(int(char)))

        # get stamina cost from punches
        for punch in self.punches:
            self.stamina_cost += punch.stamina
            self.damage_output += punch.damage

    def __repr__(self) -> str:
        out_string = f"Combo [{self.combo_str}] - (stm: {self.stamina_cost} , dmg: {self.damage_output})"
        for punch in self.punches:
            out_string += "\n\t" + str(punch)
        return out_string


class ComboLibrary:
    def __init__(self):
        self.combos = [
            Combo("12"),
            Combo("11"),
            Combo("23"),
            Combo("32"),
            Combo("34")
        ]


comboLibrary = ComboLibrary()


# ========================================= /// >>

class Sector:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.blocked = False


class SectorGroup:
    def __init__(self, sectors_str=""):
        self.sectorA = Sector("a", 2)
        self.sectorB = Sector("b", 3)
        self.sectorC = Sector("c", 2)
        self.sectorD = Sector("d", 1)
        self.sectorE = Sector("e", 1)
        self.sectorF = Sector("f", 1)
        self.sectors = [self.sectorA, self.sectorB, self.sectorC,
                        self.sectorD, self.sectorE, self.sectorF]

        self.sectors_str = sectors_str.lower()

    def GetSector(self, name):
        name = name.lower()
        for sector in self.sectors:
            if (name == sector.name):
                return sector

    def SetSector(self, name, blocked):
        sector = self.GetSector(name)
        sector.blocked = blocked

    def GetFreeSectors(self):
        free_sectors = []
        for sector in self.sectors:
            if sector.blocked == False:
                free_sectors.append(sector)
        return free_sectors

    def ResetSectors(self):
        print("Reset Sectors")
        for sector in self.sectors:
            sector.blocked = False

    def SetSectorGroup(self, sectors_str):
        self.sectors_str = sectors_str.lower()
        for sector in self.sectors:
            # if sector.name in sectors_str, set as blocked
            if sector.name in sectors_str:
                sector.blocked = True

    def Visualize(self):
        out_string = ""
        count = 0
        for sector in self.sectors:
            mark = "X"
            count += 1
            if sector.blocked == False:
                mark = sector.name
            out_string += f"| {mark} |"
            if count == 3:
                out_string += "\n"

        print(out_string)

# ======================================== /// >>
