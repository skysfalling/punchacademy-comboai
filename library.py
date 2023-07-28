class Punch:
    def __init__(self, number, name, weight, sector_req):
        self.number = number
        self.name = name
        self.weight = weight  # used for calculating damage and stamina reduction
        self.sector_req = sector_req

    def __repr__(self) -> str:
        sect_req_str = "".join(self.sector_req)
        return f"#{self.number}-{self.name} :: (dmg={self.weight}, req='{sect_req_str}')"


class PunchLibrary:
    def __init__(self):
        self.jab = Punch(1, "Jab", 1, ["B", "D", "E", "F"])
        self.cross = Punch(2, "Cross", 2, ["B", "D", "E", "F"])
        self.left_hook = Punch(3, "Left Hook", 4, ["A", "D"])
        self.right_hook = Punch(4, "Right Hook", 4, ["C", "F"])
        self.left_uppercut = Punch(5, "Left Uppercut", 3, ["B"])
        self.right_uppercut = Punch(6, "Right Uppercut", 3, ["B"])

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
                if sector.name in punch.sector_req and punch not in punchOptions:
                    punchOptions.append(punch)
        return punchOptions


punchLibrary = PunchLibrary()

# ========================================= /// >>

defense_stances = {
    "centerface": "B",
    "looseface": "AC",
    "leftside": "ADE",
    "rightside": "CEF",
    "body": "DEF"
}


class Combo:
    def __init__(self, combo_str):
        self.combo_str = combo_str
        self.punches = []
        self.stamina_cost = 0

        # get punches from combo string
        for char in combo_str:
            self.punches.append(punchLibrary.GetPunch(int(char)))

        # get stamina cost from punches
        for punch in self.punches:
            self.stamina_cost += punch.weight

    def __repr__(self) -> str:
        out_string = f"Combo [{self.combo_str}] - Stamina Cost({self.stamina_cost})"
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
        self.sectorA = Sector("A", 2)
        self.sectorB = Sector("B", 3)
        self.sectorC = Sector("C", 2)
        self.sectorD = Sector("D", 1)
        self.sectorE = Sector("E", 1)
        self.sectorF = Sector("F", 1)
        self.sectors = [self.sectorA, self.sectorB, self.sectorC,
                        self.sectorD, self.sectorE, self.sectorF]

        self.sectors_str = sectors_str.upper()

    def GetSector(self, name):
        name = name.upper()
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
        self.sectors_str = sectors_str.upper()
        for sector in self.sectors:
            # if sector.name in sectors_str, set as blocked
            if sector.name in sectors_str:
                sector.blocked = True

    def Visualize(self):
        out_string = "\t"
        for i in range(6):
            if (i == 3):
                out_string += "\n\t"  # lowerbody newline
            out_string += "| "
            if (self.sectors[i].blocked):
                out_string += "X"
            else:
                out_string += "."
            out_string += " |"

        print(out_string)

# ======================================== /// >>
