**# Chamcode SMS Program**

Welcome to the Chamcode SMS program! This project uses the Twilio API to send SMS messages to a list of phone numbers. The program is written in Python and can be easily customized to send messages to different recipients.

**## Prerequisites**

- Python 3.x
- Twilio account with a registered phone number
- Twilio Python SDK (`twilio` package)
- `python-dotenv` (optional for managing environment variables)

**## Installation**

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/kcham193/THE-CHAMCODES-SMS--PYTHON.git
   cd THE-CHAMCODES-SMS--PYTHON
2. Install the required Python packages.
    pip install twilio


**If you're using environment variables, you may also want to install python-dotenv:**
   pip install python-dotenv

   
**Usage**
**1. Set up your Twilio account credentials:**


- Replace 'XXXXXXXXXXXXXXXXXXX' in the account_sid and auth_token variables with your actual Twilio Account SID and Auth Token.
- If you're using environment variables, create a .env file in the project directory and add your credentials:
  ```
  TWILIO_ACCOUNT_SID=your_account_sid
  
  TWILIO_AUTH_TOKEN=your_auth_token

**2. Then modify the script to load these variables:**
 ```
  from dotenv import load_dotenv
  import os

  load_dotenv()
  account_sid = os.getenv('TWILIO_ACCOUNT_SID')
  auth_token = os.getenv('TWILIO_AUTH_TOKEN')
 ```


**2. Customize the message and recipient list:**

  Add the phone numbers you want to send SMS to in the phone_numbers list.
  Modify the message variable with the message you want to send.

**3. Run the script:**

  python send_sms.py

- The script will send the specified message to each phone number in the list and print the message SID for each successful send. If an error occurs, it will be printed to the console.


**Important Notes**

- Ensure that the phone numbers in the phone_numbers list are in the correct format (E.164 format with a leading + and country code).
- Do not share your Twilio Account SID and Auth Token publicly. Treat these credentials as sensitive information.




**Acknowledgements**

-Twilio for providing the SMS API.



**Contributing**

- Feel free to submit issues or pull requests if you want to contribute to this project.



**Contact**

- For any questions or suggestions, please contact kassimchambulilo@gmail.com




