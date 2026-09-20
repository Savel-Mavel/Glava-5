from address import Address
from mailing import Mailing

from_addr = Address("662606", "Минусинск", "Спартака", "15", "5")
to_addr = Address("662354", "Абакан", "Кирова", "15", "10")


mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="TRACK2799757"
)


print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)