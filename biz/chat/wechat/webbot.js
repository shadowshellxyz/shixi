import { WechatyBuilder } from 'wechaty'

const bot = WechatyBuilder.build() // get a Wechaty instance

// 登录
async function onLogin(user) {
    console.log(`贴心小助理${user}登录了`);

    bot
}


async function onMessage(message) {

    console.log(`Message: ${message}`);

    if (message.text() === 'ding') {
        await message.say('dong');
        console.log(JSON.stringify(message));
        const room = await bot.Room.find({ topic: 'ShadowShell' })
        if (room) {
          // send a message
          await room.say("Hello World.");
        }

        const contact = await bot.Contact.find({name: "ShadowShellXyz"}) || await bot.Contact.find({alias: "ShadowShellXyz"});
        const content = '商品：\n https://item.jd.com/52672000539.html';
        await contact.say(content);
    }
}



bot
  .on('scan', (qrcode, status) => console.log(`Scan QR Code to login: ${status}\nhttps://wechaty.js.org/qrcode/${encodeURIComponent(qrcode)}`))
  .on('login', onLogin)
  .on('message',  onMessage)

bot.start()