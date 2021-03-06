AI Assistant
=============

Custom  AI assistant that can handle natural language (mostly offline) and output commands. 

.. image:: snip.png
  :width: 400

Installation Guide
==================

Follow the instructions below that correspond to your environment.


Windows (Python 3.7) 
^^^^^^^^^^^^^^^^^^^^

#. Installer

    * Create a new 3.7 environment.
    * Run installer.py 
    * Let Hourglass install to default directory. This will be used for the timer application and it is a small 1mb binary.

#. GPT-3 API Auth

    * Create an accound on openai.com and go to API.
    * Locate API Key and copy to clipboard.
    * Export API key as environment variable:
    
    .. code-block:: console

        $env:OPENAI_API_KEY="your-key-here"

#. Spotipy API Auth (optional)

    * Create account on Spotify Developers and create a new application. Locate ID on Dashboard.

    * Navigate to modules/soptify/resources and open spotify.json.

    * Paste Client Id and Secret from Spotify Application Dashboard:

    .. code-block:: console

        {"client-id": "ID_HERE", "client-secret": "ID_HERE"}
    
