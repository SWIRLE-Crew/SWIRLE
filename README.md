# SWIRLE
Secure Working Interpreter Robot Leaving Encryption (SWIRLE) is a Discord bot designed to test the implementation of encryption with the Discord API.

SWIRLE utilizes 3 forms of encryption to decrypt messages sent in the designated channel. The 3 forms of encryption are [Null cipher](https://en.wikipedia.org/wiki/Null_cipher), 
[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), and [Affine cipher](https://en.wikipedia.org/wiki/Affine_cipher).

For encrypting messages it is recommended to use [CyberChef](https://gchq.github.io/CyberChef/).

## Set Channel ID's
**This will require editing the .py file.**

On row *93* replace **'General Channel ID Here' (remove ' ')** with your *Channel ID*.
On row *108* replace **'Deciphered_Text Channel ID Here' (remove ' ')** with your *Channel ID*.
To get Channel ID go to *User Settings -> Advanced* and enable *Developer Mode*. Then right click the designated channel, at the bottom select **Copy ID**.

## Set BOT ID
**This will require editing the .py file.**

On the last row (229) replace **'Insert BOT ID Here' (leave ' ')** with your *BOT ID*.
For next step you will need to create a Discord BOT profile.
To get BOT ID go to [Discord Applications](https://discord.com/developers/applications) and select your application. Then select *BOT* and you can copy your *Token*.

## Commands

### .help
The help command will display a short description of the Discord bot and provide a link to the GitHub repository.

### .set_caesar
The set_caesar command will allow you to set the integer used for the shift in the cipher.

### .set_affine
The set_affine command will allow you to set the integer used for the shift in the cipher. The available values are **1**, **3**, **5**, **7**, and **9**.
