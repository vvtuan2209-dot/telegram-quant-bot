require("dotenv").config();
const TelegramBot = require("node-telegram-bot-api");
const axios = require("axios");

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });

async function send(region, msg){

  const res = await axios.post(
    process.env.API_URL + "/predict/" + region
  );

  const d = res.data;

  bot.sendMessage(msg.chat.id,
`📊 V11 QUANT SYSTEM

Miền: ${region.toUpperCase()}

🔥 2 số: ${d.top_2digit.num}
🎲 3 số: ${d.top_3digit.num}

📈 Accuracy: ${d.backtest.accuracy}%
📊 Stability: ${d.backtest.stability}`
  );
}

bot.onText(/\/mn/,m=>send("mn",m));
bot.onText(/\/mt/,m=>send("mt",m));
bot.onText(/\/mb/,m=>send("mb",m));
