import asyncio
from utils.db_api.db_commands import Database


async def test():
    db = Database()
    await db.create()

    # print("Users jadvalini yaratamiz...")
    # await db.drop_users()
    # await db.create_table_users()
    # print("Yaratildi")
    #
    # print("Foydalanuvchilarni qo'shamiz")
    #
    # await db.add_user("anvar", "sariqdev", 123456789)
    # await db.add_user("olim", "olim223", 12341123)
    # await db.add_user("1", "1", 131231)
    # await db.add_user("1", "1", 23324234)
    # await db.add_user("John", "JohnDoe", 4388229)
    # print("Qo'shildi")
    #
    # users = await db.select_all_users()
    # print(f"Barcha foydalanuvchilar: {users}")
    #
    # user = await db.select_user(id=5)
    # print(f"Foydalanuvchi: {user}")

    #### Kurslar uchun test
    print("Kurslar jadvalini yaratamiz...")
    await db.drop_courses()
    await db.create_table_courses()
    await db.add_course(
        "dev",
        "👨🏻‍💻 Dasturlash",
        "web",
        "🌐 Web-dasturlash",
        "Front-End",
        "https://instagram.ftas1-1.fna.fbcdn.net/v/t51.2885-15/e35/240750257_4236125056476118_3539579123322634428_n.jpg?_nc_ht=instagram.ftas1-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=8FitzN0XMqIAX_SC3ZP&tn=HfgVmPDIwcyulT9n&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT8sw5w3vy7iBT--aHbSpK_csGQu3sbUhAPfIeiccjOw1Q&oe=61C9C755&_nc_sid=83d603",
        650_000,
        "👨🏻‍💻 Frontend web dasturlash kursi o'qituvchisi. Faoliyati davomida appx.uz firmasida frontend web dasturchi sifatida ishlaydi. Hozirda TATU talabasi"
    )
    await db.add_course(
        "dev",
        "👨🏻‍💻 Dasturlash",
        "web",
        "🌐 Web-dasturlash",
        "Python dasturlash tili",
        "https://instagram.ftas1-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/269490173_1618641998478824_7474161390699081638_n.jpg?_nc_ht=instagram.ftas1-1.fna.fbcdn.net&_nc_cat=108&_nc_ohc=RKHnZRUbDr4AX_zwCox&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT9xUpKWrXwcVnBzXGhHQU_lIZy-LvCWhu8bozEfukNW3Q&oe=61C88150&_nc_sid=83d603",
        650_000,
        "💻 Sohada 2 yillik tajribaga ega. Oliy ma'lumotli . DELTA IT kompaniyasida python dasturchisi bo'lib ishlaydi. Faoliyati davomida bir qancha online do'konlar, telegram botlar, yangilik saytlari ishlab chiqqan."
    )
    await db.add_course(
        "dev",
        "👨🏻‍💻 Dasturlash",
        "web",
        "🌐 Web-dasturlash",
        "PHP dasturlash tili",
        "https://bit.ly/3EjNbru",
        650_000,
        "🧑‍💻 'PHP'ga asoslangan web dasturlash kursi mentori Zafarbek Sobirov\n\n💻 Sohada 10 yillik tajribaga ega. Hozirda 'Breeze Soft' hamda 'Innova Holding xususiy korxonalarining rahbari hisoblanadi. Shu paytgacha Respublika bo\'yicha 800 dan ortiq davlat tashkilotlari va xususiy korxonalarning web sayt, web ilovalarini va online servislarni yaratgan. Serverlarni sozlash, nazorat qilish bo'yicha malakaga ega.\n\n🖥 Texnologik malakasi - HTML, CSS, JS, Bootstrap, PHP, MYSQL, Framework (Yii2, Laravel). Wordpress, Opencart, DLE CMSlariga plugin va dizaynlar yaratish.")
    await db.add_course(
        "dev",
        "👨🏻‍💻 Dasturlash",
        "mobile",
        "📲 Mobil dasturlash",
        "Java dasturlash tili",
        "https://instagram.ftas2-2.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/267522272_1597314520610669_1161646802673094287_n.jpg?_nc_ht=instagram.ftas2-2.fna.fbcdn.net&_nc_cat=105&_nc_ohc=nLNagLtMQPUAX9wTa00&tn=HfgVmPDIwcyulT9n&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT8238BFguu3ajGAoIHcbo0epI77HOlfVWa9xxJqx4ITrQ&oe=61C92AE0&_nc_sid=83d603",
        750_000,
        "👨‍💻 Профессиональный программист с 4-х летним опытом в данной сфере. Работал фрилансером с разными странами как Украина, Беларусь и Россия.",
    )

    await db.add_course(
        "komputer",
        "💻 Kompyuter savodxonligi",
        "beginner",
        "Boshlang'ich kurslar",
        "Foundation",
        "https://bit.ly/3mv3FXU",
        550_000,
        '👨🏻‍💻"Ofis dasturlarida ishlash" kursi mentori Sardor Kuziyev\n\n💻 Sohada 7 yillik tajribaga ega. "UzMU" va "Xalq ta\'limi boshqarmasi" bo\'limida ta\'lim sifati monitoringi va attestatsiya bo\'limida bo\'lim boshlig\'i bo\'lib faoliyat yuritgan.\n\n🖥 Texnologik malakasi: Word, Excel, Power Point, Elektron hujjatlar bazasini yaratish, QR kodlash, dasturlash.\n\n📌Sardor Kuziyevning 2 oylik "Ofis dasturlarida ishlash" kursida kompyuter savodxonligi va Word, Excel va Power Point dasturlarida ishlash o\'rgatiladi.')

    await db.add_course(
        "komputer",
        "💻 Kompyuter savodxonligi",
        "oficce",
        "Ofis dasturlarida ishlash",
        "Word, Excel, PowerPoint",
        "https://bit.ly/3mv3FXU",
        550_000,
        '👨🏻‍💻"Ofis dasturlarida ishlash" kursi mentori Sardor Kuziyev\n\n💻 Sohada 7 yillik tajribaga ega. "UzMU" va "Xalq ta\'limi boshqarmasi" bo\'limida ta\'lim sifati monitoringi va attestatsiya bo\'limida bo\'lim boshlig\'i bo\'lib faoliyat yuritgan.\n\n🖥 Texnologik malakasi: Word, Excel, Power Point, Elektron hujjatlar bazasini yaratish, QR kodlash, dasturlash.\n\n📌Sardor Kuziyevning 2 oylik "Ofis dasturlarida ishlash" kursida kompyuter savodxonligi va Word, Excel va Power Point dasturlarida ishlash o\'rgatiladi.')

    await db.add_course(
        "buxalteriya",
        "📊 Buxgalteriya",
        "balans1",
        "Buxgalteriya noldan balansgacha (3 oy)",
        "Umarbek Jabborov",
        "https://bit.ly/3pqXnKK",
        650_000,
        '👨‍💻 "Buxgalteriya noldan balansgacha" kursi mentori Umarbek Jabborov.\n\n📊 Buxgalteriya sohasida 21 yillik tajribaga ega mutaxassis, dotsent va iqtisod fanlari nomzodi. Faoliyati davomida 50 dan ortiq ilmiy ish va 20 dan ortiq xalqaro va respublika anjumanlarida chop qilingan tezislar muallifi. AQSH USAID fondining PRAGMA / KARANA loyihasi granti g\'olibi.\n\n📌 Umarbek Jabborovning 2 oylik "Buxgalteriya noldan balansgacha" kursi davomida buxgalteriya hisobining nazariy asoslari, moliyaviy natijalar, soliq hisobotlari bilan ishlash va shu sohaga oid bilimlarga ega bo\'lasiz')

    await db.add_course(
        "buxalteriya",
        "📊 Buxgalteriya",
        "balans2",
        "Buxgalteriya noldan balansgacha (2 oy)",
        "Faxriddin Raximov",
        "https://telegra.ph/file/7336d4bd9c4d3372db345.jpg",
        650_000,
        '👨‍💻 "Buxgalteriya noldan balansgacha" kursi mentori Umarbek Jabborov.\n\n📊 Buxgalteriya sohasida 21 yillik tajribaga ega mutaxassis, dotsent va iqtisod fanlari nomzodi. Faoliyati davomida 50 dan ortiq ilmiy ish va 20 dan ortiq xalqaro va respublika anjumanlarida chop qilingan tezislar muallifi. AQSH USAID fondining PRAGMA / KARANA loyihasi granti g\'olibi.\n\n📌 Umarbek Jabborovning 2 oylik "Buxgalteriya noldan balansgacha" kursi davomida buxgalteriya hisobining nazariy asoslari, moliyaviy natijalar, soliq hisobotlari bilan ishlash va shu sohaga oid bilimlarga ega bo\'lasiz')


    await db.add_course(
        "dev",
        "👨🏻‍💻 Dasturlash",
        "web",
        "🌐 Web-dasturlash",
        "WordPressda ishlash",
        "https://bit.ly/3ppr0fb",
        550_000,
        '👨🏻‍💻"WordPress"ga asoslangan web dasturlash kursi mentori Jamshidbek Qurbonboev.\n\n💻 Sohada 4 yillik tajribaga ega. Ayni paytda Xitoy davlatining "SWPU" universitetining "Computer engineering" kursi talabasi. Dasturlash yo\'nalishi bo\'yicha bir qancha ko\'rik tanlovlar g\'olibi.\n\n🖥 Texnologik malakasi: Word, Excel, Power Point, Elektron hujjatlar bazasini yaratish, QR kodlash, dasturlash.\n\n📌 Jamshidbek Qurbonboevning 3 oylik "WordPress"ga asoslangan web dasturlash kursida shaxsiy blog, internet do\'konlar va yangilik portallari kabi web saytlarni yaratishni o\'rganasiz.')

    await db.add_course(
        "arxdiz",
        "🏢 Arxitektura va dizayn",
        "arxitektura",
        "🏢 Arxitektura",
        "Sherzod Duschanov",
        "https://telegra.ph/file/2eec61167ff71ff833b79.jpg",
        750_000,
        "Arxitektura va dizayn sohasida 17 yillik tajribaga ega mutaxassis, ma'lumoti oliy. Faoliyati davomida bir qancha xususiy kompaniyalarda va davlat tashkilotlarida ishlagan. Yirik loyihalar ishtirokchisi va davlat tomonidan tashkil etilgan xalqaro tanlovlar g'olibi hamda sovrindori bo'lgan.\n\nTexnologik malakasi - ArchiCAD, AutoCAD, 3Ds MAX va Lumion"
        )

    await db.add_course(
        "arxdiz",
        "🏢 Arxitektura va dizayn",
        "vizual",
        "🌄 Vizual effekt",
        "Akmal Iskandarov",
        "https://telegra.ph/file/5136d0305106b8f4a6692.jpg",
        850_000,
        "Media sohasda 10 yillik tajribaga ega. Tasvirchi, montajchi va media dizayner. Faoliyati davomida ko'plab reklama roliklari ishlagan. \"DATA\" o'quv markazining Marketing bo'limida ishlagan. \"Real History\" va \"Strong Effect\" jamoasi a'zosi.\n\nTexnologik malakasi - Adobe Premiere Pro, Adobe After Effects, Cinema4D, Adobe Photoshop, Blender."
        )

    await db.add_course(
        "arxdiz",
        "🏢 Arxitektura va dizayn",
        "video",
        "📹 Opeatorlikka asoslangan video montaj",
        "Bekzod Abdullayev",
        "https://telegra.ph/file/5e2e39ae00c7375b9cdfe.jpg",
        950_000,
        "Professional videomaker. Media sohasida 10 yillik tajribaga ega. Faoliyati davomida \"8 TV\" telekanali, “SHERPRO” studiyasi va Xorazm viloyati turizmni rivojlantirish departamentida ishlagan. Ko‘plab media loyihalarda qatnashgan, videokliplar tayyorlagan. 10 dan ortiq mobil o‘yinlar ishlab chiqgan. “DATA” o‘quv markazida bosh media mutaxassisi."
        )

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
