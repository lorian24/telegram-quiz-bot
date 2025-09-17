import logging
import pandas as pd
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Вставь сюда свой токен, полученный от @BotFather
TOKEN = "7646994832:AAG8K04D-_cZYbUFpLERYpN4sBEGF0_8NPs"

# Вопросы будут храниться в этом файле
QUESTIONS_FILE = "questions.xlsx"

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Загружаем вопросы из Excel
def load_questions():
    df = pd.read_excel(QUESTIONS_FILE)
    return df.to_dict(orient="records")

questions = load_questions()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для японского языка. Напиши /quiz, чтобы получить вопрос.")

# Команда /quiz
async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    q = random.choice(questions)
    question_text = q["Вопрос"]
    answers = [q["Ответ 1"], q["Ответ 2"], q["Ответ 3"]]
    correct = q["Ответ"]

    text = f"❓ {question_text}\n\n1) {answers[0]}\n2) {answers[1]}\n3) {answers[2]}"
    await update.message.reply_text(text + f"\n\n✅ Правильный ответ: {correct}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", quiz))
    app.run_polling()

if __name__ == "__main__":
    main()

