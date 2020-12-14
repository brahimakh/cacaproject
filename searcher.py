from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .config import *

class Searcher:

    def __init__(self):
        self.config = SEARCHER_CONFIG
        self.driver = webdriver.Chrome(DRIVER_PATH)
        #1- Quand en prod, activate chrome page hidden
        #2- Lancer
        self.isProductAvailable()

    def isProductAvailable(self):
        pass
        # TODO Faire la recherche pour tous les objets dans config plutot aue simplement sur fnac
        # 1 - boucle sur les pages a inspecter (for PAGE)
        #   2 - pour PAGE; verifier presence ELTS
        #       3 - Si present et ps5IsPresentIfFound TRUE OU Si absent et ps5IsPresentIfFound FALSE
        #           3.1 Une PS5 est dispo !
        #           3.1 Garder la page ouverte; Rendre la window Chrome visibile; Plugger le driver sur une autre window Chrome pour chercher les autres pages
        #           3.1 retirer cette PAGE des configs
        #       3 - else
        #           3.2 La PS5 n'est pqs dispo sur PAGE
        #           3.2 Passer a la page suivante

        #try:
        #    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/section/ul[2]/li/div/div[1]/div[1]/div[1]/div/p")))
        #    print("Page is ready!")
        #except TimeoutException:
        #    print("Loading took too much time!")
        #    print("Coucou brahim... jaime le caca")
