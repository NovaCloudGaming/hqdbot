from telebot import types


# Main menu
main_menu = types.InlineKeyboardMarkup(row_width=3)
main_menu.add(
    types.InlineKeyboardButton(text='🛍 Каталог', callback_data='catalog1'),
    types.InlineKeyboardButton(text='👤 Профиль', callback_data='profile'),
    types.InlineKeyboardButton(text='ℹ️ Информация', callback_data='info'),
    types.InlineKeyboardButton(text='🛒 Корзина', callback_data='purchases'),
    types.InlineKeyboardButton(text='💸 Пополнить баланс', callback_data='replenish_balance1'),
)

korz5 = types.InlineKeyboardMarkup(row_width=2)
korz5.add(
    types.InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data='korz1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back7')
)
korz4 = types.InlineKeyboardMarkup(row_width=2)
korz4.add(
    types.InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data='korz1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back6')
)
korz3 = types.InlineKeyboardMarkup(row_width=2)
korz3.add(
    types.InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data='korz1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back5')
)

korz2 = types.InlineKeyboardMarkup(row_width=2)
korz2.add(
    types.InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data='korz1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back4')

)

korz = types.InlineKeyboardMarkup(row_width=2)
korz.add(
    types.InlineKeyboardButton(text='🛒 Добавить в корзину', callback_data='korz1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back3')

)

hqd2 = types.InlineKeyboardMarkup(row_width=3)
hqd2.add(
    types.InlineKeyboardButton(text='🍓', callback_data='klub'),
    types.InlineKeyboardButton(text='Blueberry🫐', callback_data='bl'),
    types.InlineKeyboardButton(text='🍌', callback_data='ban'),
    types.InlineKeyboardButton(text='🍒', callback_data='vish'),
    types.InlineKeyboardButton(text='🍑', callback_data='pers'),
    types.InlineKeyboardButton(text='🍇', callback_data='vin'),
    types.InlineKeyboardButton(text='🍏', callback_data='apple'),
    types.InlineKeyboardButton(text='Mango', callback_data='man'),
    types.InlineKeyboardButton(text='Lychee', callback_data='lich'),
    types.InlineKeyboardButton(text='🍊', callback_data='apel'),
    types.InlineKeyboardButton(text='Дыня', callback_data='din'),
    types.InlineKeyboardButton(text='Multifruit', callback_data='mult'),
    types.InlineKeyboardButton(text='🍍', callback_data='ananas'),
    types.InlineKeyboardButton(text='🍋🥧', callback_data='lim'),
    types.InlineKeyboardButton(text='Корица', callback_data='Cin'),
    types.InlineKeyboardButton(text='Сola', callback_data='cola'),
    types.InlineKeyboardButton(text='Mint', callback_data='mint'),
    types.InlineKeyboardButton(text='🌰', callback_data='oreh'),
    types.InlineKeyboardButton(text='Назад', callback_data='back2')
)

jul1 = types.InlineKeyboardMarkup(row_width=3)
jul1.add(
    types.InlineKeyboardButton(text='Slate', callback_data='sl'),
    types.InlineKeyboardButton(text='Ruby', callback_data='rub'),
    types.InlineKeyboardButton(text='Silver', callback_data='sil'),
    types.InlineKeyboardButton(text='Назад', callback_data='back2')
)

