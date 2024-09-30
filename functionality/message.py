from .driver import Driver
from .doctor_info import DoctorInfo


class Message:

    def __init__(self, driver: Driver, message_body: dict):
        self.message_header = '—' * 11 + " Available slots " + '—' * 11 + '\n\n'
        self.message_body = ""
        self.create_message_body(message_body)
        self.doctor = DoctorInfo(driver)

    def create_message_body(self, slots: dict):
        for slot_date, slots_time in slots.items():
            if slots_time:
                self.message_body += f"<b>| {slot_date} |</b> {', '.join(slots_time)}\n\n"

        # if not self.message_body:
        #     self.message_body = "**| No available slots |**"

    def __str__(self):
        return (f"<b>{self.message_header}"
                f"{self.doctor.doctor_speciality}\n{self.doctor.doctor_name}</b>"
                f"\n\n{self.message_body}") \
            if self.message_body else ""
