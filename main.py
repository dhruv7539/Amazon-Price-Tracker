import requests
from bs4 import BeautifulSoup
import smtplib,ssl

header={
'Accept-Language':"en-US,en;q=0.9",
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"

}
site=requests.get('https://www.amazon.in/DieseI-Chronograph-Black-Dial-Watch/dp/B07G78NM1C/ref=sr_1_1?pf_rd_i=62313278031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=dc590cfa-0ec5-40d8-a4d5-0e81d1b34256&pf_rd_r=6X53SXGFWJ13DY3XS2C5&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1674720902&s=watch&sr=1-1&srs=65085413031',headers=header).text

soup=BeautifulSoup(site,'lxml')
price=soup.select_one(selector=".a-section .a-spacing-none .aok-align-center .a-offscreen").getText()
price_without_currency=price.split("₹")[1].split(".")[0].split(",")
price_final=str("".join(price_without_currency))
price_as_float=float(price_final)
print(price_as_float)

if price_as_float<35000:

    port = 465  # For SSL
    password = "bfafzagqqzfbdjmh"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("birthdaywisher777@gmail.com", password)
        server.sendmail(from_addr="birthdaywisher777@gmail.com", to_addrs="birthdaywisher777@gmail.com", msg="Subject:Look up\n\nThe ISS is above you in the sky.")
