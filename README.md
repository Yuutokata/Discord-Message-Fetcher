
# Discord Message Fetcher

This Python script retrieves messages from a specified Discord channel using Discord's API. It continuously fetches batches of messages until no more are available and saves them to a JSON file for later use.

## Features

-   Fetches up to 100 messages per request from a specified Discord channel.
    
-   Continuously retrieves older messages using the API's pagination.
    
-   Saves the accumulated results in a JSON file.
    
-   Customizable headers to match your Discord account configuration.
    

## Prerequisites

-   Python 3.x
    
-   Required Python modules:
    
    -   `json`
        
    -   `os`
        
    -   `requests`
        
    -   `time`
        
-   A valid Discord token, cookie, and other header details as required by Discord's API.
    

## Setup

1.  **Install the dependencies**  
    If you have not installed the  `requests`  library, run:
    
    bash
    
    `pip install -r requirements.txt` 
    
2.  **Download or clone the script**  
    Make sure the script file is in your working directory.
    

## Configuration

Before running the script, update the configuration parameters:

-   **Channel ID**  
    Replace  `"channel id"`  with the actual ID of the Discord channel you want to fetch messages from.
    
-   **Headers**  
    Replace the placeholder values in the headers dictionary:
    
    -   `"Authorization"`: Replace  `"your token"`  with your actual Discord token.
        
    -   `"cookie"`: Replace  `"your cookie"`  with your Discord cookie.
        
    -   `"referer"`,  `"user-agent"`,  `"x-super-properties"`, and  `"x-discord-timezone"`: Update these with values from your own request headers.
        
-   **Output File**  
    Update the variable  `file_name`  if you wish to change the default output JSON file name.
    

## Usage

To run the script:

1.  Open your terminal or command prompt.
    
2.  Navigate to the directory containing the script.
    
3.  Execute the script with:
    
    bash
    
    `python your_script_name.py` 
    

The script will:

-   Check if a JSON file already exists; if so, it will load previous messages.
    
-   Make requests to the Discord API to retrieve messages.
    
-   Append new messages to the JSON file.
    
-   Stop fetching when no new messages are returned or if a non-success status code is received.
    

## Notes

-   The script uses a delay of 1 second between API calls to help avoid triggering Discord's rate limits.
    
-   This script is intended for educational or personal use. Be aware of Discord's API policies and rate limits when fetching data.
    
-   Adjust error handling and logging based on your specific requirements, particularly for production deployments.
    

## Troubleshooting

-   **API Authentication:**  Ensure that all header values (token, cookie, etc.) are correct.
    
-   **Channel ID:**  Verify that the specified channel ID is valid.
    
-   **Rate Limits:**  If you encounter rate limiting, consider increasing the delay between requests.
