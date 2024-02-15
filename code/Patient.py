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
        self.referral = referral