vap1 = types.InlineKeyboardMarkup(row_width=3)
vap1.add(
    types.InlineKeyboardButton(text='Gray', callback_data='fi1'),
    types.InlineKeyboardButton(text='Red', callback_data='fi1'),
    types.InlineKeyboardButton(text='Rose', callback_data='fi1'),
    types.InlineKeyboardButton(text='Gold', callback_data='fi1'),
    types.InlineKeyboardButton(text='Blue', callback_data='fi1'),
    types.InlineKeyboardButton(text='Dark Blue', callback_data='fi1'),
    types.InlineKeyboardButton(text='Dark Red', callback_data='fi1'),
    types.InlineKeyboardButton(text='Black', callback_data='fi1'),
    types.InlineKeyboardButton(text='Назад', callback_data='back2')
)
voop1 = types.InlineKeyboardMarkup(row_width=3)
voop1.add(
    types.InlineKeyboardButton(text='Fiesta', callback_data='fi'),
    types.InlineKeyboardButton(text='Klein blue', callback_data='fi'),
    types.InlineKeyboardButton(text='Tidal', callback_data='fi'),
    types.InlineKeyboardButton(text='lnk', callback_data='fi'),
    types.InlineKeyboardButton(text='Aurora', callback_data='fi'),
    types.InlineKeyboardButton(text='Nebulas Blue', callback_data='fi'),
    types.InlineKeyboardButton(text='Ceylon Yellow', callback_data='fi'),
    types.InlineKeyboardButton(text='Назад', callback_data='back2')
)

jij1 = types.InlineKeyboardMarkup(row_width=1)
jij1.add(
    types.InlineKeyboardButton(text="Bad Salts Don't Care Bear  45", callback_data='111'),
    types.InlineKeyboardButton(text="Bad Salts Farley's Gnarly Sauce 45", callback_data='222'),
    types.InlineKeyboardButton(text='I Love Salts Spearmint Gum 50', callback_data='333'),
    types.InlineKeyboardButton(text='Lemon Twist Salt Arctic Cool Mint 35', callback_data='444'),
    types.InlineKeyboardButton(text='Kernel Salt Popcorn Caramel 50', callback_data='555'),
    types.InlineKeyboardButton(text='Doozy Apple Mango Salt 50', callback_data='666'),
    types.InlineKeyboardButton(text='Skwezed Salt Green Apple 50', callback_data='777'),
    types.InlineKeyboardButton(text='Juice Man Salt Unicorn Frappe 50', callback_data='888'),
    types.InlineKeyboardButton(text='Fresh Farms Morning Melon 50', callback_data='999'),
    types.InlineKeyboardButton(text='Dinner Lady Lemon Sherbet 50', callback_data='1010'),
    types.InlineKeyboardButton(text='Назад', callback_data='back2')
)
catalog2 = types.InlineKeyboardMarkup(row_width=2)
catalog2.add(
    types.InlineKeyboardButton(text='HQD', callback_data='hqd1'),
    types.InlineKeyboardButton(text='Juul Basic ', callback_data='jul'),
    types.InlineKeyboardButton(text='VOOPOO DRAG NANO', callback_data='voop'),
    types.InlineKeyboardButton(text='Vaporesso OSMALL ', callback_data='vap'),
    types.InlineKeyboardButton(text='Солевые жидкости ', callback_data='jij'),
    types.InlineKeyboardButton(text='Назад', callback_data='back')

)

oplata = types.InlineKeyboardMarkup(row_width=2)
oplata.add(
    types.InlineKeyboardButton(text='100руб', callback_data='100'),
    types.InlineKeyboardButton(text='300руб', callback_data='300'),
    types.InlineKeyboardButton(text='500руб', callback_data='500'),
    types.InlineKeyboardButton(text='1000руб', callback_data='1000')
)

oplatil = types.InlineKeyboardMarkup(row_width=2)
oplatil.add(
    types.InlineKeyboardButton(text='✅ Я оплатил', callback_data='oplatil1'),

)


btn_purchase = types.InlineKeyboardMarkup(row_width=2)
btn_purchase.add(
    types.InlineKeyboardButton(text='Купить', callback_data='buy'),
    types.InlineKeyboardButton(text='Выйти', callback_data='exit_to_menu')
)

btn_ok = types.InlineKeyboardMarkup(row_width=3)
btn_ok.add(
    types.InlineKeyboardButton(text='Понял', callback_data='btn_ok')
)

replenish_balance = types.InlineKeyboardMarkup(row_width=3)
replenish_balance.add(
    types.InlineKeyboardButton(text='🔄 Проверить', callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel_payment')
)

to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)




