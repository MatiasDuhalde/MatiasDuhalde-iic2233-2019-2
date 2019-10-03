class ErrorPatente(Exception):
    def __init__(self, conductor, patente_oficial):
        '''
        Error si la patente no es la asociada al conductor.
        '''
        self.conductor = conductor
        self.patente_oficial = patente_oficial
        super().__init__((f"La patente {self.conductor.patente} no coincide con " + 
        f"la del registro oficial ({self.patente_oficial})."))

