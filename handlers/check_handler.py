from telegram import Update
from telegram.ext import ContextTypes
from services import check_nrk

async def check_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        employee_id = context.args[0]

        employee_data = await check_nrk(employee_id) 
        if employee_data:
            employee_data = employee_data[0]
            format_data = f"""*NOMOR NRK* : {employee_data['NRK']}

UNIT KERJA : {employee_data['UNIT_KERJA']}
ALAMAT : {employee_data["ALAMAT_UNIT_KERJA"]}
PERANGKAT : {employee_data["PERANGKAT_DAERAH"]}

*DATA IDENTITAS* :
THBL : {employee_data["THBL"]}
NAMA : {employee_data["NAMA"]}
NIP18 : {employee_data["NIP18"]}
NIK : {employee_data["NIK"]}

*KONTAK* : 
EMAIL : {employee_data["EMAIL"]}
NO HP :  {employee_data["NOHP"]}
"""
            await update.message.reply_text(format_data, parse_mode='Markdown')
        else:
            await update.message.reply_text(f"{employee_id} tidak ditemukan.")

    else:
        await update.message.reply_text("Harap masukkan ID karyawan setelah perintah, seperti: /cek 123")
