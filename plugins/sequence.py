from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_file_sequences = {}

# Function for processing file sequence
async def process_file_sequence(client, message, file_type):
    user_id = message.from_user.id

    if user_id in user_file_sequences:
        user_data = user_file_sequences[user_id]

        file = getattr(message, file_type, None)

        if file:
            user_data["files"].append(message)
            await message.reply_text("File received and added to the sequencing process.")
        else:
            await message.reply_text("Unsupported file type. Send documents or videos.")

# Function to end the sequence and get sequenced files
async def end_sequence(client, message):
    user_id = message.from_user.id

    if user_id in user_file_sequences:
        user_data = user_file_sequences[user_id]

        if user_data["files"]:
            user_data["files"].sort(key=lambda x: x.document.file_name if x.document else x.video.file_name)

            for file_message in user_data["files"]:
                file = file_message.document or file_message.video

                if file:
                    caption = file_message.caption or ''
                    await message.reply_document(file.file_id, caption=caption)

            await message.reply_text(f"File sequencing completed. You have received {len(user_data['files'])} sequenced files.")
            del user_file_sequences[user_id]
        
# Function to start file sequencing process
@Client.on_message(filters.command("ssequence"))
async def start_sequence(client, message):
    user_id = message.from_user.id

    if user_id in user_file_sequences:
        await message.reply_text("You are currently in a file sequencing process. Use /esequence to finish it.")
        return

    user_file_sequences[user_id] = {"files": []}
    await message.reply_text("You have started a file sequencing process. Send the files you want to sequence one by one. "
                              "When you are done, use /esequence to finish and get the sequenced files.")

# Command to end the sequence
@Client.on_message(filters.command("esequence"))
async def end_sequence_command(client, message):
    await end_sequence(client, message)

# Command to cancel the sequence
@Client.on_message(filters.command("cancel"))
async def cancel_sequence(client, message):
    user_id = message.from_user.id

    if user_id in user_file_sequences:
        del user_file_sequences[user_id]
        await message.reply_text("File sequencing process canceled. Use /ssequence to start a new one.")
    else:
        await message.reply_text("No ongoing file sequencing process to cancel. Use /ssequence to begin.")

# Command to show bot stats
@Client.on_message(filters.command("stats"))
async def show_stats(client, message):
    total_sequences = sum(len(user_data["files"]) for user_data in user_file_sequences.values())
    await message.reply_text(f"Total File Sequences: {total_sequences}")
