from constants import VehicleTypes

class Inventory:
    'Class to denote vehicle on company duty'
    vehicle_available_for_duty = {
        VehicleTypes.ALS : 0,
        VehicleTypes.HMV_4X4 : 0,
        VehicleTypes.ARMY_BUS : 0,
        VehicleTypes.WATER_BOWSER_5KL : 0,
        VehicleTypes.WATER_BOWSER_2KL : 0
    }

    def __init__(self,
                 vehicle_type,
                 auth,
                 held,
                 cl_v_vi,
                 under_cl_v,
                 in_workshop,
                 lrw,
                 bty,
                 tyre_tube,
                 mod_veh,
                 cvy,
                 out_station,
                 in_station,
                 local_duty):
        self.vehicle_type = vehicle_type
        self.auth = auth
        self.held = held
        self.cl_v_vi = cl_v_vi
        self.under_cl_v = under_cl_v
        self.in_workshop = in_workshop
        self.lrw =lrw
        self.bty = bty
        self.tyre_tube = tyre_tube
        self.total_off_road = self.in_workshop + self.lrw + self.bty + self.tyre_tube
        self.mod_veh = mod_veh
        self.cvy = cvy
        self.out_station = out_station
        self.in_station =  in_station
        self.local_duty = local_duty
        self.total_available_for_duty = self.held - (self.cl_v_vi + self.under_cl_v + self.total_off_road + self.mod_veh + self.cvy + self.out_station + self.in_station + self.local_duty)

        if self.vehicle_type == VehicleTypes.ALS:
            Inventory.vehicle_available_for_duty[VehicleTypes.ALS] = self.total_available_for_duty
        elif self.vehicle_type == VehicleTypes.HMV_4X4:
            Inventory.vehicle_available_for_duty[VehicleTypes.HMV_4X4] = self.total_available_for_duty
        elif self.vehicle_type == VehicleTypes.ARMY_BUS:
            Inventory.vehicle_available_for_duty[VehicleTypes.ARMY_BUS] = self.total_available_for_duty
        elif self.vehicle_type == VehicleTypes.WATER_BOWSER_5KL:
            Inventory.vehicle_available_for_duty[VehicleTypes.WATER_BOWSER_5KL] = self.total_available_for_duty
        elif self.vehicle_type == VehicleTypes.WATER_BOWSER_2KL:
            Inventory.vehicle_available_for_duty[VehicleTypes.WATER_BOWSER_2KL] = self.total_available_for_duty