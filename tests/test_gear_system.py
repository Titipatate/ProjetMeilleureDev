import unittest
from core.gear_system import GearSystem
from data.dataGear import gearDico

class testGearSystem(unittest.TestCase):

    #test qu'une étape valide est bien ajouté dans addGearStep
    def test_addGearStep_with_one_step(self):
        gearSystem = GearSystem(gearData=gearDico, motorRpm=400, gearSequence=[])
        gearSystem.addGearStep("Gear2", "Gear9")
        sizeGearSequence = len(gearSystem.gearSequence)
        self.assertEqual(1, sizeGearSequence)
        self.assertIn(("Gear2", "Gear9"), gearSystem.gearSequence, msg="L'étape ('Gear2', 'Gear9') n'a pas été trouvée dans gearSequence")

    #Tester que les RPM sont bien calculé avec une séquence simple dans calculate
    def test_calculate_with_two_step_valide(self):
        gearSystem = GearSystem(gearData=gearDico, motorRpm=400, gearSequence=[])
        gearSystem.addGearStep("Gear2", "Gear9")
        gearSystem.addGearStep("Gear2", "Gear9")
        gearSystem.calculate()

        self.assertEqual(3, len(gearSystem.intermediateRpms))
        self.assertListEqual([400, 2000.0, 10000.0], gearSystem.intermediateRpms, msg="Error comparaison list")
        self.assertAlmostEqual(2000.0, gearSystem.intermediateRpms[(1)], 7, msg="Error mauvais index")

    #Tester le comportement quand une clé d'engrenage n'est pas valide
    def test_calculate_with_no_existent_key(self):
        gearDicoNotValide = {
            "Gear2" : {"id": "Gear2", "name": "Gear-2", "Teeth": "8", "icon": "None", "ID Design": ""},
            "Gear3" : {"id": "Gear3", "name": "Gear-3", "Teeth": "???", "icon": "None", "ID Design": ""},
        }

        gearSystem = GearSystem(gearData=gearDicoNotValide, motorRpm=400, gearSequence=[])
        gearSystem.addGearStep("Gear2", "Gear3")
        gearSystem.calculate()
