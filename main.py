from aiogram import Bot, Dispatcher, executor, types
import python_weather


bot = Bot(token="5562729078:AAEb8045iciSikFA7XIq_2NnVu0LS4BXgK4")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")


@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = (weather.current.temperature - 32) / 1.8

    resp_msg = weather.location_name + '\n'
    resp_msg += f"Текущая температура: {round(celsius)}°\n"
    resp_msg += weather.current.sky_text + "\n"

    await message.answer(resp_msg)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
