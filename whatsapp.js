const qrcode = require('qrcode-terminal');

const { Client } = require('whatsapp-web.js');
const client = new Client();

client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on("message",(message)=>{
    const stickerMedia = MessageMedia.fromFilePath('./sign.webp');
    client.sendMessage(message.from,stickerMedia,{sendMediaAsSticker:true})
})

client.initialize();
 