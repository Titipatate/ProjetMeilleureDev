from data.dataGear import gearDico, motorDefaultsRPM
from core.gear_system import GearSystem

gearSystem = GearSystem(gearData=gearDico, motorRpm=400, gearSequence=[])
gearSystem.addGearStep("Gear2", "Gear6")
gearSystem.addGearStep("Gear2", "Gear6")
gearSystem.calculate()
print(gearSystem.intermediateRpms)
