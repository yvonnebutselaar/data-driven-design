{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a URL http://www.jpcu.nl\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date : Wed, 10 Oct 2018 08:33:42 GMT\n",
      "Server : Apache/2\n",
      "Link : <https://www.jpcu.nl/wp-json/>; rel=\"https://api.w.org/\"\n",
      "X-TEC-API-VERSION : v1\n",
      "X-TEC-API-ROOT : https://www.jpcu.nl/wp-json/tribe/events/v1/\n",
      "X-TEC-API-ORIGIN : https://www.jpcu.nl\n",
      "Upgrade : h2,h2c\n",
      "Connection : Upgrade, Keep-Alive\n",
      "Vary : Accept-Encoding,User-Agent\n",
      "Content-Encoding : gzip\n",
      "Content-Length : 9720\n",
      "Keep-Alive : timeout=2, max=100\n",
      "Content-Type : text/html; charset=UTF-8\n",
      "Yay, everything works!\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "userin = input(\"Enter a URL\").strip()\n",
    "\n",
    "req = requests.get(userin)\n",
    "status = req.status_code\n",
    "headers = req.headers\n",
    "\n",
    "if status == 200:\n",
    "    print(\"Yay, everything works!\")\n",
    "    \n",
    "else:\n",
    "    print(\"Error, it doesn't work. Exiting now.\")\n",
    "    quit()\n",
    "\n",
    "for line in headers:\n",
    "val = headers[line]\n",
    "print(line + \" : \" + str(val))\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
