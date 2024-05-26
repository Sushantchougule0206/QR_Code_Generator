# step 1   take upi id from user
# step 2   declare payment url for every payment app which contains upi id and other details
# step 3   generate qrcode for every payment app
# step 4   display qrcode using pillow viwer
import qrcode

# Taking upi id as a input
upi_id=input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=NAME&cu=CURRENCY&tn=MESSAGE
'''pa= upi id , pn= recipent name , am = amount ,  cu = currency , tn= message box after payment'''

# Defining the payment URL based on the payment app
# you can modify these URLs based on the payment apps you want to support

phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR codes for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#Save the QR code to iamge file (optional)
'''phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')'''

# Display the QR codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()