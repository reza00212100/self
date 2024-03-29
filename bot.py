import os
import jdatetime
import pytz
import speedtest
import aiocron
import asyncio
import googlesearch
import requests
import time
from PIL import Image, ImageSequence
from googletrans import Translator
from gtts import gTTS
from moviepy.editor import VideoFileClip
from pyrogram import Client, filters, enums
from pytube import YouTube

api_id = 13893053
api_hash = "f586d92837b0f6eebcaa3e392397f47c"
app = Client("my_accound", api_id=api_id, api_hash=api_hash)


def number_change(num):
    numbers = {"0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"}
    if numbers[num]:
        return numbers[num]


@aiocron.crontab('*/1 * * * *')
async def timeer():
    ir = pytz.timezone("Asia/Tehran")
    date = str(jdatetime.datetime.now(ir).strftime("%-H •° %-M"))
    text = ""
    for i in date:
        try:
            int(i)
            text += number_change(i)
        except:
            text += i
    await app.update_profile(first_name="𝓡𝓔𝓩𝓐 𝓑 𝓩", last_name=text)


@app.on_message(filters.me & filters.regex("^!message$"))
def print_message(c, m):
    if len(str(m)) > 2000:
        m.reply(str(m)[:2000])
        m.reply(str(m)[2000:])
    else:
        m.reply(str(m))


@app.on_message(filters.me & filters.regex("^(s|S)peed$"))
def speedtestsw(client, message):
    speed = speedtest.Speedtest()
    down = round(speed.download() / 1024 / 1024)
    upl = round(speed.upload() / 1024 / 1024)
    text = f"Download speed: {down} Mb/s\nUpload speed: {upl} Mb/s"
    message.reply(text)


@app.on_message(filters.regex("!stop") & filters.me)
def conver_webp(c, m):
    chat_id = m.chat.id
    message_id = m.id
    id = m.reply_to_message_id
    if (m.reply_to_message.sticker.is_animated) == False:
        m.delete()
        file = m.reply_to_message.sticker.file_id
        down = c.download_media(file, "sticker.webp")
        img = Image.open('downloads/sticker.webp').convert("RGBA")
        img.save("image.png", "PNG")
        c.send_photo(chat_id, "image.png", reply_to_message_id=id)
        c.send_document(chat_id, document="image.png", reply_to_message_id=id)
        os.remove("image.png")
        os.remove('downloads/sticker.webp')
    else:
        c.edit_message_text(chat_id, message_id,
                            "opps...\nthis sticker is animated\nme can convert the stickers that are not animated🥺\n")


def thumbnails(frames, size):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail


@app.on_message(filters.me & filters.regex("!ftog$"))
def f_to_gif(client, message):
    message_id = message.id
    chat_id = message.chat.id
    file_id = message.reply_to_message_id
    id = message.reply_to_message.video.file_id
    client.delete_messages(chat_id, message_id)
    down = client.download_media(id)
    clip = VideoFileClip(down)
    clip.write_gif("nowgif.gif")
    im = Image.open("nowgif.gif")
    frames = ImageSequence.Iterator(im)
    size = 340, 240
    frames = thumbnails(frames, size)
    om = next(frames)  # Handle first frame separately
    om.info = im.info  # Copy sequence info
    om.save("nowgif.gif", save_all=True, append_images=list(frames))
    client.send_animation(chat_id, "nowgif.gif", reply_to_message_id=file_id)
    os.remove(down)
    os.remove("nowgif.gif")


@app.on_message(filters.me & (
        filters.regex("لایک") | filters.regex("دوس") | filters.regex("عالیه") | filters.regex("حق") | filters.regex(
    "👍")))
def like(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "👍")


@app.on_message(filters.me & (filters.regex("نموخام") | filters.regex("مزخرف") | filters.regex("👎")))
def not_like(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "👎")


@app.on_message(filters.me & (filters.regex("عشق") | filters.regex("عاشق") | filters.regex("زندگیمی") | filters.regex(
    "فداتشم") | filters.regex("❤️")))
def love(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "❤️")


@app.on_message(
    filters.me & (filters.regex("هورا") | filters.regex("جشن") | filters.regex("مبارک") | filters.regex("🎉")))
def hoppy(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "🎉")


@app.on_message(
    filters.me & (filters.regex("ریدم") | filters.regex("تف") | filters.regex("گوه") | filters.regex("💩")))
def goh(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "💩")


@app.on_message(filters.me & (filters.regex("شیطون") | filters.regex("شیطونی") | filters.regex("😁")))
def lucifer(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "😁")


@app.on_message(
    filters.me & (filters.regex("جووون") | filters.regex("خوشکله") | filters.regex("زیبا") | filters.regex("🤩")))
