You can try to our DEMO:
http://34.68.217.10/
(if this is can not connect, Please clone repositories this and build it to try)

## How to Build This?

1. go to import_file/command.py
2. find and change to your openai api key
```
# 設定 OpenAI API 的金鑰
OPENAI_API_KEY = "//Your open api key//"
```
3. back to / and install requirement
4. python3 app.py
5. open browser and connect URL
6. try it!

## How to use this web
1. You can connect our Web Application 
  http://34.68.217.10/
2. Enter desired address in Input

3. Press Sumit

4. Wait some Time

http://120.108.204.50:5000/

## Error fix
- if error message is Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
  - Please go to app.py and change port setting to else port
  - ```
    if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    ```
