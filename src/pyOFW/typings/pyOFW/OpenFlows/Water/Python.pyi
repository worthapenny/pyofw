from OpenFlows.Water.Domain import IWaterModel

class OpenFlowsWaterPython:
    
    @staticmethod
    def StartWaterGEMSSession() -> None:
        pass

    @staticmethod
    def StartWaterCADSession() -> None:
        pass

    @staticmethod
    def StartWaterOPSSession() -> None:
        pass

    @staticmethod
    def OpenModel(filename: str) -> IWaterModel:
        pass

    @staticmethod
    def EndSession() -> None:
        pass