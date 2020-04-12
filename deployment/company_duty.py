from constants import VehicleTypes

class CompanyDuty:
    'Class to denote vehicle on company duty'

    total_count = 0
    vehicle_counts = {
        VehicleTypes.ALS : 0,
        VehicleTypes.HMV_4X4 : 0,
        VehicleTypes.ARMY_BUS : 0,
        VehicleTypes.WATER_BOWSER_5KL : 0,
        VehicleTypes.WATER_BOWSER_2KL : 0
    }

    def __init__(self,
        unit,
        duty,
        vehicle_type,
        company):
        self.unit =  unit
        self.duty = duty
        self.vehicle_type = vehicle_type
        self.company = company

        CompanyDuty.total_count += 1

        if self.vehicle_type == VehicleTypes.ALS:
            CompanyDuty.vehicle_counts[VehicleTypes.ALS] +=1
        elif self.vehicle_type == VehicleTypes.HMV_4X4:
            CompanyDuty.vehicle_counts[VehicleTypes.HMV_4X4] +=1
        elif self.vehicle_type == VehicleTypes.ARMY_BUS:
            CompanyDuty.vehicle_counts[VehicleTypes.ARMY_BUS] +=1
        elif self.vehicle_type == VehicleTypes.WATER_BOWSER_5KL:
            CompanyDuty.vehicle_counts[VehicleTypes.WATER_BOWSER_5KL] +=1
        elif self.vehicle_type == VehicleTypes.WATER_BOWSER_2KL:
            CompanyDuty.vehicle_counts[VehicleTypes.WATER_BOWSER_2KL] +=1