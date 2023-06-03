const { default: axios } = require('axios');
const qrcode = require('qrcode-terminal');

const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const client = new Client({
    puppeteer: {
		args: ['--no-sandbox'],
	},
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
            try{
                chat.sendMessage(stickerMedia,{sendMediaAsSticker:true})
            }
            catch {
                chat.sendMessage("Sticker Creation Faild")
            }
        }
        else{

        }
        
	}
    if(message.body.includes('!sticker') && message.body.includes('!nobg')) {
        if(message.hasMedia){
            const chat = await message.getChat()
            const stickerMedia = await message.downloadMedia()
            try{
                axios.post("http://localhost:5000/nobg",{image:stickerMedia.data})
                .then((res)=>{
                    const stickerMedia = MessageMedia.fromFilePath('images/nobg.png');
                    chat.sendMessage(stickerMedia,{sendMediaAsSticker:true})
                })
            }
            catch {
                chat.sendMessage("Sticker Creation Faild")
            }
        }
        else{
            
        }
        
	}
    if(message.body.includes('!music')) {
            const chat = await message.getChat()
            axios.post("http://localhost:5000/music",{music:message.body.replace("!music","")})
            .then((res)=>{
                const voice = MessageMedia.fromFilePath('music/output.opus');
                chat.sendMessage(voice,{sendAudioAsVoice:true})
            })
            
        }
});
 

client.initialize();
