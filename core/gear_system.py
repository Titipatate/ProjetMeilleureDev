class GearSystem():
    def __init__(self, gearData, motorRpm, gearSequence):
        self.gearData = gearData
        self.motorRpm = motorRpm
        self.gearSequence = gearSequence
    
    def addGearStep(self, driverKey, followerKey):
        
        if driverKey not in self.gearData:
            print(f"[Erreur] Driver gear '{driverKey}' introuvable.")
            return

        if followerKey not in self.gearData:
            print(f"[Erreur] Follower gear '{followerKey}' introuvable.")
            return

        self.gearSequence.append((driverKey, followerKey))

    def calculate(self):
        """
        Calcule les RPM à chaque étape de la séquence, à partir du RPM moteur.
        Remplit self.intermediate_rpms.
        """
        self.intermediateRpms = [self.motorRpm]  # RPM initial

        currentRpm = self.motorRpm

        for step in self.gearSequence:
            driverKey, followerKey = step

            # Vérification des clés (par sécurité)
            if driverKey not in self.gearData or followerKey not in self.gearData:
                print(f"[Erreur] Étape invalide : {step}")
                self.intermediateRpms.append(None)  # ou ignorer ?
                continue

            try:
                teethDriver = int(self.gearData[driverKey]["Teeth"])
                teethFollower = int(self.gearData[followerKey]["Teeth"])

                ratio = teethFollower / teethDriver
                currentRpm *= ratio
                self.intermediateRpms.append(currentRpm)

            except (ValueError, ZeroDivisionError) as e:
                print(f"[Erreur] Calcul impossible pour l'étape {step} : {e}")
                self.intermediateRpms.append(None)



    def getResults(self) -> list:
        """
        Retourne la liste des vitesses calculées (RPM) à chaque étape.

        Returns:
            list[float]: vitesses intermédiaires successives.
        """
        pass
