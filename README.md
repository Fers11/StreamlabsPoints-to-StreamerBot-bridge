Info: 
- Made with ChatGPT.
- Uses https://streamlabs.com/dashboard#/loyalty.
- I'm not sure if it works with Cloudbot.
- Not sure if it can handle large amount off Redemptions.
- If something is not working Restart the Script.

1. Go in the file and Replace YourSocketTokenHere with your StreamLabs Socket API Token. You find it here: https://streamlabs.com/dashboard#/settings/api-settings -> API Token -> Your Socket API Token !!! Do not share !!!

2. Go to REWARD_ACTIONS. Add your redemptions form StreamLabs and Actions from StreamerBot
e. g.

 REWARD_ACTIONS = {
    "VIP": "VIP",
    "TTS": "TTS"
}

4. Start the Websocket Server in StreamerBot.
    - Auto Start: On
    - Adress: 127.0.0.1
    - Port: 8080
    - Endpoint: /
    - Authentication: Off
    - Press on Start Server
  
5. Install atleast Python 3.

6. Run: pip install "python-socketio[client]" websocket-client

7. Start the Script befor every Stream and enjoy.

#StreamlabsLoyalty #Streamlabspoints #StreamerBot #StreambotPoints #StreamlabsLoyaltyPoints #SteamLabsPoints #Streamer.bot #StreamLabsStreamer.bot #PointswhitoutAffiliate