def biutiful(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "🤩")


@app.on_message(filters.me & (
        filters.regex("اتیش") | filters.regex("اتیشپاره") | filters.regex("بخورمت") | filters.regex(
    "اتیشی") | filters.regex("🔥")))
def fire(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "🔥")


@app.on_message(
    filters.me & (filters.regex("مشکل") | filters.regex("نکن") | filters.regex("عجیبه") | filters.regex("😱")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "😱")


@app.on_message(filters.me & (
        filters.regex("مخم ترکید") | filters.regex("این چی بود") | filters.regex("وای خدا") | filters.regex("🤯")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id
        client.send_reaction(chat_id, message_id, "🤯")


@app.on_message(
    filters.me & (filters.regex("تشویق") | filters.regex("تکبیر") | filters.regex("افرین") | filters.regex("👏🏻")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "👏🏻")


@app.on_message(
    filters.me & (filters.regex("فوش") | filters.regex("چرت") | filters.regex("دعوا") | filters.regex("🤬")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "🤬")


@app.on_message(
    filters.me & (filters.regex("ببخشید") | filters.regex("ببشید") | filters.regex("اشتی") | filters.regex("😢")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "🤮")


@app.on_message(filters.me & (
        filters.regex("حالم بهم خورد") | filters.regex("چه زشت") | filters.regex("حالت تهوع") | filters.regex("🤮")))
def amazing(client, message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message_id
        client.send_reaction(chat_id, message_id, "😢")


@app.on_message(filters.me & (filters.regex("^!youdl ")))
def youtube_downloader(client, message):
    message.reply("ok")
    url = str(message.text)[7:]
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    if stream.mime_type == 'video/mp4':
        name = video.title + ".mp4"
        re = message.reply("download...")
        stream.download()
        re.delete()
        fe = message.reply("upload...")
        message.reply_video(name)
        fe.delete()


@app.on_message(filters.me & (filters.regex("^!info$")))
def info(client, message):
    chat_id = message.chat.id
    message.delete()
    id = message.reply_to_message_id
    text = f"**INFO USER**\n🆔✝️ **message id :** `{id}`\n"
    text += f"🆔 **id:** `{message.reply_to_message.from_user.id}`\n📝 **is contact:** `{message.reply_to_message.from_user.is_contact}`\n"
    text += f"✏️ **first name:** `{message.reply_to_message.from_user.first_name}`\n"
    if message.reply_to_message.from_user.last_name:
        text += f"✏️ **last name:** `{message.reply_to_message.from_user.last_name}`\n"
    text += f"🆔✝️ **username:** @{message.reply_to_message.from_user.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={message.reply_to_message.from_user.id})"
    if message.reply_to_message.from_user.photo:
        file = message.reply_to_message.from_user.photo.big_file_id
        down = client.download_media(file)
        client.send_document(chat_id, document=down, caption=text, reply_to_message_id=id,
                             parse_mode=enums.ParseMode.MARKDOWN)
        os.remove(down)
    else:
        client.send_message(chat_id, text, reply_to_message_id=id, parse_mode=enums.ParseMode.MARKDOWN)


@app.on_message((filters.me) & (filters.regex("^!infof$")))
def infof(client, message):
    chat_id = message.chat.id
    message.delete()
    id = message.reply_to_message_id
    text = f"**INFO FROM USER**\n🆔✝️ **message id :** `{id}`\n"
    if message.reply_to_message.forward_sender_name:
        text += f"❌🔒 ooppsss... 🔒❌\nthe sender of this message has locked his profile.\n🔏 **name sender message :** `{message.reply_to_message.forward_sender_name}`\n"
        client.send_message(chat_id, text, reply_to_message_id=id)
    else:
        text += f"🆔 **id:** `{message.reply_to_message.forward_from.id}`\n📝 **is contact:** `{message.reply_to_message.forward_from.is_contact}`\n"
        text += f"✏️ **first name:** `{message.reply_to_message.forward_from.first_name}`\n"
        if message.reply_to_message.forward_from.last_name:
            text += f"✏️ **last name:** `{message.reply_to_message.forward_from.last_name}`\n"
        text += f"🆔✝️ **username:** @{message.reply_to_message.forward_from.username}\n[👀 SEE PROFILE 👀](tg://openmessage?user_id={message.reply_to_message.forward_from.id})"
        if message.reply_to_message.forward_from.photo:
            file = message.reply_to_message.forward_from.photo.big_file_id
            down = client.download_media(file)
            client.send_document(chat_id, document=down, caption=text, reply_to_message_id=id,
                                 parse_mode=enums.ParseMode.MARKDOWN)
            os.remove(down)
        else:
            client.send_message(chat_id, text, reply_to_message_id=id, parse_mode=enums.ParseMode.MARKDOWN)


@app.on_message(filters.me & filters.regex("^(d|D) "))
def download_image(client, message):
    message.edit_text("چه زیباس")
    prson = message.text[2:]
    if message.reply_to_message.photo:
        id = message.reply_to_message.photo.file_id
    if message.reply_to_message.video:
        id = message.reply_to_message.video.file_id
    if message.reply_to_message.audio:
        id = message.reply_to_message.audio.file_id
    down = client.download_media(id)
    if prson == "me":
        client.send_document("me", document=down)
    else:
        client.send_document(int(prson), document=down)
    os.remove(down)


@app.on_message(filters.me & filters.regex("^!srch "))
def search(client, message):
    text = message.text
    text = text[6:].replace(" ", "+")
    result = googlesearch.search(text, num_results=5)
    tex = ""
    der = 1
    for i in result:
        response = requests.get(i).text
        x = response.find("<title>")
        y = response.find("</title>", x)
        link = response[x + 7:y]
        tex += f"{der} ➖ [{link}]({i})\n"
        der += 1
    message.reply(tex)
    message.delete()


@app.on_message(filters.regex("^!trans ") & filters.me)
def translate(client, message):
    text = message.reply_to_message.text
    text2 = message.text
    text2 = text2.replace("!trans ", "")
    dest = text2.split()[0]
    translator = Translator()
    result = translator.translate(text, dest=dest)
    client.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=result.text)


@app.on_message(filters.regex("^!tts$") & filters.me)
def tts(client, message):
    chat_id = message.chat.id
    message_id = message.id
    text = message.reply_to_message.text
    language = "en"
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("test.ogg")
    client.send_audio(chat_id, "test.ogg", reply_to_message_id=message_id)
    os.remove('test.ogg')


@app.on_message(filters.me & filters.regex("^!vazhe "))
def vazhe(client, message):
    text = message.text
    chat_id = message.chat.id
    name = text.replace("!vazhe ", "")
    Response = requests.post(f"https://api.codebazan.ir/vajehyab/?text={name}")
    tex = Response.json()
    fa = tex["result"]["fa"]
    en = tex["result"]["en"]
    moein = tex["result"]["Fmoein"]
    deh = tex["result"]["Fdehkhoda"]
    mo = tex["result"]["motaradefmotezad"]
    text = f"**فارسی کلمه:** `{fa}`\n**تلفظ کلمه: ** `{en}`\n\n**معنی کلمه در فرهنگ لغت معین: ** `{moein}`\n\n**معنی کلمه در فرهنگ لغت دهخدا: ** `{deh}`\n\n**مترادف و متضاد کلمه: ** `{mo}`"
    client.edit_message_text(chat_id, message_id=message.id, text=text)


@app.on_message(filters.me & filters.regex("^!num "))
def numtofa(client, message):
    text = message.text
    chat_id = message.chat.id
    nume = text.replace("!num ", "")
    Response = requests.post(f"https://api.codebazan.ir/num/?num={nume}")
    tex = Response.json()
    client.edit_message_text(chat_id, message_id=message.id, text=tex["result"]["num"])


@app.on_message(filters.me & filters.regex("^!pdf "))
def webtopdf(client, message):
    text = message.text
    chat_id = message.chat.id
    name = text.replace("!pdf ", "")
    tex = name[0:5]
    if tex == "https":
        name = name[8:]
        url1 = "https://" + name
    if tex == "http:":
        name = name[7:]
        url1 = "http://" + name
    Response = requests.post(f"https://api.codebazan.ir/htmltopdf/?type=json&url={url1}")
    tex = Response.json()
    url = tex["result"]["url"]
    pdf = requests.get(url)
    time.sleep(3)
    namefile = "test.pdf"
    with open("webtopdf.pdf", "wb") as f:
        f.write(pdf.content)
    client.send_document(chat_id, "webtopdf.pdf", reply_to_message_id=message.id)
    os.remove("webtopdf.pdf")


@app.on_message(filters.me & filters.regex("^!pass "))
def password_gen(client, message):
    text = message.text
    messag_id = message.id
    name = text.replace("!pass ", "")
    Response = requests.post(f"http://api.codebazan.ir/password/?length={name}")
    client.edit_message_text(chat_id=message.chat.id, message_id=messag_id, text=Response.text)


@app.on_message(filters.me & filters.regex("^!. "))
def strrev(client, message):
    text = message.text
    messag_id = message.id
    name = text.replace("!. ", "")
    Response = requests.post(f"http://api.codebazan.ir/strrev/?text={name}")
    client.edit_message_text(chat_id=message.chat.id, message_id=messag_id, text=Response.text)


@app.on_message(filters.me & filters.regex("^!font "))
def font(client, message):
    text = message.text
    messag_id = message.id
    text = text.replace("!font ", "")
    Response = requests.post(f"http://api.codebazan.ir/font/?text={text}")
    tex = Response.json()
    result = ""
    for i in tex["result"]:
        font = tex["result"][i]
        result += f"**{i}:**`{font}`\n\n"
    client.edit_message_text(chat_id=message.chat.id, message_id=messag_id, text=result)


@app.on_message(filters.me & filters.regex("^!fontfa "))
def fontfa(client, message):
    text = message.text
    messag_id = message.id
    text = text.replace("!fontfa ", "")
    Response = requests.post(f"https://api.codebazan.ir/font/?type=fa&text={text}")
    tex = Response.json()
    result = ""
    for i in tex["Result"]:
        font = tex["Result"][i]
        result += f"**{i}:**`{font}`\n"
    client.edit_message_text(chat_id=message.chat.id, message_id=messag_id, text=result)


@app.on_message(filters.me & filters.regex("^!ttr "))
def ttr(client, message):
    text = message.reply_to_message.text
    tex = message.text
    chat_id = message.chat.id
    language = tex.replace("!ttr ", "")
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("testvoice.ogg")
    client.send_audio(chat_id, "testvoice.ogg", reply_to_message_id=message.id)
    os.remove('testvoice.ogg')


@app.on_message(filters.me & filters.regex("!del$"))
def delete_mess(client, message):
    message_id = message.id
    chat_id = message.chat.id
    client.delete_messages(chat_id, message_id)
    message_id = message.reply_to_message_id
    client.delete_messages(chat_id, message_id)


@app.on_message(filters.me & filters.regex("^!meli"))
def meli(client, message):
    text = message.text
    code = text.replace("!meli ", "")
    Response = requests.post(f"https://api.codebazan.ir/codemelli/?code={code}")
    tex = Response.json()
    client.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=tex["Result"])


@app.on_message(filters.me & filters.regex("!down "))
def download(client, message):
    text = message.text
    url = text[6:]
    response = requests.get(url, stream=True)
    message_id = message.id
    chat_id = message.chat.id
    file_name = os.path.basename(url)
    file = response.raw
    client.edit_message_text(chat_id, message_id, f"👾 **DOWNLOADING...**\n**FILE NAME:** {file_name}\n")
    f = open(file_name, 'wb')
    for chunk in response.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    client.edit_message_text(chat_id, message_id, f"👾 **UPLOADING...**\n**FILE NAME:** {file_name}\n")
    client.send_document(chat_id, file_name, reply_to_message_id=message_id)
    os.remove(file_name)


@app.on_message(filters.me & filters.regex("^!help$"))
def help(client, message):
    help = ""
    help += "**command:**\n!info \n**descriptin:**\nsend info user replyed message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!infof \n**descriptin:**\nsend info user forward message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!stop \n**descriptin:**\nconvert replyed sticker to png\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!ftog \n**descriptin:**\nconvert replyed movie to gif\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!down \n**descriptin:**\nget link download and upload to " \
            "telegram\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!del \n**descriptin:**\nget reply message and delete " \
            "message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!srch \n**descriptin:**\nget text and show result search\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!trans \n**descriptin:**\nget text and source language and defective language so print " \
            "trtanslate\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!tts \n**descriptin:**\nget text and send voice text to language english " \
            "\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n! \n**descriptin:**\nget text and print it slowly\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!meli\n**descriptin:**\nsend result sending code meli\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!vazhe\n**descriptin:**\nget word prsion and send meaning\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!num\n**descriptin:**\nget number and send number to " \
            "persion\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!.\n**descriptin:**\nget string and send strrev\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!font\n**descriptin:**\nget name or any thing and send difrent " \
            "fonts\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!fontfa\n**descriptin:**\nget persion text and send difrent " \
            "font\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!ttr\n**descriptin:**\nget language and text so send voice text withe input language " \
            "\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n!pdf\n**descriptin:**\nget link web and send pdf shot web \n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n"
    help += "**command:**\n!pass\n**descriptin:**\nget number and genereat password to len " \
            "number\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    help += "**command:**\n(دانلود نمیشه|صبر کن دانلود شه)\n**descriptin:**\ndownload and send media to saved  " \
            "message\n\n/*/*/*/*/*/*/*/*/*/*/*/*/\n\n "
    client.edit_message_text(chat_id=message.chat.id, message_id=message.id, text=help)


app.run()  # Automatically start() and idle()
timeer.start()
asyncio.get_event_loop().run_forever()
