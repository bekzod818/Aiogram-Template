import asyncio
from utils.db_api.db_commands import Database


async def test():
    db = Database()
    await db.create()

    print("Users jadvalini yaratamiz...")
    await db.drop_users()
    await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("anvar", "sariqdev", 123456789)
    await db.add_user("olim", "olim223", 12341123)
    await db.add_user("1", "1", 131231)
    await db.add_user("1", "1", 23324234)
    await db.add_user("John", "JohnDoe", 4388229)
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

    #### Kurslar uchun test
    print("Kurslar jadvalini yaratamiz...")
    await db.drop_courses()
    await db.create_table_courses()
    await db.add_course(
        "web",
        "🌐 Web-dasturlash",
        "front",
        "🌌 Front-End",
        "Zohidjon Ozadov",
        "https://instagram.ftas1-1.fna.fbcdn.net/v/t51.2885-15/e35/240750257_4236125056476118_3539579123322634428_n.jpg?_nc_ht=instagram.ftas1-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=8FitzN0XMqIAX_SC3ZP&tn=HfgVmPDIwcyulT9n&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT8sw5w3vy7iBT--aHbSpK_csGQu3sbUhAPfIeiccjOw1Q&oe=61C9C755&_nc_sid=83d603",
        650000,
        "👨🏻‍💻 Frontend web dasturlash kursi o'qituvchisi. Faoliyati davomida appx.uz firmasida frontend web dasturchi sifatida ishlaydi. Hozirda TATU talabasi"
    )
    await db.add_course(
        "web",
        "🌐 Web-dasturlash",
        "back",
        "🛠 Back-End",
        "Bekzod Raximov",
        "https://instagram.ftas1-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/269490173_1618641998478824_7474161390699081638_n.jpg?_nc_ht=instagram.ftas1-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=RKHnZRUbDr4AX_zwCox&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT9xUpKWrXwcVnBzXGhHQU_lIZy-LvCWhu8bozEfukNW3Q&oe=61C88150&_nc_sid=83d603",
        650000,
        "💻 Sohada 2 yillik tajribaga ega. Oliy ma'lumotli . DELTA IT kompaniyasida python dasturchisi bo'lib ishlaydi. Faoliyati davomida bir qancha online do'konlar, telegram botlar, yangilik saytlari ishlab chiqqan."
    )
    await db.add_course(
        "mobile",
        "📲 Mobil dasturlash",
        "android",
        "Android dasturlash",
        "Jalol Imomaddinov",
        "https://instagram.ftas2-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/267522272_1597314520610669_1161646802673094287_n.jpg?_nc_ht=instagram.ftas2-2.fna.fbcdn.net&_nc_cat=105&_nc_ohc=nLNagLtMQPUAX9wTa00&tn=HfgVmPDIwcyulT9n&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT8238BFguu3ajGAoIHcbo0epI77HOlfVWa9xxJqx4ITrQ&oe=61C92AE0&_nc_sid=83d603",
        750000,
        "👨‍💻 Профессиональный программист с 4-х летним опытом в данной сфере. Работал фрилансером с разными странами как Украина, Беларусь и Россия.",
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
