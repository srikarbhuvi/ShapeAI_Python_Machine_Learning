{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "shape ai project (weather).py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNhTM7ewyzgpH1NCNU3uAcM",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/srikarbhuvi/ShapeAI_Python_Machine_Learning/blob/main/shape_ai_project_(weather).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VtHY5iS08jDg"
      },
      "source": [
        "import requests\n",
        "#import as \n",
        "from datetime import datetime"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FvvpxgYT9dRK",
        "outputId": "e3e069eb-3841-4ae4-d865-57b86e181fc4"
      },
      "source": [
        "api_key = '00ef06c52ca9dbc727ff1bc505c4652d'\n",
        "location = input(\"enter the city name: \")"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "enter the city name: hyderabad\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EJAHQpst-E7D"
      },
      "source": [
        "complete_api_link =\"https://api.openweathermap.org/data/2.5/weather?q=\"+location+\"&appid=\"+api_key\n",
        "api_link = requests.get(complete_api_link)\n",
        "api_data = api_link.json()"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eZsZOv_q_kqp"
      },
      "source": [
        "#create variables to store and display data\n",
        "temp_city = ((api_data['main']['temp']) - 273.15)\n",
        "weather_desc = api_data['weather'][0]['description']\n",
        "hmdt = api_data['main']['humidity']\n",
        "wind_spd = api_data['wind']['speed']\n",
        "date_time = datetime.now().strftime(\"%d %b %Y | %I:%M:%S %p\")\n"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AendLvO4BqxB",
        "outputId": "a9f27b93-0deb-4d98-a820-43f569c455d3"
      },
      "source": [
        "print (\"current temperature is: {:.2f} deg C\".format(temp_city))\n",
        "print (\"current weather desc  :\",weather_desc)\n",
        "print (\"current humidity      :\",hmdt, '%')\n",
        "print (\"current wind speed    :\",wind_spd ,'kmph')"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "current temperature is: 29.54 deg C\n",
            "current weather desc  : haze\n",
            "current humidity      : 49 %\n",
            "current wind speed    : 2.57 kmph\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1HlmJS4-_LXG"
      },
      "source": [
        "f = open(\"result.txt\",\"w\")\n",
        "f.write(\"api_link.json()\")\n",
        "f.close()"
      ],
      "execution_count": 16,
      "outputs": []
    }
  ]
}