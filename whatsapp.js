const { default: axios } = require('axios');
const qrcode = require('qrcode-terminal');

const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const client = new Client({
    authStrategy: new LocalAuth()
});

client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

client.on('message',async message => {
	if(message.body === '!sign') {
        const chat = await message.getChat()
        axios.post("http://localhost:5000/",{name:message._data.notifyName})
        .then((res)=>{
            const stickerMedia = MessageMedia.fromFilePath('images/sign.png');
            chat.sendMessage(stickerMedia,{sendMediaAsSticker:true})
        })
		
	}
    if(message.body === '!sticker') {

        if(message.hasMedia){
            const chat = await message.getChat()
            const stickerMedia = await message.downloadMedia()
            chat.sendMessage(stickerMedia,{sendMediaAsSticker:true})
        }
        
	}
});
 

client.initialize();
