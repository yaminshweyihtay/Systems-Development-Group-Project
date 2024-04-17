class Patient:
    def __init__(self, encounter_id, end_tidal_co2=None, feed_vol=None, feed_vol_adm=None, fio2=None, fio2_ratio=None,
                 insp_time=None,
                 oxygen_flow_rate=None, peep=None, pip=None, resp_rate=None, sip=None, tidal_vol=None,
                 tidal_vol_actual=None, tidal_vol_kg=None, tidal_vol_spon=None,
                 bmi=None, referral=0):
        self.__encounter_id = encounter_id
        self.__end_tidal_co2 = end_tidal_co2
        self.__feed_volume = feed_vol
        self.__feed_volume_adm = feed_vol_adm
        self.__fio2 = fio2
        self.__fio2_ratio = fio2_ratio
        self.__insp_time = insp_time
        self.__oxygen_flow_rate = oxygen_flow_rate
        self.__peep = peep
        self.__pip = pip
        self.__resp_rate = resp_rate
        self.__sip = sip
        self.__tidal_volume = tidal_vol
        self.__tidal_volume_actual = tidal_vol_actual
        self.__tidal_volume_kg = tidal_vol_kg
        self.__tidal_volume_spon = tidal_vol_spon
        self.__bmi = bmi
        self.__referral = referral

    # Setters
    def set_encounter_id(self, encounter_id):
        self.__encounter_id = encounter_id

    def set_end_tidal_co2(self, end_tidal_co2):
        self.__end_tidal_co2 = end_tidal_co2

    def set_feed_volume(self, feed_vol):
        self.__feed_volume = feed_vol

    def set_feed_volume_adm(self, feed_vol_adm):
        self.__feed_volume_adm = feed_vol_adm

    def set_fio2(self, fio2):
        self.__fio2 = fio2

    def set_fio2_ratio(self, fio2_ratio):
        self.__fio2_ratio = fio2_ratio

    def set_insp_time(self, insp_time):
        self.__insp_time = insp_time

    def set_oxygen_flow_rate(self, oxygen_flow_rate):
        self.__oxygen_flow_rate = oxygen_flow_rate

    def set_peep(self, peep):
        self.__peep = peep

    def set_pip(self, pip):
        self.__pip = pip

    def set_resp_rate(self, resp_rate):
        self.__resp_rate = resp_rate

    def set_sip(self, sip):
        self.__sip = sip

    def set_tidal_volume(self, tidal_vol):
        self.__tidal_volume = tidal_vol

    def set_tidal_volume_actual(self, tidal_vol_actual):
        self.__tidal_volume_actual = tidal_vol_actual

    def set_tidal_volume_kg(self, tidal_vol_kg):
        self.__tidal_volume_kg = tidal_vol_kg

    def set_tidal_volume_spon(self, tidal_vol_spon):
        self.__tidal_volume_spon = tidal_vol_spon

    def set_bmi(self, bmi):
        self.__bmi = bmi

    def set_referral(self, referral):
        self.__referral = referral

    # Getters
    def get_encounter_id(self):
        return self.__encounter_id

    def get_end_tidal_co2(self):
        return self.__end_tidal_co2

    def get_feed_volume(self):
        return self.__feed_volume

    def get_feed_volume_adm(self):
        return self.__feed_volume_adm

    def get_fio2(self):
        return self.__fio2

    def get_fio2_ratio(self):
        return self.__fio2_ratio

    def get_insp_time(self):
        return self.__insp_time

    def get_oxygen_flow_rate(self):
        return self.__oxygen_flow_rate

    def get_peep(self):
        return self.__peep

    def get_pip(self):
        return self.__pip

    def get_resp_rate(self):
        return self.__resp_rate

    def get_sip(self):
        return self.__sip

    def get_tidal_volume(self):
        return self.__tidal_volume

    def get_tidal_volume_actual(self):
        return self.__tidal_volume_actual

    def get_tidal_volume_kg(self):
        return self.__tidal_volume_kg

    def get_tidal_volume_spon(self):
        return self.__tidal_volume_spon

    def get_bmi(self):
        return self.__bmi

    def get_referral(self):
        return self.__referral
